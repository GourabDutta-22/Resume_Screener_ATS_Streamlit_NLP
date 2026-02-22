import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Placeholder domains

# Expanded domains
DOMAINS = [
    'AIML', 'ML Engineer', 'Cyber Security', 'Java Developer', 'Full Stack Developer',
    'MERN Stack Developer', 'Backend Developer', 'Frontend Developer', 'Data Scientist', 'Data Analyst'
]

# Example keywords for each domain (should be expanded for production)
DOMAIN_KEYWORDS = {
    'AIML': ['machine learning', 'deep learning', 'neural network', 'ai', 'nlp', 'tensorflow', 'pytorch'],
    'ML Engineer': ['machine learning', 'model deployment', 'feature engineering', 'scikit-learn', 'pipeline'],
    'Cyber Security': ['security', 'penetration testing', 'vulnerability', 'firewall', 'encryption', 'malware'],
    'Java Developer': ['java', 'spring', 'hibernate', 'j2ee', 'maven', 'servlet'],
    'Full Stack Developer': ['frontend', 'backend', 'api', 'database', 'react', 'node', 'express', 'html', 'css', 'javascript'],
    'MERN Stack Developer': ['mongodb', 'express', 'react', 'node', 'mern'],
    'Backend Developer': ['api', 'database', 'server', 'django', 'flask', 'node', 'express'],
    'Frontend Developer': ['html', 'css', 'javascript', 'react', 'angular', 'vue', 'ui', 'ux'],
    'Data Scientist': ['data analysis', 'statistics', 'python', 'machine learning', 'pandas', 'numpy', 'visualization'],
    'Data Analyst': ['excel', 'sql', 'data analysis', 'reporting', 'visualization', 'tableau', 'powerbi']
}

# Load or train model
try:
    with open('model.pkl', 'rb') as f:
        model, vectorizer = pickle.load(f)
except:
    # Dummy training for placeholder
    sample_texts = [
        'python machine learning data analysis',
        'java software development coding',
        'marketing sales branding',
        'finance accounting investment',
        'hr recruitment management'
    ]
    sample_labels = [0, 1, 2, 3, 4]
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(sample_texts)
    model = LogisticRegression()
    model.fit(X, sample_labels)
    with open('model.pkl', 'wb') as f:
        pickle.dump((model, vectorizer), f)


def predict_domain(resume_text):
    X = vectorizer.transform([resume_text])
    pred = model.predict(X)[0]
    return DOMAINS[pred]

def ats_score(resume_text, domain):
    """
    Calculate ATS score based on keyword match for the predicted domain.
    Returns a score between 0 and 100.
    """
    keywords = DOMAIN_KEYWORDS.get(domain, [])
    if not keywords:
        return 0
    resume_text_lower = resume_text.lower()
    matches = sum(1 for kw in keywords if kw in resume_text_lower)
    return int((matches / len(keywords)) * 100) if keywords else 0
