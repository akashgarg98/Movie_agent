import schedule
import time
import logging
from agent import run_agent

# Configure logging
logging.basicConfig(
    filename='movie_agent.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def job():
    logging.info("Triggering weekly movie agent job...")
    try:
        run_agent()
        logging.info("Job completed successfully.")
    except Exception as e:
        logging.error(f"Job failed with error: {str(e)}")

# Schedule the job for every Thursday at 9:00 AM
schedule.every().thursday.at("09:00").do(job)

print("Movie Agent Scheduler is running...")
print("The agent will trigger every Thursday at 9:00 AM.")
logging.info("Scheduler started.")

while True:
    schedule.run_pending()
    time.sleep(60) # Check every minute
