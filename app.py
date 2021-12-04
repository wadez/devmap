from flask import Flask, render_template, abort
from datetime import datetime

app = Flask(__name__, template_folder='views', static_folder="public", static_url_path="")

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')

@app.route('/p/<page>')
def fetch_page(page):
    page = str(page)
    slug = page.split(".")[0]
    try:
        return render_template("pages/" + slug + ".html")
    except Exception as e:
        abort(404)


if __name__ == '__main__':
    app.run()
