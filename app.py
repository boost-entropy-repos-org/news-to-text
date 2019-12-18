from flask import Flask
from flask import request
from flask_cors import CORS

from get_article import get_article
from text_to_speech import text_to_speech

app = Flask(__name__, static_folder='public', static_url_path='')
# app.static_folder = 'public'
CORS(app)


@app.route('/')
def fetch_article():
    url = request.args.get('url')
    article = get_article(url)

    print(article.title)
    text_to_speech(article.text, article.title)

    return article.text
