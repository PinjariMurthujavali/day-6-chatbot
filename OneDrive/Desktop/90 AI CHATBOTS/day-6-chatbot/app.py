# ============================================
# Day 6: Web UI with Streamlit
# Developed by: MURTHU 🚀
# ============================================

import os
from dotenv import load_dotenv
from groq import Groq
from datetime import datetime
import streamlit as st
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(script_dir, ".env"))
api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None


# PERSONALITIES
personalities = {
    "mentor": "You are a friendly, motivating coding mentor who explains things simply and encourages the user like a supportive friend.",
    "comedian": "You are a witty, funny comedian who makes jokes and uses humor while still being helpful. Keep responses light and entertaining.",
    "strict_teacher": "You are a strict but fair teacher who doesn't tolerate nonsense. Be direct, no-nonsense, and demand excellence.",
    "zen_master": "You are a calm, wise zen master who speaks in philosophical terms and uses metaphors.",
    "enthusiast": "You are an overly enthusiastic tech enthusiast who gets excited about everything! Use lots of emojis and exclamation marks.",
}


# PAGE CONFIG
st.set_page_config(
    page_title="🤖 AI Chatbot Pro by Murthu",
    page_icon="🤖",
    layout="wide",
)

st.markdown("""
    <style>
    .main { background-color: #0f1419; color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

if client is None:
    st.sidebar.error(
        "Missing GROQ_API_KEY. Create a `.env` file with `GROQ_API_KEY=your_api_key_here` "
        "or configure the environment variable before running this app."
    )


# SIDEBAR
st.sidebar.title("⚙️ Settings")
selected_personality = st.sidebar.selectbox(
    "Choose AI Personality:",
    list(personalities.keys()),
    index=0
)


# MAIN PAGE
st.title("🤖 AI Chatbot Pro")
st.markdown(f"**Powered by Groq • Developed by: Murthu 🚀 • Personality: {selected_personality.upper()}**")

col1, col2, col3 = st.columns(3)
with col1:
    st.metric("📊 Messages", st.session_state.get("message_count", 0))
with col2:
    st.metric("😊 Sentiment", st.session_state.get("overall_sentiment", "Neutral"))
with col3:
    st.metric("🔑 Keywords", st.session_state.get("keyword_count", 0))


# SESSION STATE
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = [
        {"role": "system", "content": personalities[selected_personality]}
    ]

if "message_count" not in st.session_state:
    st.session_state.message_count = 0

if "sentiment_scores" not in st.session_state:
    st.session_state.sentiment_scores = {"positive": 0, "negative": 0, "neutral": 0}

if "keywords" not in st.session_state:
    st.session_state.keywords = {}


# FUNCTIONS
def analyze_sentiment(text):
    positive_words = ["good", "great", "amazing", "awesome", "excellent", "love", "best", "perfect", "brilliant"]
    negative_words = ["bad", "terrible", "awful", "hate", "worst", "poor", "useless", "stupid", "wrong"]
    
    text_lower = text.lower()
    pos_count = sum(1 for word in positive_words if word in text_lower)
    neg_count = sum(1 for word in negative_words if word in text_lower)
    
    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    else:
        return "neutral"


def get_keywords(text):
    stop_words = {"the", "a", "is", "it", "to", "and", "or", "in", "on", "at", "for", "of", "with"}
    words = text.lower().split()
    keywords = [w.strip(".,!?;:") for w in words if w.strip(".,!?;:") not in stop_words and len(w) > 2]
    return keywords


# CHAT DISPLAY
st.markdown("---")
st.subheader("💬 Conversation")
chat_container = st.container()


# CHAT INPUT
user_input = st.chat_input("Type your message here...")

if user_input:
    if client is None:
        st.error(
            "Unable to send your message because GROQ_API_KEY is missing. "
            "Please add it to a `.env` file or configure the environment variable."
        )
    else:
        st.session_state.conversation_history.append({"role": "user", "content": user_input})
        st.session_state.message_count += 1
        
        user_sentiment = analyze_sentiment(user_input)
        st.session_state.sentiment_scores[user_sentiment] += 1
        
        user_keywords = get_keywords(user_input)
        for keyword in user_keywords:
            st.session_state.keywords[keyword] = st.session_state.keywords.get(keyword, 0) + 1
        
        with st.spinner("🤖 Murthu's AI thinking..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=st.session_state.conversation_history
            )
        
        ai_reply = response.choices[0].message.content
        st.session_state.conversation_history.append({"role": "assistant", "content": ai_reply})
        
        ai_sentiment = analyze_sentiment(ai_reply)
        st.session_state.sentiment_scores[ai_sentiment] += 1
        
        ai_keywords = get_keywords(ai_reply)
        for keyword in ai_keywords:
            st.session_state.keywords[keyword] = st.session_state.keywords.get(keyword, 0) + 1


# DISPLAY CONVERSATION
with chat_container:
    for message in st.session_state.conversation_history:
        if message["role"] == "system":
            continue
        
        if message["role"] == "user":
            st.chat_message("user").write(message["content"])
        else:
            st.chat_message("assistant").write(message["content"])


# SIDEBAR ANALYTICS
st.sidebar.markdown("---")
st.sidebar.subheader("📊 Analytics")

if st.session_state.message_count > 0:
    st.sidebar.metric("Total Messages", st.session_state.message_count)
    
    sentiment_data = st.session_state.sentiment_scores
    st.sidebar.write("**Sentiment Distribution:**")
    st.sidebar.bar_chart(sentiment_data)
    
    st.sidebar.write("**Top Keywords:**")
    if st.session_state.keywords:
        top_keywords = sorted(st.session_state.keywords.items(), key=lambda x: x[1], reverse=True)[:5]
        for keyword, count in top_keywords:
            st.sidebar.write(f"🔹 {keyword}: {count}")


# EXPORT
st.sidebar.markdown("---")
st.sidebar.subheader("💾 Export & Deploy")

if st.sidebar.button("📥 Export Chat as JSON"):
    export_data = {
        "developer": "Murthu",
        "personality": selected_personality,
        "timestamp": datetime.now().isoformat(),
        "message_count": st.session_state.message_count,
        "sentiment": st.session_state.sentiment_scores,
        "top_keywords": sorted(st.session_state.keywords.items(), key=lambda x: x[1], reverse=True)[:10],
        "conversation": [m for m in st.session_state.conversation_history if m["role"] != "system"]
    }
    
    json_str = json.dumps(export_data, indent=2)
    st.sidebar.download_button(
        label="📥 Download JSON",
        data=json_str,
        file_name=f"chat_{selected_personality}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.json",
        mime="application/json"
    )


# DEPLOYMENT INFO
with st.sidebar.expander("🚀 How to Deploy (FREE)", expanded=False):
    st.markdown("""
    **Free Deployment Options:**
    
    1️⃣ **Streamlit Cloud (Easiest)**
    - Push code to GitHub
    - Visit: streamlit.io/cloud
    - Connect GitHub → Deploy
    - Free forever! ✅
    
    2️⃣ **Heroku**
    - Free tier available
    - Easy integration
    
    3️⃣ **Render**
    - Free deployment
    - No credit card needed
    
    **Your App URL will be:**
    `https://yourname-chatbot.streamlit.app`
    
    Share link anywhere! 🌐
    """)


# CLEAR CHAT
if st.sidebar.button("🗑️ Clear Chat"):
    st.session_state.conversation_history = [
        {"role": "system", "content": personalities[selected_personality]}
    ]
    st.session_state.message_count = 0
    st.session_state.sentiment_scores = {"positive": 0, "negative": 0, "neutral": 0}
    st.session_state.keywords = {}
    st.rerun()


# FOOTER
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray; font-size: 12px;'>
    🚀 Day 6: Web UI with Streamlit • Developed by Murthu • Part of 90-Day AI Challenge
    <br>
    Deploy Free on Streamlit Cloud | GitHub: PinjariMurthujavali
    </div>
    """, unsafe_allow_html=True)