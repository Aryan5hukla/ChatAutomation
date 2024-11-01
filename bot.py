import pyautogui
import time
import pyperclip
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("gemini-key")
genai.configure(api_key=api_key)


# def is_last_message_from_sender(chat_log, sender_name="Vaibhav"):
#     # Split the chat log into individual messages
#     messages = chat_log.strip().split("/2024] ")[-1]
#     if sender_name in messages:
#         return True 
#     return False


def is_last_message_from_sender(chat_log, sender_name="Yadav Nikhil"):
    # Split the chat log by each message entry
    messages = chat_log.strip().split("\n")
    # Check if the last non-empty message contains the sender's name
    last_message = messages[-1].strip() if messages else ""
    return sender_name in last_message


# pyautogui.click
# Step 1: Click on the chrome icon at coordinates (1096, 1047)
pyautogui.moveTo(1097 , 1080)
time.sleep(1) 
pyautogui.click(1097 , 1045)


 # Wait for 1 second to ensure the click is registered

while True :
    
    time.sleep(3)
    # Step 2: Drag the mouse from (1003, 237) to (2187, 1258) to select the text
    pyautogui.moveTo(758 , 278)
    pyautogui.dragTo(1104 , 1010, duration=2.0, button='left')  # Drag for 1 second

    # Step 3: Copy the selected text to the clipboard
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(2)  # Wait for 1 second to ensure the copy command is completed

    pyautogui.click(1568 , 932)

    # Step 4: Retrieve the text from the clipboard and store it in a variable
    chat_history = pyperclip.paste()

    print(chat_history)

    print(is_last_message_from_sender(chat_history))



    if is_last_message_from_sender(chat_history):
        last_sender_message = chat_history.split("\n")[-1].split("] ")[-1]  # Extract only the last message text
    
        prompt = (
        "You are Akshit, a 20-year-old engineering student from Gurugram. Reply naturally to the sender’s last message. Use Hinglish or Hindi for a friendly tone. Keep it short, and avoid unnecessary coding talk unless relevant. Only reply to the single last message and paraphrase."

        )
        try:
    
            model = genai.GenerativeModel("gemini-1.5-flash")
            full_prompt = f"{prompt} {chat_history}"
            response = model.generate_content(full_prompt)
            response_text = response.text.strip().split('\n')
            short_response = '\n'.join(response_text[:4])

            print(short_response)
        except Exception as e:
            print("An error occurred:", e)

        pyperclip.copy(short_response)


        # Step 5: Click at coordinates (1808, 1328)
        pyautogui.click(1042, 1021)
        time.sleep(3)  # Wait for 1 second to ensure the click is registered

        # Step 6: Paste the text
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)  # Wait for 1 second to ensure the paste command is complete
        # Step 7: Press Enter
        pyautogui.press('enter')
