import requests
from bs4 import BeautifulSoup

def get_baidu_news():
    url = 'http://news.baidu.com/'  # 百度新闻首页地址
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')

    news_titles = []
    for item in soup.select('.hotnews a'):  # 假设新闻标题在.hotnews类下的a标签里
        title = item.text.strip()
        news_titles.append(title)

    return news_titles[:10]  # 取前10条新闻标题

if __name__ == '__main__':
    top_news = get_baidu_news()
    for i, news in enumerate(top_news, start=1):
        print(f"{i}. {news}")