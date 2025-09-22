import google.generativeai as genai
import os

# Replace with your actual API key - securely store it!
key = 'AIzaSyC0FGSzkUbgjJ_3Tjqh_WyoawIvM5u63XE'  # Or use os.environ as explained before

genai.configure(api_key=key)
model = genai.GenerativeModel("gemini-1.5-flash") # or "gemini-pro"


with open("C:/Users/Sachi/OneDrive/Pictures/Camera Roll/john.jpg", "rb") as image_file:
    image_bytes = image_file.read()

response = model.generate_content(
    [
        {
            "mime_type": "image/jpeg",
            "data": image_bytes  # Use 'data' for the image bytes
        },
        "What is shown in this image?"
    ]
)
return response.text
