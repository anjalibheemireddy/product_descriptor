# Product JSON Extractor Bot

A lightweight AI-powered tool that extracts structured JSON from free-form product descriptions.
This project uses:

Streamlit for the frontend chat interface

FastAPI as the backend API service

Groq LLM for natural-language understanding and JSON generation

---

## Prerequisites

-Python 3.10 or higher

-pip for dependency management

-A Groq API key

---

## Installation

1. Clone the repository
```bash
git clone <repository_url>
cd product-json-extractor
```

2. Create a virtual environment
```bash
conda create -p venv python=3.12 -y
```

(You may use any other method to create a virtual environment.)

3. Activate the environment
```bash
conda activate ./venv 
```

4. Install dependencies
```bash
pip install -r requirements.txt
```

5. Add your API key

Create a .env file in the project root:
```bash
GROQ_API_KEY=your_groq_key
```

---

## Usage

Start the FastAPI Backend
```bash
uvicorn main:app --reload
```

Run the Streamlit Frontend
```bash
streamlit run app.py
```

---
## Interacting With the Bot

- Paste any product description such as:

“This vacuum cleaner has 1200W power, HEPA filter, 2-liter dust capacity.”

“An organic cotton pillow, soft and hypoallergenic, size 20x26 inches.”

- The bot will return structured JSON with fields like:

```bash
{
  "product_name": "",
  "features": [],
  "material": "",
  "size": "",
  "specifications": {}
}
```

---

## Features

- Converts unstructured product descriptions into clean, consistent JSON

- Uses few-shot prompting for highly reliable output

- Export chat as a text file

- Backend and frontend separated for 
scalability
---


## Workflow

1. User Input
User enters a product description in Streamlit.

2. FastAPI Processing
Streamlit sends the text to FastAPI → Groq LLM processes and extracts JSON.

3. Structured Output
Assistant returns a clean JSON block, shown in the chat UI.

4. Chat History
Messages are preserved and can be exported.
---


## License

This project is licensed under the terms included in the LICENSE file.
---

## Author

- Anjali Bheemireddy
- 📧 anjalinature156@gmail.com

