from flask import Flask, request, jsonify
from db_config import get_db_connection

app = Flask(__name__)
@app.route('/ingredients', methods=['POST'])
def add_ingredient():
    data = request.json
    name = data['name']
    quantity = data['quantity']
    unit = data.get('unit', '')
    category = data.get('category', '')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Ingredients (name, quantity, unit, category) VALUES (%s, %s, %s, %s)",
            (name, quantity, unit, category)
        )
        conn.commit()
        return jsonify({"message": "Ingredient added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


@app.route('/ingredients/<int:ingredient_id>', methods=['PUT'])
def update_ingredient(ingredient_id):
    data = request.json
    quantity = data.get('quantity')
    unit = data.get('unit')
    category = data.get('category')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE Ingredients SET quantity = %s, unit = %s, category = %s WHERE id = %s",
            (quantity, unit, category, ingredient_id)
        )
        conn.commit()
        return jsonify({"message": "Ingredient updated successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        conn.close()


@app.route('/adjust_ingredient', methods=['PUT'])
def adjust_ingredient():
    data = request.json
    name = data.get('name')
    adjustment = data.get('adjustment')  # Can be positive (add) or negative (subtract)

    if not name or adjustment is None:
        return jsonify({"error": "Ingredient name and adjustment value are required"}), 400

    connection = get_db_connection()
    cursor = connection.cursor()
    try:
        # Fetch the current quantity
        cursor.execute("SELECT id, quantity FROM Ingredients WHERE name = %s", (name,))
        ingredient = cursor.fetchone()

        if not ingredient:
            return jsonify({"error": "Ingredient not found"}), 404

        ingredient_id, current_quantity = ingredient
        new_quantity = current_quantity + adjustment

        # Ensure the quantity doesn't go below zero
        if new_quantity < 0:
            return jsonify({"error": "Insufficient quantity. Adjustment would result in negative quantity."}), 400

        # Update the quantity in the database
        cursor.execute(
            "UPDATE Ingredients SET quantity = %s WHERE id = %s",
            (new_quantity, ingredient_id)
        )
        connection.commit()

        return jsonify({
            "message": "Ingredient quantity updated successfully",
            "name": name,
            "previous_quantity": current_quantity,
            "adjustment": adjustment,
            "new_quantity": new_quantity
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()

import os

RECIPE_FILE = "my_fav_recipes.txt"

# API to add a new recipe text
@app.route('/add_recipe', methods=['POST'])
def add_recipe():
    data = request.json
    name = data.get('name')
    ingredients = data.get('ingredients')
    cuisine = data.get('cuisine', 'Unknown')
    taste = data.get('taste', 'Unknown')
    prep_time = data.get('prep_time', 0)
    reviews = data.get('reviews', '')

    if not name or not ingredients:
        return jsonify({"error": "Name and ingredients are required"}), 400

    recipe_text = f"""
Name: {name}
Ingredients: {', '.join(ingredients)}
Cuisine: {cuisine}
Taste: {taste}
Preparation Time: {prep_time}
Reviews: {reviews}
"""
    try:
        with open(RECIPE_FILE, 'a') as file:
            file.write(recipe_text.strip() + '\n\n')
        return jsonify({"message": "Recipe added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
