import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

api_key = os.getenv("gemini-key")
genai.configure(api_key=api_key)
# Create a model object and generate a response

chat_history = '''
    [9:49 am, 30/10/2024] Akshit: Mujhe nhi pta ye saab tere saath hi seekh ra 🤡🤡🤡
    [5:13 pm, 30/10/2024] Uday: Prk???
    [5:13 pm, 30/10/2024] Uday: At 5.30
    [5:41 pm, 30/10/2024] Akshit: 😪😪😪
    [5:44 pm, 30/10/2024] Uday: Chlna h ki nii???
    [5:48 pm, 30/10/2024] Akshit: Ummm yrrr
    [5:48 pm, 30/10/2024] Uday: Aau ???
    [5:48 pm, 30/10/2024] Uday: Ki Naa???
    [5:53 pm, 30/10/2024] Akshit: Rehn de
    [5:53 pm, 30/10/2024] Akshit: Thoda late ho gya
    [5:53 pm, 30/10/2024] Uday: Soraa tha na tu
    [5:59 pm, 30/10/2024] Akshit: Yepp
'''
prompt = (
    "You are Akshit, a 20-year-old engineering student from Gurugram, specializing in Information Technology. Respond to questions in a friendly and concise manner, using Hinglish or English. Keep your responses short and relatable, reflecting a young person's perspective."
    "also no need to introduce your self in response"
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