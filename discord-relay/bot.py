"""
Post new Reddit threads into a Discord channel as formatted embeds,
driven by a Redlisten stream webhook -- no bot process required.

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
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/your/webhook"


@app.route("/redlisten-webhook", methods=["POST"])
def new_post():
    item = request.json
    embed = {
        "title": item["title"][:256],
        "url": item["permalink"],
        "description": item["body"][:300],
        "footer": {"text": f"Posted by u/{item['author']['name']} in r/{item['community']}"},
    }
    requests.post(DISCORD_WEBHOOK, json={"embeds": [embed]})
    return "", 200


if __name__ == "__main__":
    app.run(port=5000)
