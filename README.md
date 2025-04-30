# KeshavBot - AI Smart Bot with Gemini Pro

KeshavBot is a simple and interactive Streamlit web app powered by Google's Gemini Pro language model. It allows users to ask questions and receive intelligent, generative responses in real time.

## Features

- Built using **Streamlit** for UI
- Uses **Google Generative AI (Gemini Pro)**
- Loads API key securely via **dotenv**
- Clean and user-friendly interface
- Lightweight and easy to deploy

## Installation

1. **Clone the repository:**

```bash
git clone
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
pip install -r requirements.txt
GOOGLE_API_KEY=your_google_api_key_here
streamlit run app.py
keshavbot/
├── app.py
├── .env
├── requirements.txt
└── README.md
