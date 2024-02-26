import openai

def process_question(codebase, prompt):
    client = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": prompt + codebase},
        ],
    )
    return client.choices[0].message.content
