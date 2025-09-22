import numpy as np
from PIL import ImageGrab
import time
import pytesseract
import pyautogui
import pyperclip # never used in current iteration
from PIL import Image
import google.generativeai as genai
import os # never used in current iteration

temp = 0.5 # temperature not implemented [it sucked ass when i tried to change it]

# Screen width for scaling x-coordinates
x = 2560
# Time to wait between actions
wait_time = 7
key = 'AIzaSyC0FGSzkUbgjJ_3Tjqh_WyoawIvM5u63XE'

# Screen height for scaling y-coordinates
y = 1600

def load_words_from_file(filepath="words.txt"):
    """Loads words from a text file into a list."""
    try:
        with open(filepath, 'r') as f:
            words = [line.strip() for line in f if line.strip()]
        return words
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []
    except Exception as e:
        print(f"Error reading words from file: {e}")
        return []

# Load the list of possible words from the words.txt file
possible_words = load_words_from_file()

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

def sendScreenshot(image_path, possible_words_list, prompta):
    """Sends a screenshot to Gemini and gets a response."""
    genai.configure(api_key=key)
    model = genai.GenerativeModel(
        "gemini-1.5-flash"
    )
    

    with open(image_path, "rb") as image_file:
        image_bytes = image_file.read()

    prompt = f"{prompta} Get it right clanker"

    response = model.generate_content(
        [
            {
                "mime_type": "image/jpeg",
                "data": image_bytes
            },
            prompt
        ]
    )
    return response.text

    
def myFunction():
    for i in range(6000):
        pyautogui.scroll(10000)
        screenshot1_path = take_screenshot(int(10 * x / 2560), int(200 * y / 1600), int(1900 * x / 2560), int(2530 * y / 1600), 1)
        text = read_screenshot(screenshot1_path)

        if "Word Theater" in text or "Word Constellation" in text or "Word Ingredient" in text:
            # 'study question'
            pyautogui.typewrite("abcd")
            pyautogui.click(int(1900 * x / 2560), int(323 * y / 1600)) # Next button
            time.sleep(wait_time)
        elif "Spell the word" in text:
            pyautogui.click(int(1263 * x / 2560), int(597 * y / 1600)) # Click on the text box
            pyautogui.typewrite("fffffffffffffffff")
            time.sleep(wait_time)
        elif "image?" in text:
            screenshot2_path = take_screenshot(int(10 * x / 2560), int(200 * y / 1600), int(1520 * x / 2560), int(2530 * y / 1600), 2)
            response2 = sendScreenshot(screenshot2_path, possible_words, "Answer the question by entering a word that makes sense with the hint word and the image, the word will start with the same letter as the letter before the blanks. No spaces or astericks, just the word.") # Pass the loaded list
            print(response2 + "\n\n\n\n\n\n\n\n")
            answer = str(response2)
            newString = answer.lstrip()
            if len(answer) > 1:
                newString = answer[1:]
            pyautogui.typewrite(newString)
            pyautogui.typewrite(answer)
            print("GEMINI RESPONSE: " + newString)
            time.sleep(wait_time)
        elif "Training Expectations" in text:
            pyautogui.click(int(1817 * x / 2560), int(542 * y / 1600))
            pyautogui.click(int(1817 * x / 2560), int(442 * y / 1600))
            time.sleep(3)
            pyautogui.click(int(1316 * x / 2560), int(1130 * y / 1600))
        elif "wordmap" in text:
            screenshot2_path = take_screenshot(int(10 * x / 2560), int(200 * y / 1600), int(1520 * x / 2560), int(2530 * y / 1600), 2)
            response2 = sendScreenshot(screenshot2_path, possible_words, "Answer the question in the format of: A, B, C, or D by using the wordmap of words that are related to the answer word. Since the question is multiple choice, you should answer with ONLY A, B, C, or D") # Pass the loaded list
            print(response2 + "\n\n\n\n\n\n\n\n")
            answer = str(response2)
            newString = answer.lstrip()
            if len(answer) > 1:
                newString = answer[1:]
            pyautogui.typewrite(newString)
            pyautogui.typewrite(answer)
            print("GEMINI RESPONSE WORDMAP: " + newString)
            time.sleep(wait_time)
        elif "BREAK!" in text:
            pyautogui.click(int(1400 * x / 2560), int(868 * y / 1600))
        else:
            screenshot2_path = take_screenshot(int(10 * x / 2560), int(200 * y / 1600), int(1520 * x / 2560), int(2530 * y / 1600), 2)
            response2 = sendScreenshot(screenshot2_path, possible_words, "Answer the question in the format of: A, B, C, or D OR a single word, there should be no spaces or asterisks in your response. If the question is not multiple choice, try to answer by completing the missing word. If the question is multiple choice, answer with only a single letter of the answer") # Pass the loaded list
            print(response2 + "\n\n\n\n\n\n\n\n")
            answer = str(response2)
            newString = answer.lstrip()
            if len(answer) > 1:
                newString = answer[1:]
            pyautogui.typewrite(newString)
            pyautogui.typewrite(answer)
            print("GEMINI RESPONSE: " + newString)
            time.sleep(wait_time)
