# Board-Bazar-99-Bitfest-Preli
KUET Bitfest Hackathon Preli

CHALLENGE 1:
Link:https://huggingface.co/rummanadib023/Banglish_To_Bengali_Board_Bazar_99/tree/main
## Tech Stack & Tools Used

1. **Programming Language**: Python
2. **Libraries & Frameworks**:
   - **AutoTokenizer**: Used to tokenize the input text.
   - **AutoModelForSeq2SeqLM**: Used to load and fine-tune the mBART model.
   - **Seq2SeqTrainer**: Handles the training and evaluation process of the model.
   - **PyTorch**: Used for model training.
   - **scikit-learn**: Used to split the dataset into training and validation sets (80/20 split).
   - **Hugging Face Model Hub**: For loading pre-trained models and tokenizers and sharing the fine-tuned model.
3. **Environment**: Jupyter Notebook for the development and execution of code.

## Model & Hyperparameter Choices

- **Model**: `facebook/mbart-large-50-many-to-many-mmt` (mBART)
   - **Reason for Choice**: mBART is a multilingual model designed for translation tasks. It is suitable for low-resource languages because it leverages knowledge from other languages, improving performance on languages with limited data.
   
- **Learning Rate**: `3e-5`
   - **Reason for Choice**: This learning rate is widely used as a default for fine-tuning transformer models and ensures stable convergence without causing divergence or overfitting.

- **Batch Size**: `32`
   - **Reason for Choice**: A batch size of 32 strikes a balance between memory usage and effective gradient updates, providing a good compromise for efficient training on limited resources.

- **Number of Epochs**: `1`
   - **Reason for Choice**: Given the small training dataset (500 examples), only one epoch is chosen to avoid overfitting while achieving decent performance in the short available training time.

- **Total Training Examples**: `500` (training) and `100` (validation)
   - **Reason for Choice**: Limited data due to time constraints. This may not yield optimal results, but fine-tuning with a larger dataset and more epochs would improve performance.


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
