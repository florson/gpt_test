import os
import openai
from dotenv import load_dotenv

load_dotenv(override=True)

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_response(prompt):
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=100,
            temperature=0.7,
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {str(e)}"

if __name__ == "__main__":
    prompt = input("O co chcesz zapytać?: ")
    result = generate_response(prompt)
    print(result)


