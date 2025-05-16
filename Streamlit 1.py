import streamlit as st
from PIL import Image

# FILE UPLOADING
st.title('File Uploading')

#1. IMAGE
IMG_file = st.file_uploader("UPLOAD IMAGE", type=["jpg", "png", "jpeg"])
if IMG_file is not None:
    img = Image.open(IMG_file)
    st.image(img, caption='Uploaded Image', use_container_width=True)
    file_details = {"filename": IMG_file.name, "filetype": IMG_file.type, "filesize": IMG_file.size}
    st.write(file_details)

#2. Audio
Audio_file = st.file_uploader("UPLOAD Audio", type=["mp3", "wav"])
if Audio_file is not None:
    audio_bytes = Audio_file.read()
    st.audio(audio_bytes, format='audio/mp3')
    file_details = {"filename": Audio_file.name, "filetype": Audio_file.type, "filesize": Audio_file.size}
    st.write(file_details)

#3. Video
Video_file = st.file_uploader("UPLOAD Video", type=["mp4", "mov", "avi"])
if Video_file is not None:
    video_bytes = Video_file.read()
    st.video(video_bytes)
    file_details = {"filename": Video_file.name, "filetype": Video_file.type, "filesize": Video_file.size}
    st.write(file_details)