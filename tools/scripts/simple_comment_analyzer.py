import sys
import json
import time
from urllib.parse import urlparse, parse_qs

# Note: This is a simplified educational script demonstrating how to use 
# basic scraping principles for YouTube comments without heavy APIs.
# For high volume, use 'yt-dlp' or 'google-api-python-client'.

def get_yt_video_id(url):
    query = urlparse(url).query
    params = parse_qs(query)
    return params.get("v", [None])[0]

def analyze_pain_points(comments):
    # Simulated internal logic for identifying common complaints
    keywords = ["tệ", "buồn", "không thể", "làm sao", "tại sao", "giúp", "vấn đề", "sai lầm"]
    pains = []
    for comment in comments:
        if any(word in comment.lower() for word in keywords):
            pains.append(comment.strip())
    return pains

def main():
    print("--- YouTube Comment Scraper (Minimalist) ---")
    url = input("Enter YouTube Video URL: ")
    video_id = get_yt_video_id(url)
    
    if not video_id:
        print("Invalid URL.")
        return

    print(f"Targeting Video ID: {video_id}")
    print("Tip: To run this for real, install 'yt-dlp' or use a Browser Extension to export CSV.")
    print("Action: Paste your exported comments here (one per line, end with Ctrl+D/Ctrl+Z):")
    
    try:
        user_comments = sys.stdin.readlines()
        if not user_comments:
            return
            
        pain_points = analyze_pain_points(user_comments)
        
        print("\n--- ANALYZED PAIN POINTS ---")
        for i, p in enumerate(pain_points[:10]):
            print(f"{i+1}. {p}")
            
        print("\nReady! Use these in 'youtube-script-master' to generate your script.")
            
    except EOFError:
        pass

if __name__ == "__main__":
    main()
