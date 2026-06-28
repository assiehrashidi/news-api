# AI-Powered News API

A self-taught project that scrapes live Persian economic news 
and summarizes it using an LLM — served via a REST API.

## Tech stack
- Python
- BeautifulSoup (web scraping)
- Groq API + LLaMA 3.3 70B (AI summarization)
- FastAPI (REST API)

## How to run

1. Clone the repository:
git clone https://github.com/a-rashidi75/news-api

2. Install dependencies:
pip install -r requirements.txt

3. Set your Groq API key:
Get a free key from console.groq.com
set GROQ_API_KEY=your_key_here

4. Run the API:
python -m uvicorn main:app --reload

5. Open in browser:
http://127.0.0.1:8000/news
