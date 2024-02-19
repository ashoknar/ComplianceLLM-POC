from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def chatgpt_completion(messages):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125", 
        messages=messages,
        temperature= 0.0,
        top_p=1.0,
        presence_penalty=-0.0,
        frequency_penalty=0.0,
    )

    return str(completion.choices[0].message)


def check_content_compliance(compliance_policy, content):

    messages = [
        {
            "role": "system",
            "content": (
                f"You are an AI compliance system specialized in marketing policies. "
                f"Use this as the compliance policy: {compliance_policy}. "
                f"Follow the steps to check a marketing document for compliance with the specified policy. "
                f"Take the scraped website data as input from the user. "
                f"Consider format, structure, and relevant contextual information. Identify key criteria, e.g., truth in advertising, data protection. "
                f"Be aware of language nuances and marketing terminology. "
                f"Initiate the check using the policy. "
                f"Identify specific violations, clauses, or criteria that are not met. "
                f"For each violation, include the location and the specific text in the compliance policy and the document. "
                f"Provide feedback on the exact policy clause or criteria breached. "
                f"Only include suggestions if they are based on the compliance policy"
                f"Give details and suggestions for remediation."
            )
        },
        {
            "role": "user",
            "content": f"Content to check for compliance: {content}"
        }
    ]
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125", 
        messages=messages,
        temperature= 0.0,
        top_p=1.0,
        presence_penalty=0.0,
        frequency_penalty=0.0,
    )
    completion_text = str(completion.choices[0].message.content)

    return completion_text
