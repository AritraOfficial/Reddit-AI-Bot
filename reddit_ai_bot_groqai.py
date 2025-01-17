import praw
import openai
import os
import logging
from datetime import datetime
import time
import random

# Set up logging
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

# Function to generate content using Groq API (with dynamic prompt generation)
def generate_content():
    try:
        # Select a random topic each time
        topic = random.choice(topics)
        
        # Construct the prompt dynamically based on the selected topic
        prompt = f"Generate a bold title and one-liner about {topic}."
        
        # Initialize Groq client with API key
        from groq import Groq
        client = Groq(api_key= ("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"))

        # Request content generation
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.3-70b-versatile",  
            stream=False
        )

        # Extract the generated content
        generated_content = chat_completion.choices[0].message.content.strip()

        # Log the generated content
        logging.info(f"Generated Title: {generated_content}")
        
        # Split title and selftext from the generated content
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

# Function to post content to Reddit
def post_to_reddit(title, selftext):
    # Subreddit to post to
    subreddit_name = "aricommunityai"
    subreddit = reddit.subreddit(subreddit_name)

    try:
        # Submit the post to Reddit
        subreddit.submit(title=title, selftext=selftext)
        logging.info(f"Posted to Reddit: {title}")
    except Exception as e:
        logging.error(f"Error in posting to Reddit: {e}")

# Custom scheduling function that waits until the specified time to post
def schedule_posting(post_time):
    try:
        current_time = datetime.now()
        target_time = datetime.strptime(post_time, "%Y-%m-%d %H:%M")
        
        # Wait until the scheduled time
        time_difference = (target_time - current_time).total_seconds()
        if time_difference > 0:
            logging.info(f"Waiting for {time_difference} seconds until the scheduled post time.")
            time.sleep(time_difference)

        # Generate content and post to Reddit
        title, selftext = generate_content()
        if title and selftext:
            post_to_reddit(title, selftext)

    except Exception as e:
        logging.error(f"Error in schedule_posting: {e}")

# Example: Schedule a post at a specific time (e.g., 2025-01-17 09:30)
if __name__ == "__main__":
    post_time = "2025-01-17 11:49"  # Change this to your desired post time
    schedule_posting(post_time)
