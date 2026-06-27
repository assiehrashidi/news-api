import requests
from bs4 import BeautifulSoup
from fastapi import FastAPI
from groq import Groq
import os

app = FastAPI()

def get_news():
    url = "https://feeds.bbci.co.uk/persian/rss.xml"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "xml")
    titles = soup.find_all("title")
    news = []
    for title in titles[1:11]:
        text = title.text.strip()
        if text:
            news.append(text)
    return news
    
def summarize(news_list):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    news_text = "\n".join([f"{i+1}. {n}" for i, n in enumerate(news_list)])
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "user", "content": f"این اخبار اقتصادی رو به فارسی خلاصه کن:\n{news_text}"}
        ]
    )
    return response.choices[0].message.content

@app.get("/news")
def news():
    news_list = get_news()
    summary = summarize(news_list)
    return {
        "اخبار_امروز": news_list,
        "خلاصه_AI": summary
    }
