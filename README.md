# 🌤️ Mood Journal Analyzer

Ever wonder whether your daily thoughts skew positive or negative?
This app lets you log mood sentences in Chinese or English,
instantly translates them, and tells you the emotional tone —
positive, negative, or neutral — with a confidence score.

Built with Azure Translator and Azure AI Language, deployed on Azure Web App.

🔗 **Try it live**: https://yolanda-sentiment-app.azurewebsites.net

---

## Features
- 📝 Write mood entries in Chinese or English
- 🔄 Auto-detects language and translates Chinese ↔ English
- 💡 Analyzes sentiment: Positive / Negative / Neutral
- 📊 Shows confidence scores for emotional tone
- ☁️ Deployed on Azure Web App — accessible from anywhere

## Who Is This For?
- Language learners who journal in both Chinese and English
- Anyone curious about the emotional patterns in their daily thoughts
- Developers exploring Azure AI services for NLP projects

## Tech Stack
| Layer | Technology |
|---|---|
| Backend | Python + Flask |
| Translation | Azure Translator API |
| Sentiment Analysis | Azure AI Language |
| Deployment | Azure Web App (Free Tier) |

## How to Run Locally
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Set environment variables:
   - `TRANSLATOR_KEY` = your Azure Translator key
   - `LANGUAGE_KEY` = your Azure AI Language key
4. Run: `python app.py`
5. Open `http://localhost:5000`
