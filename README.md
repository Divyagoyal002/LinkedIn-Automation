# LinkedIn Content Automation Agent

Automate high-quality LinkedIn posts every 3 days using **GPT-4o**, **Google Sheets**, and **Phantombuster** — no manual effort required.

---

## Problem

Staying active on LinkedIn with engaging, relevant content is hard.  
Ideas dry up, time runs out, and consistency suffers.

---

## Solution

This project automates the **end-to-end LinkedIn posting process**:

- Scrapes trending topics  
- Generates posts using GPT-4o  
- Stores content in Google Sheets  
- Auto-posts via Phantombuster every 3 days  
- Scheduled with a lightweight Python scheduler  

---

## Tech Stack

| Component         | Tool                      |
|------------------|---------------------------|
| LLM              | GPT-4o (via OpenAI API)   |
| Content Posting  | Phantombuster             |
| Storage          | Google Sheets             |
| Scheduler        | Python + `cron` / APScheduler |
| Data Sources     | Custom trending topic scraper |

---

## Project Structure

- ├── generate_post.py # Generates content using GPT-4o
- ├── trending_topic_scraper.py # Scrapes trending topics (Walmart Sparkathon, Twitter, etc.)
- ├── utils/
    - └── sheet_updater.py # Writes posts to Google Sheets
- ├── scheduler.py # Triggers the flow every 3 days
- ├── phantombuster_config.json # Settings for automated posting
  - └── README.md


---

## Features

- AI-generated content that sounds human and professional  
- Fully autonomous — no need to log into LinkedIn  
- Can be extended to support Twitter, Instagram, etc.  
- Easy to plug into any content marketing workflow  

---

## Setup Guide

### 1. Clone the repo

```bash
git clone https://github.com/yourname/linkedin-automation-agent.git
```
2. Set up Google Sheets API
  Link your sheet and update credentials in utils/sheet_updater.py.

3. Set up Phantombuster
  Add your API key and config to phantombuster_config.json.

4. Schedule the bot
  You can either:
  
  Run scheduler.py manually every 3 days, or
  
  Use cron to schedule it:
```
0 10 */3 * * /path/to/python scheduler.py
```
## Future Improvements

- Engagement tracking
- Multi-platform support
- AI post style customization (funny, professional, informative, etc.)
- Approval workflow before posting

## Contact
Made by Divya Goyal – feel free to connect or fork this repo to build your own LinkedIn autopilot.

### Demo
<p align="center"> <img src="demo.gif" width="600" alt="Demo GIF"> </p>

### Tags
#GPT4o #Automation #LinkedInMarketing #Python #Phantombuster #SideProject

### License
- MIT

