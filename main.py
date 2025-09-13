import streamlit as st
import random

st.set_page_config(page_title="MBTI 공부법 추천기 🎓", page_icon="📚", layout="centered")

st.title("📚 MBTI별 공부법 추천 웹사이트 ✨")
st.markdown("당신의 **MBTI**를 선택하면 딱 맞는 공부 방법을 알려드려요! 🚀")

# MBTI 유형 리스트
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 공부법 데이터
study_tips = {
    "INTJ": "📖 계획적으로! 장기 플랜 세우고 목표 달성까지 직진 💡",
    "INTP": "🤯 궁금증을 해결하며! 개념 원리 파고들기 🔍",
    "ENTJ": "🗂️ 목표 달성형! 계획 → 실행 → 피드백 루틴 🔥",
    "ENTP": "💡 토론하며! 친구랑 아이디어 폭발 💬",
    "INFJ": "🌌 몰입 독서! 의미 찾으며 깊게 공부하기 📚",
    "INFP": "🎶 감성 충전! 음악과 함께 따뜻하게 공부 🎧",
    "ENFJ": "🤝 함께 성장! 스터디 그룹에서 리더 역할 🌟",
    "ENFP": "🎨 창의력
