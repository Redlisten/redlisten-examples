"""
Pull daily Reddit mention counts for a keyword over the last 30 days
and plot them. Same approach works for a brand name, a competitor, a
product category, or any topic you're researching.

The trends endpoint is on the Pro plan and above; a free key gets a
plan-required error here.
"""

import requests
import matplotlib.pyplot as plt

API_KEY = "rl_live_YOUR_KEY"
KEYWORD = "notion"

resp = requests.get(
    "https://api.redlisten.com/v1/trends",
    params={"q": KEYWORD, "interval": "day", "days": 30},
    headers={"Authorization": f"Bearer {API_KEY}"},
)
resp.raise_for_status()
data = resp.json()

# Response body is data["data"], a list of daily rows. Each row has a
# timestamp in "t" plus separate "posts" and "comments" counts.
rows = data["data"]
dates = [row["t"][:10] for row in rows]
counts = [row["posts"] + row["comments"] for row in rows]

plt.figure(figsize=(10, 4))
plt.plot(dates, counts, marker="o")
plt.xticks(rotation=45, ha="right")
plt.title(f'Reddit mentions of "{KEYWORD}" per day')
plt.ylabel("Mentions")
plt.tight_layout()
plt.savefig("mentions.png")
print(f"Saved chart with {sum(counts)} total mentions over {len(dates)} days")
