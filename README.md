# Movie Agent Setup Guide

This guide will help you set up and run the Movie Agent on your local machine.

## Prerequisites
- **Python 3.8+** installed.
- **Git** installed.

## Step 1: Clone the Repository
Open your terminal and run:
```bash
git clone https://github.com/akashgarg98/Movie_agent.git
cd Movie_agent
```

## Step 2: Install Dependencies
Install the required Python libraries:
```bash
pip install -r requirements.txt
```

## Step 3: Setup Environment Variables
1. Create a new file named `.env` in the root folder.
2. Copy the contents of `.env.example` into `.env`.
3. Fill in your API keys and email details:
   - `TMDB_API_KEY`: Your TMDB API key.
   - `OPENAI_API_KEY`: Your OpenAI API key.
   - `GMAIL_USER`: Your Gmail address.
   - `GMAIL_APP_PASSWORD`: Your Gmail App Password.
   - `RECIPIENT_EMAIL`: The email address where you want to receive reports.

## Step 4: Run the Agent
To start the agent and send a movie report immediately, run:
```bash
python agent.py
```

## Optional: Schedule the Agent
If you want the agent to run automatically on a schedule, run:
```bash
python scheduler.py
```

---
*Happy Movie Watching!*
