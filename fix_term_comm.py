import os

from fire import Fire
from openai import OpenAI


def main(message):
    client = OpenAI(api_key=os.environ['OPENAI_API_KEY'])
    system_prompt = "You are fixing Bash terminal commands. You produce only valid Bash commands without comments as a first line. You are often given a sketch with approximate names."

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": message}
        ],
        # stop=["\n"],
        temperature=0.6,
        n=1,
    )
    
    choice = completion.choices[0].message.content
    return choice


if __name__ == '__main__':
    Fire(main)
