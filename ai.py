from openai import OpenAI

def query_ai(assumptions: list, to_show: str):
    client = OpenAI()
    content = "Assume "
    assumption_phrase = ' and '.join(assumptions)
    content += assumption_phrase
    content += ". "
    content += "Show that " + to_show
    
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a mathematical processor, designed to produce proofs based off of given assumptions, giving consice responses at most 3 lines long"},
            {"role": "user", "content": content}
        ]
    )

    return completion.choices[0].message.content

