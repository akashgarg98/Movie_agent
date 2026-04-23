from duckduckgo_search import DDGS
import time

class SearchService:
    def __init__(self):
        self.ddgs = DDGS()

    def get_movie_sentiment(self, movie_title):
        """Searches for movie reviews and returns snippets for Gemini summary."""
        query = f"{movie_title} movie reviews consensus 2026"
        results = []
        try:
            # Get snippets from DuckDuckGo
            for r in self.ddgs.text(query, max_results=5):
                results.append(f"Source: {r['title']}\nSnippet: {r['body']}")
            
            # Simple delay to avoid rate limiting
            time.sleep(1)
        except Exception as e:
            results.append(f"Error searching for {movie_title}: {str(e)}")
            
        return "\n\n".join(results)

if __name__ == "__main__":
    # Test block
    service = SearchService()
    print(service.get_movie_sentiment("The Batman II"))
