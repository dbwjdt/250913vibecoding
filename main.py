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
    "ENFP": "🎨 창의력 폭발! 색깔펜·마인드맵 활용 🎆",
    "ISTJ": "📑 체크리스트! 하나씩 지워가며 성취감 💯",
    "ISFJ": "🕯️ 조용한 공간에서 안정적으로 공부 🧘",
    "ESTJ": "📊 시간표대로! 규칙적 학습 & 자기 점검 ✅",
    "ESFJ": "👫 친구와 같이! 서로 가르치고 배우기 🤲",
    "ISTP": "🛠️ 실험하며! 손으로 직접 해보고 배우기 🔧",
    "ISFP": "🌿 감각적 몰입! 아늑한 분위기 & 음악 🎶",
    "ESTP": "⚡ 액션형! 문제 풀고 바로바로 피드백 🏃",
    "ESFP": "🎉 즐겁게! 음악·보상·게임화로 재미 UP 🎮"
}

# 선택 UI
selected = st.selectbox("👉 MBTI 유형을 골라보세요!", mbti_types)

if selected:
    st.success(f"✨ 당신의 MBTI는 **{selected}** ✨")
    st.subheader("📌 추천 공부법")
    st.write(study_tips[selected])

    # 랜덤 효과
    effect = random.choice(["balloons", "snow"])
    if effect == "balloons":
        st.balloons()
    else:
        st.snow()

    st.markdown("---")
    st.markdown("💡 **Tip**: MBTI는 참고용일 뿐! 결국 중요한 건 당신의 꾸준함입니다 💪😉")
