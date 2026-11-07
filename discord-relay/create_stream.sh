#!/usr/bin/env bash
# Create a Redlisten stream that matches every new post in a given
# subreddit. Add an "any" list alongside "subreddits" if you only want
# posts that mention certain words within that subreddit.

curl -X POST "https://api.redlisten.com/v1/streams" \
  -H "Authorization: Bearer rl_live_YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "subreddit-watch",
    "subreddits": ["startups"],
    "types": ["post"]
  }'
