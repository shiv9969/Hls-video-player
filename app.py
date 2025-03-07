from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    video_url = "https://jf5.dunyapurkaraja.com:999/hls/starhindi.m3u8?md5=-aWT2AkN8mIVmvrrTc3YhQ&expires=1741282662"
    return render_template("index.html", video_url=video_url)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
