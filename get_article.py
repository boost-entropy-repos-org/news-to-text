from newspaper import Article
from text_to_speech import text_to_speech


def get_article(url):
    print("fetching: " + url)
    article = Article(url)
    article.download()
    article.parse()
    return article


if __name__ == '__main__':
    url = input('enter article url: ')
    article = get_article(url)
    print(article.title)
    print(article.text)
    text_to_speech(article.text)
