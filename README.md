# RESUME_SCREENER

A Python project using Streamlit, NLTK, regex, and pickle to screen resumes and predict the best domain.

## Features
- Upload resumes (txt, pdf, image)
- Extract and clean text using regex and NLP
- Remove stopwords (NLTK)
- Vectorize resumes
- Train/test ML model (pickle for persistence)
- Predict best domain for resume

## Setup
1. Install dependencies:
   - streamlit
   - nltk
   - scikit-learn
   - pdfplumber
   - pytesseract
   - Pillow
2. Run Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Folder Structure
- app.py: Streamlit frontend
- resume_processing.py: Text extraction & cleaning
- model.py: Training, vectorization, prediction
- requirements.txt: Dependencies

## Notes
- Placeholders for model and domain list; update as needed.
- OCR requires Tesseract installed for image extraction.
