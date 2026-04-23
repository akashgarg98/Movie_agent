# 🍿 Movie Agent

An AI-powered agent that scrapes upcoming movie releases, ranks them using Gemini AI based on online sentiment and ratings, and sends a weekly report to your email every Thursday.

## 🚀 Features
- **Upcoming Movies**: Fetches movies releasing this week via the TMDB API.
- **Online Consensus**: Searches the web (via DuckDuckGo) for public sentiment and reviews.
- **AI Ranking**: Uses Gemini 1.5 Flash to categorize movies into **MUST WATCH**, **CONSIDER**, or **SKIP**.
- **Weekly Delivery**: Sends a beautiful HTML report to your Gmail every Thursday morning.

## 🛠️ Setup

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment Variables**:
   - Copy `.env.example` to `.env`.
   - Fill in your `TMDB_API_KEY`, `GEMINI_API_KEY`, and Gmail credentials.

3. **Gmail App Password**:
   - To send emails, you need a Google App Password. [Learn how to create one here](https://support.google.com/accounts/answer/185833).

4. **Run the Agent**:
   - To run once immediately:
     ```bash
     python agent.py
     ```
   - To keep it running on a schedule:
     ```bash
     python scheduler.py
     ```

## 📂 Project Structure
- `agent.py`: The main orchestrator.
- `movie_service.py`: TMDB integration.
- `search_service.py`: Web search integration.
- `ranking_service.py`: Gemini AI ranking logic.
- `email_service.py`: HTML email generation and SMTP.
- `scheduler.py`: The weekly trigger logic.
