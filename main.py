# streamlit_app.py
import streamlit as st
import pandas as pd
import altair as alt
import os

st.set_page_config(page_title="MBTI 국가 Top10 대시보드", layout="wide")

st.title("🌍 MBTI 유형별 국가 분포 Top10 대시보드")
st.caption("같은 폴더의 CSV 파일을 기본으로 읽고, 없을 경우 업로드한 파일을 사용합니다.")

# ---------------------------
# 1) 데이터 불러오기
# ---------------------------
default_path = "countriesMBTI_16types.csv"
df = None

if os.path.exists(default_path):
    try:
        df = pd.read_csv(default_path)
        st.success(f"기본 데이터 파일을 불러왔습니다: {default_path}")
    except Exception as e:
        st.warning(f"기본 파일을 읽는 중 오류 발생: {e}")

if df is None:
    uploaded = st.file_uploader("CSV 파일 업로드 (예: countriesMBTI_16types.csv)", type=["csv"])
    if uploaded is not None:
        df = pd.read_csv(uploaded)
        st.success("업로드한 CSV 파일을 사용합니다.")

if df is None:
    st.error("CSV 파일을 찾을 수 없습니다. 기본 파일을 넣거나 업로드 해주세요.")
    st.stop()

# ---------------------------
# 2) MBTI 컬럼 검증
# ---------------------------
required_first_col = "Country"
mbti_cols = [
    "INFJ","ISFJ","INTP","ISFP","ENTP","INFP","ENTJ","ISTP",
    "INTJ","ESFP","ESTJ","ENFP","ESTP","ISTJ","ENFJ","ESFJ"
]

missing = [c for c in [required_first_col]+mbti_cols if c not in df.columns]
if missing:
    st.error(f"필수 컬럼이 누락되었습니다: {missing}")
    st.stop()

for c in mbti_cols:
    df[c] = pd.to_numeric(df[c], errors="coerce")

# ---------------------------
# 3) Top10 계산 함수
# ---------------------------
def top10_for_type(data: pd.DataFrame, mbti_type: str) -> pd.DataFrame:
    temp = data[["Country", mbti_type]].dropna().copy()
    temp = temp.rename(columns={mbti_type: "value"})
    temp = temp.sort_values("value", ascending=False).head(10)
    temp["rank"] = range(1, len(temp)+1)
    temp["Type"] = mbti_type
    return temp

def build_single_chart(df_top: pd.DataFrame, title: str):
    hover = alt.selection_point(fields=["Country"], on="mouseover", nearest=True, empty=False)
    chart = (
        alt.Chart(df_top)
        .mark_bar()
        .encode(
            y=alt.Y("Country:N", sort="-x", title="국가"),
            x=alt.X("value:Q", title="비율", axis=alt.Axis(format=".0%")),
            tooltip=[
                alt.Tooltip("Country:N", title="국가"),
                alt.Tooltip("value:Q", title="비율", format=".2%"),
                alt.Tooltip("rank:O", title="순위"),
            ],
            opacity=alt.condition(hover, alt.value(1.0), alt.value(0.7)),
        )
        .add_params(hover)
        .properties(height=400, title=title)
        .interactive()
    )
    return chart

# ---------------------------
# 4) 단일 유형 선택 뷰
# ---------------------------
st.subheader("① 단일 유형 Top10 보기")

selected_type = st.selectbox("MBTI 유형 선택", options=mbti_cols, index=0)
df_top_single = top10_for_type(df, selected_type)

col1, col2 = st.columns([1, 1])
with col1:
    st.dataframe(
        df_top_single.assign(비율=lambda d: (d["value"]*100).round(2))
        .loc[:, ["rank", "Country", "비율"]],
        use_container_width=True
    )
with col2:
    st.altair_chart(build_single_chart(df_top_single, f"{selected_type} Top10"), use_container_width=True)

# ---------------------------
# 5) 모든 유형 탭
# ---------------------------
st.subheader("② 전체 유형별 Top10 (탭)")

tabs = st.tabs(mbti_cols)
for i, t in enumerate(mbti_cols):
    with tabs[i]:
        df_top_t = top10_for_type(df, t)
        st.altair_chart(build_single_chart(df_top_t, f"{t} 비율 Top10"), use_container_width=True)
