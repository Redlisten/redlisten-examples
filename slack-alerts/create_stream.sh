#!/usr/bin/env bash
# Create a Redlisten stream that matches any mention of your brand name
# or domain, across posts and comments. The word list goes under "any"
# (or "all" if every term must be present) -- not "keywords".
#
# Narrow further with "subreddits", "exclude_subreddits", or "authors"
# if your brand name is a common word and needs noise filtering.

curl -X POST "https://api.redlisten.com/v1/streams" \
  -H "Authorization: Bearer rl_live_YOUR_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "brand-mentions",
    "any": ["yourbrand", "yourbrand.com"],
    "types": ["post", "comment"]
  }'
