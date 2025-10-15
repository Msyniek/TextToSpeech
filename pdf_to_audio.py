import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename
import re
import os

script_dir = os.path.dirname(os.path.abspath(__file__))

book = askopenfilename()
reader = PdfReader(book)
pages = len(reader.pages)
engine = pyttsx3.init()

voices = engine.getProperty('voices')
print("Available voices/languages:")
for idx, v in enumerate(voices):
    print(f"{idx}: Name: {v.name}, Lang: {v.languages}, ID: {v.id}")

voice_index = int(input("Enter the number of the voice/language you want to use: "))
engine.setProperty('voice', voices[voice_index].id)

output_file = os.path.join(script_dir, input("Enter the output audio file name (e.g., audio.wav / audio.mp3): "))

full_text = ""
for i in range(pages):
     page = reader.pages[i]
     page_text = page.extract_text()
     if page_text:
         full_text += page_text + "\n"

full_text = re.sub(r'(?<!\n)\n(?!\n)', ' ', full_text)

engine.save_to_file(full_text, output_file)
engine.runAndWait()
print(f"Audio saved at {output_file}")