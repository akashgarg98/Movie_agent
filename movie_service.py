import os
from datetime import datetime, timedelta
import json
import re
from openai import OpenAI

class MovieService:
    def __init__(self, api_key=None):
        self.api_key = api_key

    def get_upcoming_movies(self, ranking_svc):
        """Discovers movies releasing in the next 7 days using OpenAI."""
        print("Discovering upcoming movies using OpenAI...")
        
        # Calculate the strict 7-day window (Today to Today + 6)
        start_date = datetime.now()
        end_date = start_date + timedelta(days=6)
        
        week_str = f"{start_date.strftime('%B %d, %Y')} to {end_date.strftime('%B %d, %Y')}"
        
        prompt = f"""
        Act as a movie discovery expert for the Indian and Global markets. 
        List up to 10 major movies releasing in theaters or on major streaming platforms during the week of {week_str}.
        
        CRITICAL: Include a diverse mix from Bollywood (Hindi), Hollywood (English), and South Indian Cinema (Telugu, Tamil, Kannada, Malayalam).
        
        For each movie, provide:
        1. Title
        2. Exact Release Date (YYYY-MM-DD)
        3. Platform (Specify exactly: "Theatre" or the name of the OTT service like "Netflix", "Disney+", "Prime", etc.)
        4. Lead Actors (comma separated)
        5. Plot Summary (exactly 2 sentences)
        6. Estimated IMDB/Rotten Tomatoes rating (or "N/A")
        
        Respond ONLY with a JSON list of objects.
        Format:
        [
            {{
                "title": "Movie Title",
                "release_date": "2026-04-23",
                "platform": "Netflix",
                "lead_actors": "Actor A, Actor B",
                "plot": "Plot sentence 1. Plot sentence 2.",
                "rating": "7.5"
            }}
        ]
        """
        
        try:
            response = ranking_svc.client.chat.completions.create(
                model=ranking_svc.model,
                messages=[{"role": "user", "content": prompt}],
                response_format={ "type": "json_object" } if "gpt-4o" in ranking_svc.model else None
            )
            content = response.choices[0].message.content
            
            # Extract JSON from markdown response if needed
            json_match = re.search(r'\[.*\]', content, re.DOTALL)
            if json_match:
                movies = json.loads(json_match.group(0))
            else:
                parsed = json.loads(content)
                movies = parsed.get("movies", parsed) if isinstance(parsed, dict) else parsed
            
            if not isinstance(movies, list):
                if isinstance(movies, dict):
                    for k in movies:
                        if isinstance(movies[k], list):
                            movies = movies[k]
                            break

            # Enrich and normalize fields
            for m in movies:
                m['id'] = 0
                title_query = m['title'].replace(' ', '+')
                m['trailer'] = f"https://www.youtube.com/results?search_query={title_query}+official+trailer"
                
                # Standardize keys for agent
                m['overview'] = m.get('plot', '')
                
            return movies
        except Exception as e:
            print(f"OpenAI Discovery Error: {e}")
            return self.get_hardcoded_fallback()

    def get_hardcoded_fallback(self):
        """Basic fallback if AI fails."""
        return [
            {
                'title': 'The Batman II (Sample)',
                'id': 0,
                'rating': 'N/A',
                'release_date': '2026-04-23',
                'platform': 'Theatre',
                'lead_actors': 'Robert Pattinson, Zoë Kravitz',
                'overview': 'The Dark Knight returns to face new challenges in Gotham.',
                'trailer': 'https://www.youtube.com/results?search_query=The+Batman+II+trailer'
            }
        ]
