"""
Post a Slack message whenever a Redlisten stream matches a new Reddit
post or comment. Point your Redlisten stream's webhook destination at
wherever this is deployed.

Redlisten webhook payloads use Redlisten's own field names, not Reddit's
raw ones:
  - item["community"]        (not "subreddit")
  - item["author"]["name"]   (author is an object, not a flat string)
  - item["body"]             (no separate "selftext" field)
  - item["permalink"]        (already a full URL)

See: https://redlisten.com/docs
"""

from flask import Flask, request
import requests

app = Flask(__name__)
SLACK_WEBHOOK = "https://hooks.slack.com/services/your/webhook/url"


@app.route("/redlisten-webhook", methods=["POST"])
def handle_mention():
    item = request.json
    text = (
        f":loudspeaker: New mention in r/{item['community']}\n"
        f"*{item.get('title') or item['body'][:140]}*\n"
        f"Posted by u/{item['author']['name']}\n"
        f"<{item['permalink']}|View on Reddit>"
    )
    requests.post(SLACK_WEBHOOK, json={"text": text})
    return "", 200


if __name__ == "__main__":
    app.run(port=5000)
