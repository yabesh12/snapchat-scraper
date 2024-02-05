from flask import Flask, request, jsonify
import threading
from db import user_profile_collection
from scraper_thread import scrape_and_store_profile_data
import re
from urllib.parse import urlparse

app = Flask(__name__)

@app.route('/')
def home():
    return "Application server started!"

@app.route('/scrape-user-profile/', methods=['POST'])
def scrape_user_profile():
    try:
        # Get user URL from request body
        url = request.json.get('profile_url')

        snapchat_url_pattern = re.compile(r'https://www\.snapchat\.com/add/[a-zA-Z0-9_]+')


        if not url:
            return jsonify({'error': 'Missing profile_url in the request body'})
        
        # Validate the URL format
        if not snapchat_url_pattern.match(url):
            return jsonify({'error': 'Invalid Snapchat profile URL format'})
        

        # Extract username
        username = urlparse(url).path.split('/add/')[1]

        # Check if the username already exists in the database
        existing_profile = user_profile_collection.find_one({'profile_username': username})

        if existing_profile:
            print(f"Profile with username {username} already exists. Skipping scraping.")
            return jsonify({"message": f"Profile with username {username} already exists"})
        
        # Run scraping and storing in the background using threading
        threading.Thread(target=scrape_and_store_profile_data, args=(url,username)).start()

        return jsonify({"status": "success", "message": "Profile data successfully uploaded! It might take sometime to reflect on db"})

    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

@app.route('/get-all-profiles/', methods=['GET'])
def get_all_profiles():
    try:
        # Fetch all profiles from the collection
        all_profiles = list(user_profile_collection.find())

        # Convert ObjectId to str for JSON serialization
        all_profiles = [{**profile, '_id': str(profile['_id'])} for profile in all_profiles]

        return jsonify({'status': 'success', 'profiles': all_profiles})

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})



if __name__ == '__main__':
    app.run(debug=True, port=8000)
