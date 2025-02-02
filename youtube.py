import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

# Load environment variables
load_dotenv()  # Load all the environment variables
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """You are a YouTube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here: """

# Function to extract transcript data from YouTube videos
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("=")[1]
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id)

        transcript = ""
        for i in transcript_text:
            transcript += " " + i["text"]

        return transcript

    except Exception as e:
        raise e

# Function to generate summary based on the prompt using Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

# Streamlit UI
st.title("🎥 YouTube Transcript to Detailed Notes Converter")

# Input field for YouTube link
youtube_link = st.text_input("Enter YouTube Video Link:")

# Display video thumbnail
if youtube_link:
    video_id = youtube_link.split("=")[1]
    print(video_id)
    # Display the video thumbnail with the updated parameter
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

# Button to get detailed notes
if st.button("Get Detailed Notes"):
    try:
        # Extract transcript text from YouTube video
        transcript_text = extract_transcript_details(youtube_link)

        if transcript_text:
            # Generate summary using Google Gemini Pro
            summary = generate_gemini_content(transcript_text, prompt)

            # Display the detailed notes
            st.markdown("## Detailed Notes:")
            st.write(summary)
    except Exception as e:
        st.error(f"⚠️ Error: {str(e)}")

