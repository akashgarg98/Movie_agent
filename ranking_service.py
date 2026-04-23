import os
from openai import OpenAI

class RankingService:
    def __init__(self, api_key):
        self.client = OpenAI(api_key=api_key)
        self.model = "gpt-4o-mini"

    def rank_movie(self, movie_details, online_sentiment):
        """Uses OpenAI to rank the movie and provide a summary including lead actors."""
        actors = movie_details.get('lead_actors', 'N/A')
        
        prompt = f"""
        Analyze the following movie and online consensus to decide if it's a "WATCH" or a "SKIP".
        
        Movie: {movie_details['title']}
        Lead Actors: {actors}
        Plot: {movie_details['overview']}
        Online Sentiment: {online_sentiment}
        
        Provide a response in this EXACT format:
        SUMMARY: Cast includes {actors}. {movie_details['overview']} (Audience sentiment: [1-sentence sentiment summary])
        RANKING: [WATCH or SKIP or CONSIDER]
        REASON: [1-sentence reason for the ranking]
        """
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            if "429" in str(e):
                return "SUMMARY: (Analysis unavailable)\nRANKING: CONSIDER\nREASON: API Limit reached."
            return f"SUMMARY: (Error: {str(e)})\nRANKING: N/A\nREASON: Error during analysis."
