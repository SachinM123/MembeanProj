import numpy as np
from PIL import ImageGrab
import time
import random
import pytesseract
import pyautogui
import pyperclip
from PIL import Image
from google import genai
from google.genai import types
import os
import re

temp = 0.5

# Screen width for scaling x-coordinates (YOU NEED TO CHANGE THIS BASED ON YOUR SCREEN RESOLUTION)
x = 2560
# Time to wait between actions
wait_time = 5
AIModel = "gemini-3-flash-preview"

y = 1600
# Screen height for scaling y-coordinates (YOU NEED TO CHANGE THIS BASED ON YOUR SCREEN RESOLUTION)
key = 'AIzaSyCXRG2eXfTzvzSYlBX3cgr3fY1j-mf3-7s'

# Configure the Gemini API
client = genai.Client(api_key=key)

def read_screenshot(screenshot_path):
    """Reads text from an image using OCR."""
    try:
        img = Image.open(screenshot_path)
        text = pytesseract.image_to_string(img)
        print(f"OCR Text: {text}")
        return text
    except FileNotFoundError:
        print(f"Error: Screenshot file not found at {screenshot_path}")
        return ""
    except Exception as e:
        print(f"Error during OCR: {e}")
        return ""

def take_screenshot(left, upper, right, lower, num):
    """Takes a screenshot of a specific region and saves it."""
    sNum = str(num)
    screenshot = ImageGrab.grab(bbox=(left, upper, right, lower))
    screenshot_path = f'screenshot{sNum}.png'
    screenshot.save(screenshot_path)
    return screenshot_path

def sendScreenshot(image_path, prompta):
    """Sends a screenshot to Gemini and gets a response."""
    # Read image file
    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()

    # Prepare the prompt
    prompt = f"{prompta} Get it right clanker"

    # Generate content with image and text using the correct API format
    response = client.models.generate_content(
        model=AIModel,
        contents=[
            prompt,
            types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg")
        ]
    )
    return response.text

def get_answer_from_response(text: str, marker: str = "My answer is:") -> str:
    """Extracts and returns the answer following the given marker in `text`.

    Behavior:
    - Case-insensitive search for `marker`.
    - Returns the first line after the marker, trimmed of surrounding whitespace and quotes.
    - If the marker isn't found, returns an empty string.

    Examples:
    >>> get_answer_from_response("My answer is: cat")
    'cat'
    >>> get_answer_from_response("something\nMy answer is: \"dog\"\nmore")
    'dog'
    >>> get_answer_from_response("No answer here")
    ''
    """
    if not text:
        return ""

    lower = text.lower()
    marker_lower = marker.lower()
    idx = lower.find(marker_lower)
    if idx == -1:
        return ""

    # Get substring after the marker
    start = idx + len(marker_lower)
    remainder = text[start:]

    # Take only the first line (answers are typically single-line)
    first_line = remainder.splitlines()[0] if remainder.splitlines() else remainder

    # Trim whitespace and surrounding quotes
    ans = first_line.strip()
    # Remove wrapping quotes if present
    if (ans.startswith('"') and ans.endswith('"')) or (ans.startswith("'") and ans.endswith("'")):
        ans = ans[1:-1].strip()

    # Remove trailing punctuation that is unlikely part of the answer
    ans = ans.rstrip(' .,!?:;')

    return ans

    
def myFunction():
    for i in range(6000):
        pyautogui.scroll(10000)
        screenshot1_path = take_screenshot(int(10 * x / 2560), int(200 * y / 1600), int(1900 * x / 2560), int(2530 * y / 1600), 1)
        text = read_screenshot(screenshot1_path)

        if "Word Theater" in text or "Word Constellation" in text or "Word Ingredient" in text:
            # 'study question'
            if(random.randint(1,2) == 2):
                pyautogui.hotkey('ctrl','r')
            time.sleep(5)
            pyautogui.typewrite("abcd")
            pyautogui.click(int(1900 * x / 2560), int(323 * y / 1600)) # Next button
            time.sleep(wait_time + random.uniform(1,2))
        elif "Spell the word" in text:
            pyautogui.click(int(1263 * x / 2560), int(597 * y / 1600)) # Click on the text box
            pyautogui.typewrite("fffffffffffffffff")
            time.sleep(wait_time + random.uniform(1,2))
        elif "image?" in text:
            screenshot2_path = take_screenshot(int(10 * x / 2560), int(200 * y / 1600), int(1520 * x / 2560), int(2530 * y / 1600), 2)
            response2 = sendScreenshot(screenshot2_path, "Answer the question by entering a word that makes sense with the hint word and the image, the word will start with the same letter as the letter before the blanks. Format your final answer as: My answer is: <answer>'") # Pass the loaded list
            print(response2 + "\n\n\n\n\n\n\n\n")
            answer = str(response2)
            answer = get_answer_from_response(answer)
            newString = answer.lstrip()
            if len(answer) > 1:
                newString = answer[1:]
            pyautogui.typewrite(newString)
            pyautogui.typewrite(answer)
            print("GEMINI RESPONSE: " + newString)
            time.sleep(wait_time + random.uniform(1,2))
        elif "Training Expectations" in text:
            pyautogui.click(int(1817 * x / 2560), int(542 * y / 1600))
            pyautogui.click(int(1817 * x / 2560), int(442 * y / 1600))
            time.sleep(3)
            pyautogui.click(int(1316 * x / 2560), int(645 * y / 1600))
        elif "wordmap" in text:
            screenshot2_path = take_screenshot(int(10 * x / 2560), int(200 * y / 1600), int(1520 * x / 2560), int(2530 * y / 1600), 2)
            response2 = sendScreenshot(screenshot2_path, "Answer the question in the format of: A, B, C, or D by using the wordmap of words that are related to the answer word. Format your final answer as: 'My answer is: <answer>'") # Pass the loaded list
            print(response2 + "\n\n\n\n\n\n\n\n")
            answer = str(response2)
            answer = get_answer_from_response(answer)
            newString = answer.lstrip()
            if len(answer) > 1:
                newString = answer[1:]
            pyautogui.typewrite(newString)
            pyautogui.typewrite(answer)
            print("GEMINI RESPONSE WORDMAP: " + newString)
            time.sleep(wait_time + random.uniform(1,2))
        elif "BREAK!" in text:
            pyautogui.click(int(1400 * x / 2560), int(868 * y / 1600))
        else:
            screenshot2_path = take_screenshot(int(10 * x / 2560), int(200 * y / 1600), int(1520 * x / 2560), int(2530 * y / 1600), 2)
            response2 = sendScreenshot(screenshot2_path, "Answer the question in the format of: A, B, C, or D OR a single word. If the question is not multiple choice, try to answer by completing the missing word. If the question is multiple choice, answer with only a single letter of the answer. Format your final answer as: 'My answer is: <answer>'") # Pass the loaded list
            print(response2 + "\n\n\n\n\n\n\n\n")
            answer = str(response2)
            answer = get_answer_from_response(answer)
            newString = answer.lstrip()
            if len(answer) > 1:
                newString = answer[1:]
            pyautogui.typewrite(newString)
            pyautogui.typewrite(answer)
            print("GEMINI RESPONSE: " + newString)
            time.sleep(wait_time + random.uniform(1,2))


