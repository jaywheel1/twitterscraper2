import streamlit as st
import requests
import feedparser
import pandas as pd

st.set_page_config(page_title="Twitter/X Profile Scraper")

st.title("Twitter/X Profile Scraper")
st.write("Enter a Twitter handle or profile URL to scrape recent tweets via Nitter RSS feed.")

# 1. Get raw input and normalize to handle only
raw_input = st.text_input("Twitter handle or profile URL:")
if raw_input:
    username = raw_input.strip().rstrip("/").split("/")[-1]
else:
    username = ""

# 2. Select how many tweets to fetch
max_tweets = st.slider(
    label="Number of tweets to scrape:",
    min_value=1,
    max_value=100,
    value=25
)

# 3. On button click, fetch and display
if st.button("Scrape Tweets"):
    if not username:
        st.error("Enter a valid handle or URL.")
    else:
        # Build Nitter RSS URL
        rss_url = f"https://nitter.net/{username}/rss"
        try:
            resp = requests.get(rss_url, timeout=10)
            feed = feedparser.parse(resp.text)
        except Exception as e:
            st.error(f"Failed to fetch RSS: {e}")
        else:
            if not feed.entries:
                st.error("No tweets found. Check the handle or try a different Nitter instance.")
            else:
                # Collect entries up to max_tweets
                rows
