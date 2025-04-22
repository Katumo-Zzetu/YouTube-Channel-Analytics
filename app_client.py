# scripts/extraction/api_client.py
import os
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("logs/api_extraction.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

def get_youtube_api():
    """
    Creates and returns an authenticated YouTube API client.
    
        """
    try:
        api_key = os.environ.get('YOUTUBE_API_KEY')
        if not api_key:
            raise ValueError("YouTube API key not found in environment variables")
        
        youtube = build('youtube', 'v3', developerKey=api_key)
        logger.info("Successfully created YouTube API client")
        return youtube
    
    except HttpError as e:
        logger.error(f"HTTP error when creating YouTube API client: {str(e)}")
        raise
    except Exception as e:
        logger.error(f"Error creating YouTube API client: {str(e)}")
        raise


if __name__ == "__main__":
    youtube = get_youtube_api()
    print("YouTube API client created:", youtube)

