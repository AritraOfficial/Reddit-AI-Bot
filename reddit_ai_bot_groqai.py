import praw
import openai
import os
import logging
from datetime import datetime
import time
import random

logging.basicConfig(filename="reddit_bot.log", level=logging.INFO)

# Reddit API credentials
reddit = praw.Reddit(
    client_id='K8Pia996wNP3ijpKzb_eyQ',
    client_secret='UZQTg2ypEjM_mhie6FEewzC1XrahUg',
    user_agent='aibot',
    username='Aritra_Official',
    password='Aritra2025',
)

# Define the list of topics for dynamic content generation
topics = [
    "motivation", "business", "AI", "news", "self-improvement", 
    "technology", "leadership", "success", "entrepreneurship", "productivity"
]

# Function to generate content using Groq API 
def generate_content():
    try:
        
        topic = random.choice(topics)
        
        
        prompt = f"Generate a bold title and one-liner about {topic}."
        
    
        from groq import Groq
        client = Groq(api_key= ("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"))

        
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",  
            stream=False
        )

        
        generated_content = chat_completion.choices[0].message.content.strip()

        
        logging.info(f"Generated Title: {generated_content}")
        
        
        title_and_text = generated_content.split(":")
        if len(title_and_text) > 1:
            title = title_and_text[0].strip()
            selftext = title_and_text[1].strip()
        else:
            title = "Fallback Bold Title"
            selftext = "Fallback one-liner to inspire people."
        
        title = title.strip("*").strip()
        
        return title, selftext

    except Exception as e:
        logging.error(f"Error in generate_content: {e}")
        return None, None


def post_to_reddit(title, selftext):
    
    subreddit_name = "aricommunityai"
    subreddit = reddit.subreddit(subreddit_name)

    try:
        # Submit the post to Reddit
        subreddit.submit(title=title, selftext=selftext)
        logging.info(f"Posted to Reddit: {title}")
    except Exception as e:
        logging.error(f"Error in posting to Reddit: {e}")


def schedule_posting(post_time):
    try:
        current_time = datetime.now()
        target_time = datetime.strptime(post_time, "%Y-%m-%d %H:%M")
        
        
        time_difference = (target_time - current_time).total_seconds()
        if time_difference > 0:
            logging.info(f"Waiting for {time_difference} seconds until the scheduled post time.")
            time.sleep(time_difference)

        
        title, selftext = generate_content()
        if title and selftext:
            post_to_reddit(title, selftext)

    except Exception as e:
        logging.error(f"Error in schedule_posting: {e}")


if __name__ == "__main__":
    post_time = "2025-01-17 11:49"  
    schedule_posting(post_time)
