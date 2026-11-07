# mcp-config

Give an AI agent Reddit search with MCP, using [Redlisten](https://redlisten.com)'s hosted MCP server. Redlisten is not affiliated with Reddit, Inc.

## What you get

Without an API key, the server still connects and offers two read-only tools: `reddit_preview` and `subreddit_preview`. With a free key, it adds `search_reddit`, `latest_posts`, `latest_comments`, `get_thread`, `user_history`, and stream management tools (`list_streams`, `create_stream`, `stream_items`).

A few tools need a paid plan on top of a key: `keyword_trends` needs Pro, `compare_keywords` and `top_communities` need Team. They still show up in the tool list either way; calling one without the right plan just returns a plan-required error instead of data.

## Setup

Copy `mcp.json` into your MCP client's configuration (this `url`-and-`headers` format works in Cursor and other MCP clients that take a raw config file). Replace `rl_live_YOUR_KEY` with your own key from [app.redlisten.com](https://app.redlisten.com/?signup=1).

Claude desktop app: add remote MCP servers through its own connectors screen rather than a config file. Check Claude's current documentation for the exact steps.

Claude Code:

```bash
claude mcp add --transport http redlisten https://api.redlisten.com/mcp \
  --header "Authorization: Bearer rl_live_YOUR_KEY"
```

## Trying it without setup

Free preview pages, built to be read and quoted by AI models directly:

- `https://redlisten.com/reddit/<keyword>` (also available as `?format=json`)
- `https://redlisten.com/r/<subreddit>` (also available as `?format=json`)

## Docs

https://redlisten.com/docs
