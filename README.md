# Snapchat Profile Scraper

A Python application for scraping and storing Snapchat profile data.

## Overview

This application utilizes Selenium and MongoDB to scrape and store Snapchat profile data. It includes a Flask server to handle requests for scraping profiles and fetching stored data.

## Features

- Scrapes Snapchat profile data using Selenium.
- Stores the scraped data in MongoDB.
- Provides an API endpoint for scraping profiles in the background.
- Fetches and displays stored profiles.

## Prerequisites

- Python 3.x
- Flask
- MongoDB


## Setup

Follow the steps below to set up and run the Snapchat Profile Scraper:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yabesh12/snapchat-scraper.git
   ```

2. **Navigate to the Project Directory:**

   ```bash
   cd snapchat-profile-scraper
   ```

3. **Create a Virtual Environment:**

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**

   - On Windows:

     ```bash
     .\venv\Scripts\activate
     ```

   - On Unix or MacOS:

     ```bash
     source venv/bin/activate
     ```

5. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```


6. **Run the Flask Application:**

   ```bash
   python app.py
   ```


## Usage (API-Endpoints)

### Scraping a Profile

To scrape a Snapchat profile, make a POST request to:

```
http://localhost:8000/scrape-user-profile/
```

Include the profile URL in the request body:

```json
{
  "profile_url": "https://www.snapchat.com/add/username"
}
```

### Fetching All Profiles

To fetch all stored profiles, make a GET request to:

```
http://localhost:8000/get-all-profiles/
```