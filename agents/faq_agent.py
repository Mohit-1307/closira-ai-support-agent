import json
from dotenv import load_dotenv
from openai import OpenAI
load_dotenv()
import os

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def load_sop():
    with open("data/sop.json", "r") as file:
        return json.load(file)


sop_data = load_sop()


SYSTEM_PROMPT = f"""
You are an AI assistant for Bloom Aesthetics Clinic.

You MUST answer ONLY using the SOP below.
Do NOT make up, infer, assume, or hallucinate any information not explicitly present in the SOP.
If information is missing, say:
'I could not find that information in our policy documents. I will escalate this to a human representative.'

SOP:
{sop_data}
"""


def answer_question(user_message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_message}
        ],
        temperature=0
    )

    return response.choices[0].message.content