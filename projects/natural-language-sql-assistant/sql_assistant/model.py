
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize Gemini
model = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)


def get_model_response(message):
    response = model.invoke(message)

    return response.text
