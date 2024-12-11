import streamlit as st
from streamlit_carousel import carousel
import google.generativeai as genai
from openai import OpenAI
import os
from dotenv import load_dotenv, find_dotenv

'''
load_dotenv(find_dotenv())
open_ai_key = os.getenv("open_ai_key")
google_gemini_api_key = os.getenv("google_gemini_api_key")
client = OpenAI(api_key=open_ai_key)
genai.configure(api_key=google_gemini_api_key)
'''



single_image= dict(
        title="",
        text="",
        interval=None,
        img="",
    )
    
'''
# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

 

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  system_instruction="Generate a comprehensive, engaging blog post relevant to the given title “Effects of Generative AI” and keywords “Artificial Creativity, Ethical Implications, Technology Innovation, Machine Learning Applications, AI Impact on Society”. Make sure to incorporate these keywords in the blog post. The blog should be approximately 500 words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout.",
)
'''

st.set_page_config(layout='wide')


# title of app
st.title('BlogBuilder: AI Blog Writing Assistant')

# create subheader
st.subheader("Here to help you curate the greatest blog posts!")

# sidebar for user input
with st.sidebar:
    st.title("Input Blog Details")
    st.subheader("Enter your blog details for the blog you'd like to generate.")

    # blog title
    blog_title=st.text_input("Blog Title")

    # keywords input
    keywords = st.text_area("What are some keywords that describe your blog post (comma-separated).")

    # number of words
    num_words = st.slider("How many words would you like in your blog post?", min_value=100, max_value=2000, step=100)

    # number of images
    num_images = st.number_input("How many images would you like in your blog post?", min_value=1, max_value=5, step=1)

    prompt_parts = [
        f"Generate a comprehensive, engaging blog post relevant to the given title {blog_title} and keywords {keywords} Make sure to incorporate these keywords in the blog post. The blog should be approximately {num_words} words in length, suitable for an online audience. Ensure the content is original, informative, and maintains a consistent tone throughout.",
    ]



    # Submit Button
    submit_button = st.button("Create Blog Post")

if submit_button:
   
    text_response = model.generate_content(prompt_parts)
   # Create a gallery of images with titles and text
images = []
image_gallery = []

for i in range(num_images):
    image_response = client.images.generate(
        model="dall-e-3",
        prompt=f"Generate a Blog Post Image on the title: {blog_title}",
        size="1024x1024",
        quality="standard",
        n=1,
    )
    new_image = single_image.copy()
    new_image["title"] = f"Image {i+1}"
    new_image["text"] = blog_title
    new_image["img"] = image_response.data[0].url
    images.append(new_image)  # Add the complete dictionary to the list

# Use the images list for the carousel
carousel(items=images, width=1)

# Display the blog post
st.title("YOUR BLOG POST")
st.write(text_response.text)
