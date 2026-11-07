# python-trends-chart

Pull daily Reddit mention counts for a keyword (or compare several) and plot them, using [Redlisten](https://redlisten.com)'s trends endpoints. Redlisten is not affiliated with Reddit, Inc.

## Scripts

- `mentions.py` -- daily mention counts for a single keyword over 30 days. Requires a **Pro** plan key.
- `compare.py` -- mention counts for multiple keywords on the same chart in one call. Requires a **Team** plan key.

## Setup

```bash
pip install requests matplotlib
```

Set `API_KEY` and `KEYWORD` (or the comma-separated `q` list in `compare.py`), then run:

```bash
python mentions.py
# or
python compare.py
```

Each script saves a `.png` chart to the current directory.

## Response shape

`/v1/trends` returns `{"data": [{"t": "...", "posts": N, "comments": N}, ...]}`.

`/v1/trends/compare` returns `{"series": [{"q": "...", "data": [...]}, ...]}`, one object per keyword, each in the same row shape as above.

Free preview (no key, no code): `https://redlisten.com/reddit/<keyword>?format=json`

## Docs

https://redlisten.com/docs
