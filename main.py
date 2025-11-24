from fastapi import FastAPI
from pydantic import BaseModel
from agent import get_response  # import the Groq logic

app = FastAPI(title="Product JSON Bot API", description="Returns product info in JSON format from product description")

# Request model
class ProductDescription(BaseModel):
    description: str

# Endpoint to extract product JSON
@app.post("/extract-json")
def extract_json(data: ProductDescription):
    """
    Accepts a product description and returns structured JSON from Groq LLM.
    """
    user_input = data.description
    response = get_response(user_input)  # call Groq
    return {"input": user_input, "output_json": response}
