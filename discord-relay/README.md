# discord-relay

Post new threads from a subreddit into a Discord channel automatically, using a [Redlisten](https://redlisten.com) stream and a Discord webhook instead of a persistent bot process. Redlisten is not affiliated with Reddit, Inc.

## How it works

1. `create_stream.sh` creates a Redlisten stream that matches every new post in a subreddit.
2. On the Pro plan and above, Redlisten's dashboard can deliver straight to a Discord destination with no code.
3. For a formatted embed (subreddit, author, snippet, link), `bot.py` is a small Flask relay: point the stream's webhook destination at it.

## Setup

In your Discord server: channel settings → Integrations → create a webhook, copy its URL.

```bash
pip install flask requests
```

Edit `DISCORD_WEBHOOK` in `bot.py`, then run:

```bash
python bot.py
```

Deploy it somewhere that can receive a public POST request, then set that URL as your stream's webhook destination.

## Field names

| Field | Notes |
|---|---|
| `community` | the subreddit name, not `subreddit` |
| `author.name` | author is an object, not a flat string |
| `body` | the post text; there is no separate `selftext` |
| `permalink` | already a full URL |

## Docs

https://redlisten.com/docs
