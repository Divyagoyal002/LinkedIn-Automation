import os
import re
from openai import OpenAI
from dotenv import load_dotenv
from trending_topic_scraper import get_trending_topic
from utils.sheet_updater import push_to_sheet

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def clean_content(text):
    # for removing markdown bold/italic markers like **bold** or *italic*
    text = re.sub(r'\*\*(.*?)\*\*', r'\1', text)
    text = re.sub(r'\*(.*?)\*', r'\1', text)
    
    # to remove emojis 
    # text = re.sub(r'[^\w\s.,;:!?()#@&%-]', '', text)

    # Normalize spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def generate_linkedin_post():
    topic = get_trending_topic("AI in Retail")

    prompt = f"""Write a short (150 to 300 words), engaging LinkedIn post about: "{topic}".
    Use an informative and slightly optimistic tone. you can add an interactive closing line,
    if it is required as per the content. Include 8-10 relevant hashtags trending on linkedin."""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )

    raw_content = response.choices[0].message.content.strip()
    cleaned_content = clean_content(raw_content)
    push_to_sheet(cleaned_content)
    print("Post cleaned, generated, and saved to Google Sheet.")

if __name__ == "__main__":
    generate_linkedin_post()
