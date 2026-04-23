# 🍿 Automated Movie Intelligence Agent

An intelligent, Python-based movie discovery and ranking agent. This tool automates the process of identifying upcoming releases across global and local markets, analyzing audience sentiment using Large Language Models (OpenAI), and delivering curated weekly reports.

## 🌟 Why this project?
Recruiters and developers may find interest in several key architectural decisions:
- **AI-Driven Discovery**: Bypasses traditional API limitations (like TMDB regional blocks) by using OpenAI's reasoning capabilities to source current releases.
- **Cross-Industry Coverage**: Expertly identifies movies from **Hollywood (Global)**, **Bollywood (Hindi)**, and **South Indian Cinema (Telugu, Tamil, Kannada, Malayalam)**.
- **Sentiment Analysis Engine**: Integrates live web search (DuckDuckGo) with GPT-4o-mini to provide a "Watch or Skip" verdict based on real-time audience hype.
- **Security-First Design**: Implements industry-standard credential management via `.env` and `.gitignore` to prevent sensitive key exposure.

## 🛠️ Technology Stack
- **Language**: Python 3.x
- **AI Engine**: OpenAI GPT-4o-mini (via `openai`)
- **Web Discovery**: DuckDuckGo Search API (`ddgs`)
- **Automation**: `schedule` for periodic weekly execution
- **Delivery**: SMTP (Gmail) with personalized HTML templating

## 🚀 Key Features
- **Strict 7-Day Window**: Always provides a precise look at the *next* 7 days of cinema.
- **Rich Metadata**: Captures Release Date, Platform (OTT/Theatre), Lead Cast, and Plot.
- **Premium Reports**: Delivers a dark-themed, responsive HTML email with actionable YouTube trailer links.
- **Resilient Fallbacks**: Includes hardcoded data handles to ensure system stability if AI services are unavailable.

## ⚙️ Installation & Setup

1. **Clone the Repo**:
   ```bash
   git clone <your-repo-url>
   cd movieup
   ```

2. **Setup Environment**:
   - Install dependencies: `pip install -r requirements.txt`
   - Copy `.env.example` to `.env`.
   - Add your `OPENAI_API_KEY` and Gmail App Password.

3. **Run**:
   - Manual execute: `python agent.py`
   - Start 24/7 scheduler: `python scheduler.py`

## 📂 Project Architecture
- `agent.py`: Central orchestrator for the weekly workflow.
- `movie_service.py`: Handles AI-driven discovery and release identification.
- `search_service.py`: Scrapes web consensus and audience ratings.
- `ranking_service.py`: Performs LLM-based sentiment analysis and ranking.
- `email_service.py`: Generates and delivers the professional HTML watchlist.

---
*Created by [Akash Garg](https://github.com/akashgarg1920)*
