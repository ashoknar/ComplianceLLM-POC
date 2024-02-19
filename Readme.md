# Complance check LLM

The task is to build an API that does the following:

* Take a webpage as the input and it has to check the content in the page against a compliance policy
* Return the findings (non-compliant results) in the response

As an example, we take

Stripe's public compliance policy: https://stripe.com/docs/treasury/marketing-treasury
Lets test it against https://www.joinguava.com/

The task is to build a simple API in any language that checks the webpage copy against the policy and report the findings. 
You can use OpenAI or any open-source LLMs for this purpose.


## Quick Start
```
# Clone the repository
git clone https://github.com/ashoknar/ComplianceLLM-POC.git

# Create virtual environment
python -m venv venv

# Activate the environment
source venv/bin/activate

# Install the requirements
pip install -r requirements.txt

# Specify your API key here
API_KEY="your_key_here"

# Create the .env file
echo "OPENAI_API_KEY=${API_KEY}" > .env

# Start the server
python main.py

# Send a request to the server
curl --request POST \
  --url http://0.0.0.0:9000/check-compliance \
  --header 'Content-Type: application/json' \
  --data '{
        "url": "https://www.joinguava.com/"
}'
```


## Sample Output
```

I will now check the document for compliance with the specified policy on marketing Treasury-based services.

Violation:

The document uses the term "banking," which is recommended to be avoided.
Policy: "Many states have statutory prohibitions on references to 'banking,' 'banks,' and 'bank accounts' when the entities making these references are not state- or federally-chartered banks or credit unions."
Location: The term "banking" in the sentence "Guava is a banking and networking hub designed for Black entrepreneurs."
Suggestion: Replace "banking" with recommended terms like "money management" or "financial services."
Violation:

The document implies that Guava is a bank by using the term "banking hub."
Policy: "Avoid the terms in this list for any marketing programs you create because only financial institutions licensed as banks can use them."
Location: The phrase "banking hub" in the sentence "Guava is a banking and networking hub designed for Black entrepreneurs."
Suggestion: Use terms like "financial services hub" or "money management hub" instead.
Violation:

The document suggests that Guava offers banking products or services directly.
Policy: "Phrases that suggest your users receive banking products or services directly from bank partners should be avoided."
Location: The sentence "Guava is a banking and networking hub designed for Black entrepreneurs."
Suggestion: Reframe the sentence to avoid implying direct banking services, for example, "Guava offers financial services and networking for Black entrepreneurs."
Violation:

The document does not clarify the nature of the financial services provided by Guava.
Policy: "Create precise messaging for your users that complies with regulations."
Location: The sentence "Guava is a banking and networking hub designed for Black entrepreneurs."
Suggestion: Specify the type of financial services offered using recommended terms like "money management" or "financial services."
Violation:

The document does not mention the conditions under which the yield percentage might change.
Policy: "Always disclose prominently in your marketing materials that the yield percentage is subject to change and the conditions under which it might change."
Location: The document does not mention yield or its variability.
Suggestion: Include a statement about the variability of the yield percentage and the conditions that might lead to changes.
Violation:

The document does not include the required disclosures about FDIC insurance eligibility.
Policy: Information about FDIC insurance eligibility and required disclosures.
Location: The document does not mention FDIC insurance eligibility or the necessary disclosures.
Suggestion: If Guava offers FDIC insurance eligibility, ensure to include the approved terms and required disclosures as outlined in the compliance policy.
These violations need to be addressed to ensure compliance with the marketing policy for Treasury-based services.
```

## Files

- Compliance-LLM repository

  - Readme.md
    - Usage instructions, installation guidelines, and other relevant details.

  - llm.py
    - The main module for the Compliance-LLM project, containing the core functionality to prompt GPT to analyze the compliance policy and website data to check for compliance.

  - main.py
    - The entry point  containing flask server functionality for the Compliance-LLM project.

  - requirements.txt
    - Rquirements file to create the virtual environment.

  - scraper.py
    - Script for data extraction from websites using GPT to extract the text data from scraped HTML.

  - LICENSE
    - The license file outlining the terms and conditions for using the Compliance-LLM project.

  - settings.py
    - Contains code to securely import the OPEN_AI_KEY.