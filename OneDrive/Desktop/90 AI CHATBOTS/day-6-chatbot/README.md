# 🤖 AI Chatbot Pro

**Developed by: Murthu**

![Status](https://img.shields.io/badge/Status-Live-brightgreen?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20UI-red?style=for-the-badge)
![Groq](https://img.shields.io/badge/AI-Groq%20API-orange?style=for-the-badge)

---

## 🚀 Features

✨ **5 AI Personalities** - Mentor, Comedian, Strict Teacher, Zen Master, Enthusiast

💬 **Real-time Conversation** - ChatGPT-style interface

📊 **Live Analytics** - Sentiment analysis + keyword tracking

📥 **Export to JSON** - Download chat history anytime

🌐 **Deploy Free** - Streamlit Cloud (1-click deployment)

---

## 🎯 Tech Stack

**Frontend:** Streamlit (Python Web UI)

**Backend:** Groq API (Lightning-fast LLMs)

**Analytics:** Sentiment detection + keyword extraction

**Deployment:** Streamlit Cloud (Free forever)

---

## 📱 How to Use

### Local Development

```bash
python -m venv venv
venv\Scripts\activate
pip install streamlit groq python-dotenv
streamlit run app.py
```

Browser automatically opens at `http://localhost:8501`

### Deploy to Cloud (FREE)

1. Push code to GitHub
2. Visit streamlit.io/cloud
3. Connect GitHub repository
4. Select day-6-chatbot/app.py
5. Deploy (takes 2 minutes!)

Your app URL: `https://yourname-chatbot.streamlit.app`

---

## 🎭 Available Personalities

| Personality | Emoji | Description |
|-------------|-------|-------------|
| Mentor | 🎓 | Patient, encouraging, teaching-focused |
| Comedian | 🤣 | Witty, funny, entertainment-driven |
| Strict Teacher | 👨‍🏫 | Direct, no-nonsense, demanding |
| Zen Master | 🧘 | Philosophical, wise, big-picture |
| Enthusiast | 🤩 | Hyped, emoji-filled, positive |

---

## 📊 Analytics Dashboard

**Real-time Tracking:**

- Message count & conversation length
- Sentiment breakdown (positive/negative/neutral)
- Top keywords with frequency
- Beautiful bar charts & metrics
- JSON export with full analysis

---

## 💾 Export Options

Download complete chat sessions in JSON format:

```json
{
  "developer": "Murthu",
  "personality": "mentor",
  "message_count": 25,
  "sentiment": {
    "positive": 10,
    "negative": 2,
    "neutral": 13
  },
  "top_keywords": [
    {"word": "python", "frequency": 5},
    {"word": "code", "frequency": 4}
  ],
  "conversation": [...]
}
```

---

## 🔧 Customization

Modify `app.py` to add new personalities:

```python
personalities = {
    "your_name": "Your custom system prompt here...",
}
```

---

## 📈 Part of 90-Day AI Challenge

**Day 6 of 90** - Building professional AI applications

Progress: 6/90 Days Complete ✅

---

## 👤 About

**Developer:** Murthu (Pinjari Murthujavali)

**GitHub:** [@PinjariMurthujavali](https://github.com/PinjariMurthujavali)

**Challenge:** 90 Days of AI + Full Stack + Automation

---

## 🌟 Key Learning Points

- Streamlit for professional web UIs
- Session state management
- Real-time analytics
- Free cloud deployment
- JSON data handling
- Sentiment analysis basics

---

*Built with ❤️ | Powered by Groq API | Free & Open Source*
