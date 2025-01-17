# Reddit-AI-Bot
A Reddit bot that uses Groq AI to generate and post content automatically to a specified subreddit at a scheduled time.

# Setup Instructions:
Prerequisites:
Ensure you have the following installed before running the bot:

- Python 3.x - The code is written in Python.
- Groq API - You will need an API key for Groq AI.
- Reddit API - Set up Reddit API credentials (client ID, client secret, username, password).
------------------------------------
# Installation Steps:
- Clone the repository
- Install necessary libraries: Install the required dependencies using pip.
```
pip install praw openai groq
 ```
------------------------
### Set up Reddit API credentials: Edit the client_id, client_secret, username, and password in the code. 
Replace them with your own Reddit API credentials. 
> https://www.reddit.com/prefs/apps
```
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='YOUR_USER_AGENT',
    username='YOUR_USERNAME',
    password='YOUR_PASSWORD',
) 
```
## Set up Groq API: 
You will need an API key from Groq to access the content generation feature. You can obtain the API key from Groq's official site.
> Visit https://console.groq.com/keys
Replace the API key in the code:
``` client = Groq(api_key='YOUR_API_KEY') ```
-------------------------
# Run the bot: 
To run the bot, execute the following command, ensuring that you specify a scheduled post time.
```
python reddit_bot.py
```
--------------------------------
> Note: All actions performed by the bot, including content generation and posting to Reddit, are logged in the reddit_bot.log file. This log file helps you keep track of the bot's activities and debug if necessary. You 
 can check the log to understand the details of what the bot is doing at each step.
---------------------------------------

# Code Explanation:
- Reddit API Setup: The bot uses the praw library to connect to Reddit with the provided credentials. It posts to a specific subreddit (aricommunityai) by calling the subreddit.submit() method.
>  ### Visit to see the all the post, created by AI  -  https://www.reddit.com/r/aricommunityai/ 

- Groq API for Content Generation: Groq AI is used to dynamically generate content based on a random selection of topics. The API key is used to initialize the Groq client, and a request is made to generate a title and selftext.

- Content Scheduling: The bot schedules a post using the schedule_posting() function. It waits until the specified time to post, using the time.sleep() function to handle the waiting period.

- Logging: All actions, including content generation and Reddit posting, are logged in the reddit_bot.log file. This file records both successful operations and errors, allowing you to track the bot's activity and identify any issues.
---------------------------------
# Flowchart:
```
+-----------------+       +---------------------+       +-----------------------+
|  Start Bot      | ----> | Generate Content    | ----> | Post to Reddit        |
+-----------------+       +---------------------+       +-----------------------+
        |                        |                             |
        v                        v                             v
+----------------+       +-----------------------+       +---------------------------+
| Schedule Time  | ----> | Wait until Scheduled  | ----> | Log Activity / Error      |
+----------------+       +-----------------------+       +---------------------------+
```
# License
This project is licensed under the MIT License - see the LICENSE file for details.
