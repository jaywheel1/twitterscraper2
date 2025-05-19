import streamlit as st
import snscrape.modules.twitter as sntwitter

st.title("Twitter Profile Scraper")

username = st.text_input("Twitter handle (no @):")
max_tweets = st.slider("Max tweets to fetch:", 1, 500, 100)

if st.button("Fetch"):
    if not username:
        st.error("Enter a handle first.")
    else:
        tweets = []
        for i, tweet in enumerate(
                sntwitter.TwitterUserScraper(username).get_items()):
            if i >= max_tweets:
                break
            tweets.append({
                "Date": tweet.date,
                "Content": tweet.content,
                "Likes": tweet.likeCount,
                "Retweets": tweet.retweetCount
            })
        if tweets:
            st.success(f"Fetched {len(tweets)} tweets")
            st.table(tweets)
        else:
            st.warning("No tweets found.")
