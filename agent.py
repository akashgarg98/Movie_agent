import os
from dotenv import load_dotenv
from movie_service import MovieService
from search_service import SearchService
from ranking_service import RankingService
from email_service import EmailService

# Load environment variables
load_dotenv()

def run_agent():
    print("Movie Agent is starting...")
    
    # Initialize services
    movie_svc = MovieService(os.getenv("TMDB_API_KEY"))
    search_svc = SearchService()
    ranking_svc = RankingService(os.getenv("OPENAI_API_KEY"))
    email_svc = EmailService(os.getenv("GMAIL_USER"), os.getenv("GMAIL_APP_PASSWORD"))
    
    recipient = os.getenv("RECIPIENT_EMAIL")
    
    # 1. Fetch movies
    movies = movie_svc.get_upcoming_movies(ranking_svc=ranking_svc)
    if not movies:
        print("No movies releasing this week.")
        return

    processed_movies = []
    
    # 2. Process each movie
    for movie in movies:
        print(f"Processing: {movie['title']}...")
        
        # Get online sentiment
        sentiment = search_svc.get_movie_sentiment(movie['title'])
        
        # Get AI ranking
        analysis = ranking_svc.rank_movie(movie, sentiment)
        
        movie['analysis'] = analysis
        processed_movies.append(movie)
        
        # Add a small delay to avoid rate limiting
        import time
        time.sleep(1)
        
    # 3. Send email report
    if processed_movies:
        print(f"Sending report to {recipient}...")
        success = email_svc.send_movie_report(recipient, processed_movies)
        if success:
            print("Weekly report sent successfully!")
        else:
            print("Failed to send report.")

if __name__ == "__main__":
    run_agent()
