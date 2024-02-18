from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chatgpt_completion(messages):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages
    )

    return str(completion.choices[0].message)


def check_content_compliance(compliance_policy, content):

    messages = [
        {
            "role": "system",
            "content": f"You are a compliance officer who checks contents for web site against the compliance policy: {compliance_policy}",
        },
        {"role": "user", "content": f"Content to check for compliance: {content}"},
    ]

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo", messages=messages
    )
    completion_text = str(completion.choices[0].message.content)

    return completion_text
