import os
from openai import OpenAI
from dotenv import load_dotenv
from trending_topic_scraper import get_trending_topic
from utils.sheet_updater import push_to_sheet

# Load API Key from .env
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_linkedin_post():
    topic = get_trending_topic("AI in Retail")

    prompt = f"""Write a short (~150 words), engaging LinkedIn post about: "{topic}".
Use an informative and slightly optimistic tone. Include 1-2 relevant hashtags."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response.choices[0].message.content.strip()
    push_to_sheet(content)
    print("✅ Post generated and saved to Google Sheet.")

if __name__ == "__main__":
    generate_linkedin_post()
