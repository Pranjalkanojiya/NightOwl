import os

from dotenv import load_dotenv
from groq import Groq


load_dotenv()


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def generate_answer(question, results):

    evidence = "\n\n".join(
        f"Source: {r['chunk']['source']} | "
        f"Page: {r['chunk']['page']}\n"
        f"{r['chunk']['text']}"
        for r in results
    )


    prompt = f"""
You are NightOwl, an evidence-first study assistant.

Your job is to answer questions ONLY from the
provided course material.

STRICT RULES:

1. Use ONLY the evidence provided below.
2. Do NOT use outside knowledge.
3. Do NOT guess or invent information.
4. If the evidence does not contain enough information
   to answer the question, respond exactly:

"I couldn't find enough information in your uploaded material."

5. Keep answers concise and useful for a student.
6. When possible, structure explanations using short
   paragraphs or bullet points.
7. Never claim something is present in the material
   unless it actually appears in the evidence.


QUESTION:
{question}


EVIDENCE:
{evidence}
"""


    response = client.chat.completions.create(

        model="openai/gpt-oss-20b",

        messages=[
            {
                "role": "system",
                "content": (
                    "You are a precise, evidence-first "
                    "study assistant."
                )
            },
            {
                "role": "user",
                "content": prompt
            }
        ],

        temperature=0.1,

        max_tokens=700
    )


    return response.choices[0].message.content