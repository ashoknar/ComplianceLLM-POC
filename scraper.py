import requests
from llm import chatgpt_completion
from lxml import html


def extract_web_content(url: str):

    response = requests.get(url)
    response.raise_for_status()

    messages = [
        {
            "role": "system",
            "content": "You are a bot that extracts content from an html page. Keep the content of the page unmodified.",
        },
        {
            "role": "user",
            "content": f"Extract the text from this html page: {response.text}",
        },
    ]

    web_content = chatgpt_completion(messages)

    return web_content


def extract_strip_content_policy():

    url = "https://stripe.com/docs/treasury/marketing-treasury"
    page = requests.get(url)
    page.raise_for_status()

    tree = html.fromstring(page.content)

    # we are using xpath to locate the element containing the compliance information because the page is too big to directly pass to chatgpt

    compliance_html = tree.xpath(
        '//*[@id="root"]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]'
    )
    compliance_html_str = compliance_html[0].text_content()

    messages = [
        {
            "role": "system",
            "content": "You are a bot that extracts content from an html page. Keep the content of the page unmodified.",
        },
        {
            "role": "user",
            "content": f"Extract the text from this html page: {compliance_html_str}",
        },
    ]

    compliance_content = chatgpt_completion(messages)

    return compliance_content
