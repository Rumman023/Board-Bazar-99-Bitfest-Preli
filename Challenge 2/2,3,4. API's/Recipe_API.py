from flask import Flask, request, jsonify
import openai
from db_config import get_db_connection

app = Flask(__name__)


#openai.api_key = ''


# Endpoint for the chatbot to get user input and process preferences
@app.route('/chatbot', methods=['POST'])
def chatbot():
    data = request.json
    user_input = data.get("message")

    if not user_input:
        return jsonify({"error": "Message is required"}), 400

    user_preferences = get_user_preferences_from_llm(user_input)

    if not user_preferences:
        return jsonify({"error": "Unable to understand user preferences"}), 400

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT name FROM Ingredients WHERE quantity > 0")
        ingredients_in_stock = [row[0].lower() for row in cursor.fetchall()]

        cursor.close()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT id, name, ingredients, taste, cuisine FROM Recipes")
        recipes = cursor.fetchall()

        matching_recipes = []

        for recipe in recipes:
            recipe_id, recipe_name, recipe_ingredients, taste, cuisine = recipe
            recipe_ingredients_list = [ingredient.strip().lower() for ingredient in recipe_ingredients.split(',')]

            # Check if recipe ingredients are available in stock
            if all(ingredient in ingredients_in_stock for ingredient in recipe_ingredients_list):
                # Apply preferences filter
                if user_preferences.get('taste') and user_preferences['taste'] != taste.lower():
                    continue  # Skip if taste doesn't match
                if user_preferences.get('cuisine') and user_preferences['cuisine'] != cuisine.lower():
                    continue  # Skip if cuisine doesn't match

                matching_recipes.append({
                    "recipe_id": recipe_id,
                    "recipe_name": recipe_name,
                    "ingredients": recipe_ingredients_list,
                    "taste": taste,
                    "cuisine": cuisine
                })

        cursor.close()
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    if matching_recipes:
        return jsonify({
            "message": "Recipe suggestions found!",
            "recipes": matching_recipes
        }), 200
    else:
        return jsonify({
            "message": "No matching recipes found. Try a different combination of ingredients or preferences."
        }), 404


def get_user_preferences_from_llm(user_input):
    """Use OpenAI GPT model to process user input and return preferences."""

    try:

        response = openai.Completion.create(
            engine="gpt-4",
            prompt=f"Extract user preferences (e.g., taste, cuisine, dietary restrictions) from the following message: '{user_input}'",
            max_tokens=100,
            temperature=0.7,
        )

        # Parse the response and extract preferences
        preferences = response.choices[0].text.strip().lower()
        preferences_dict = {}

        if "sweet" in preferences:
            preferences_dict["taste"] = "sweet"
        if "spicy" in preferences:
            preferences_dict["taste"] = "spicy"
        if "vegetarian" in preferences:
            preferences_dict["diet"] = "vegetarian"
        if "italian" in preferences:
            preferences_dict["cuisine"] = "italian"

        return preferences_dict
    except Exception as e:
        print(f"Error processing LLM: {e}")
        return None


if __name__ == '__main__':
    app.run(debug=True)
