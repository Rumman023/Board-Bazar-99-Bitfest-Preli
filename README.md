# Board-Bazar-99-Bitfest-Preli
KUET Bitfest Hackathon Preli

CHALLENGE 2
# Mofa’s Kitchen Buddy API

## Setup Instructions

### Prerequisites
- Python 3.x
- MySQL database setup
- OpenAI API key (if using chatbot functionality)

### Installation

1. **Clone the repository**:  
   `git clone https://github.com/Rumman023/Board-Bazar-99-Bitfest-Preli`  

2. **Create a virtual environment**:  
   `python -m venv venv`

3. **Activate the virtual environment**:  
   - On **Windows**:  
     `venv\Scripts\activate`  
   - On **macOS/Linux**:  
     `source venv/bin/activate`

4. **Install the required dependencies**:  
   `pip install -r requirements.txt`

5. **Set up your MySQL database** and update the `db_config.py` file with your credentials.The schema structure is given in the Challenge 2\1.Database Schema folder

6. **Start the Flask application**:  
   `python app.py`  
   The API will now be running on `http://127.0.0.1:5000`.
   To test the chatbot feature run `python Ingredient_API.py` 
   you will need an openAI key for this.

### Using Postman

You can use [Postman](https://www.postman.com/) to test the API:

1. Open Postman and create a new request.
2. Set the request type (GET, POST, PUT) based on the API method you want to test.
3. Enter the URL (e.g., `http://127.0.0.1:5000/ingredients`).
4. For POST and PUT requests, add the JSON payload in the body tab.
5. Send the request and check the response.

## Tech Stack

- **Backend**: Flask
- **Database**: MySQL
- **Python Libraries**:
  - `Flask` for creating the API
  - `MySQL-connector` for connecting to MySQL
  - `openai` for chatbot integration (if used)
  - `requests` for external API calls (if needed)
