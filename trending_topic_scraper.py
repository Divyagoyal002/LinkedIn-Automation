import requests

def get_trending_topic(field="AI in Retail"):
    query = f"{field} site:techcrunch.com OR site:wired.com OR site:forbes.com"
    serp_api_key = "Your_api_key_here"
    
    url = "https://serpapi.com/search"
    params = {
        "q": query,
        "api_key": serp_api_key,
        "engine": "google",
        "num": 5
    }
    
    res = requests.get(url, params=params).json()
    if 'organic_results' in res:
        top_title = res['organic_results'][0]['title']
        return top_title
    return f"Latest trends in {field}"
