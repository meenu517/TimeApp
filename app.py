
from gtts import gTTS
import streamlit as st
import pyttsx3
import time
import os
from io import BytesIO




# Initialize text-to-speech engine
# engine = pyttsx3.init()

# Function to speak the time
# def speak_time_gtts():
#     while True:
#         current_time = time.strftime("%I:%M %p")  # Format as "03:15 PM"
#         text = f"The current time is {current_time}"
#         tts = gTTS(text=text, lang='en')
#         tts.save("time.mp3")
#         playsound("time.mp3")
#         time.sleep(1 * 60)  # Wait for 5 minutes

# # Background thread to run the speak_time function
# def start_time_announcement():
#     thread = threading.Thread(target=speak_time_gtts, daemon=True)
#     thread.start()

# Streamlit UI
st.title("Time Announcer")
st.write("This app will speak the current time every 5 minutes.")

if st.button("Start Time Announcements"):
    st.write("Time announcements started!")
    # start_time_announcement()
    current_time = time.strftime("%I:%M %p")  # Format as "03:15 PM"
    text = f"The current time is {current_time}"
    st.write(f"text is {text}")
    # Generate speech from text using gTTS
    tts = gTTS(text)
    
    # Save the audio to a BytesIO object
    audio_buffer = BytesIO()
    tts.write_to_fp(audio_buffer)
    audio_buffer.seek(0)  # Reset buffer to the beginning
    
    # Play the audio in the Streamlit app
    st.audio(audio_buffer, format="audio/mp3")
        
    # # Load audio file
    # audio = AudioSegment.from_file("time.mp3")

    # # Play audio
    # play(audio)
    
    # playsound("time.mp3")
    # # Load the WAV file
    # wave_obj = sa.WaveObject.from_wave_file("time.mp3")
    
    # # Play the audio
    # play_obj = wave_obj.play()
    
    # Wait for playback to finish before exiting
    # play_obj.wait_done()
