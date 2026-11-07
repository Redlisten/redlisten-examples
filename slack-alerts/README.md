# slack-alerts

Get a Slack message every time your brand is mentioned on Reddit, using a [Redlisten](https://redlisten.com) keyword stream. Redlisten is not affiliated with Reddit, Inc.

## How it works

1. `create_stream.sh` creates a Redlisten stream that matches any post or comment containing your brand name or domain.
2. On the Pro plan and above, you can point that stream straight at a Slack incoming webhook from the Redlisten dashboard, no code required.
3. For more control over the message format, `app.py` is a small Flask relay: point the stream's webhook destination at it, and it formats and posts the Slack message itself.

## Setup

```bash
pip install flask requests
```

Edit `SLACK_WEBHOOK` in `app.py` with your Slack incoming webhook URL, then run:

```bash
python app.py
```

Deploy it somewhere that can receive a public POST request, then set that URL as your stream's webhook destination.

## Field names

Redlisten webhook payloads use Redlisten's own shape, not Reddit's raw field names:

| Field | Notes |
|---|---|
| `community` | the subreddit name, not `subreddit` |
| `author.name` | author is an object, not a flat string |
| `body` | the post/comment text; there is no separate `selftext` |
| `permalink` | already a full URL |

## Docs

https://redlisten.com/docs
