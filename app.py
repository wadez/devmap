from flask import Flask, render_template, abort, make_response
from datetime import datetime

app = Flask(__name__, template_folder='views', static_folder="public", static_url_path="")
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.context_processor
def inject_now():
    return {'now': datetime.utcnow()}

@app.route('/')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/sitemap.xml')
def fetch_sitemap():
    resp = make_response(render_template("sitemap.xml"))
    resp.headers['Content-type'] = 'text/xml; charset=utf-8'
    return resp

@app.route('/p/<slug>')
def page(slug):
    slug = str(slug).split(".")[0]
    try:
        return render_template("pages/" + slug + ".html")
    except Exception as e:
        print(e)
        abort(404)


if __name__ == '__main__':
    app.run()
