import pdfplumber
import pytesseract
from PIL import Image
import re
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
STOPWORDS = set(stopwords.words('english'))

def extract_text_from_txt(file):
    return file.read().decode('utf-8')

def extract_text_from_pdf(file):
    text = ''
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ''
    return text

def extract_text_from_image(file):
    image = Image.open(file)
    return pytesseract.image_to_string(image)

def clean_text(text):
    text = re.sub(r'[^a-zA-Z ]', '', text)
    text = text.lower()
    words = [w for w in text.split() if w not in STOPWORDS]
    return ' '.join(words)

def extract_and_clean_resume(file):
    if file.name.endswith('.txt'):
        text = extract_text_from_txt(file)
    elif file.name.endswith('.pdf'):
        text = extract_text_from_pdf(file)
    elif file.name.endswith(('.png', '.jpg', '.jpeg')):
        text = extract_text_from_image(file)
    else:
        return ''
    return clean_text(text)
