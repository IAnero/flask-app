from flask import Flask, render_template
import json
import os
from urllib.error import URLError
from urllib.request import Request, urlopen

app = Flask(__name__)

WAIFU_API_URL = os.environ.get("WAIFU_API_URL", "https://api.waifu.pics/sfw/waifu")


def fetch_waifu_url() -> str:
    req = Request(
        WAIFU_API_URL,
        headers={
            "Accept": "application/json",
            "User-Agent": "docker-curriculum-flask-app/1.0",
        },
    )
    with urlopen(req, timeout=5) as resp:
        payload = json.loads(resp.read().decode("utf-8"))
    url = payload.get("url")
    if not url:
        raise ValueError("Waifu API returned no url")
    return url


@app.route("/")
def index():
    url = None
    error = None
    try:
        url = fetch_waifu_url()
    except (URLError, ValueError) as e:
        error = str(e)
    return render_template("index.html", url=url, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
