from flask import Flask, request, jsonify
import settings

from scraper import extract_web_content, extract_strip_content_policy
from llm import check_content_compliance


app = Flask(__name__)


@app.route("/check-compliance", methods=["POST"])
def check_compliance():
    request_json = request.get_json()
    url = request_json["url"]

    stripe_compliance_policy = extract_strip_content_policy()
    web_content = extract_web_content(url)

    result = check_content_compliance(stripe_compliance_policy, web_content)

    response = {"result": result}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9000, debug=True)
