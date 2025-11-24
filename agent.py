from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SYSTEM_PROMPT = """
You are an intelligent AI assistant that extracts key product features from a given product description.

Read the paragraph carefully and output the most relevant information in JSON format. 
Be consistent with the JSON format for all products. Focus on attributes that describe the product’s identity, specifications, and benefits. Be concise, factual, and well-structured.

### Example 1
Product Description: "The Acme 3000 Blender has a 1000W motor, 5-speed settings, and a durable stainless steel blade. It is perfect for smoothies, soups, and crushing ice."
JSON Output:
{
    "product_name": "Acme 3000 Blender",
    "power": "1000W",
    "speeds": 5,
    "blade_material": "stainless steel",
    "uses": ["smoothies", "soups", "crushing ice"]
}

### Example 2
Product Description: "The CozySoft Cotton Blanket is made from 100% organic cotton, measures 60x80 inches, and provides warmth and comfort for all seasons."
JSON Output:
{
    "product_name": "CozySoft Cotton Blanket",
    "material": "100% organic cotton",
    "dimensions": "60x80 inches",
    "benefits": ["warmth", "comfort", "all seasons"]
}

### Now extract JSON for the given product description:
"""


def get_response(user_input: str):
    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_input}
        ],
        temperature=0.7,
        max_completion_tokens=1024,
        top_p=1,
        stream=True
    )

    response = ""
    for chunk in completion:
        text = chunk.choices[0].delta.content or ""
        print(text, end="")  # optional streaming in console
        response += text

    return response
