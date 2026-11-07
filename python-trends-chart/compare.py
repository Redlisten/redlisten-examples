"""
Compare Reddit mention volume for two or more keywords on the same
chart, in one API call. Useful for putting your own mention volume
next to a competitor's.

The comparison endpoint is on the Team plan and above.
"""

import requests
import matplotlib.pyplot as plt

API_KEY = "rl_live_YOUR_KEY"

resp = requests.get(
    "https://api.redlisten.com/v1/trends/compare",
    params={"q": "notion,obsidian", "interval": "day", "days": 30},
    headers={"Authorization": f"Bearer {API_KEY}"},
)
resp.raise_for_status()
compare_data = resp.json()

# Response comes back as "series", a list of one object per keyword,
# each holding its own "q" and "data" in the same shape as the
# single-keyword /v1/trends endpoint.
plt.figure(figsize=(10, 4))
for series in compare_data["series"]:
    keyword = series["q"]
    rows = series["data"]
    counts = [row["posts"] + row["comments"] for row in rows]
    plt.plot([row["t"][:10] for row in rows], counts, marker="o", label=keyword)

plt.legend()
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("compare.png")
