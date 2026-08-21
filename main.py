# main.py
import streamlit as st
import folium
from streamlit_folium import st_folium
import pandas as pd

# 1. 웹 페이지 설정
st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

st.title("🏞️🏞️ 2026 학교 등산 행사 안내 지도 🏞️🏞️")
st.markdown("우리 동아리가 직접 발로 뛰며 만든 코스 가이드 입니다")
st.markdown("왼쪽 메뉴에서 코스를 선택하고 행사에 참여해 보세요.")

# 2. 데이터 불러오기 및 가공
df = pd.read_csv('등산경로 - 시트1.csv', encoding='utf-8')
df['이미지'] = 'images/' + df['코스'] + df['위치명'] + '.jpg'

df_lation = df[['위도','경도']]
df_lation = df_lation.rename(columns={'위도':'lat','경도':'lon'})
st.map(df_lation) 

course_info = {
    "A코스": {
        "color": "blue",        "time": "4~5분",

        "desc": "학교 출발",
        "notice": "경사가 완만하여 초보자에게 추천합니다.",
        "caution": "편안한 운동화를 착용하세요."
    },
    "B코스": {
        "color": "green",
        "time": "8~9분",
        "desc": "가온어린이공원 경유",
        "notice": "탁 트인 조망과 아름다운 자연 경관을 즐길 수 있습니다.",
        "caution": "낙엽 및 미끄럼 주의, 등산화 권장."
    },
    "C코스": {
        "color": "orange",
        "time": "10~11분",
        "desc": "서해랑길 94코스 출발",
        "notice": "접근성이 뛰어난 완주 코스입니다.",
        "caution": "수분 보충을 위해 물을 챙기세요."
    },
    "D코스": {
        "color": "red",
        "time": "13~14분",
        "desc": "세븐일레븐 코스",
        "notice": "편의점이 있어 간식 및 음료 구매가 편리합니다.",
        "caution": "쓰레기는 반드시 되가지고 내려오세요."
    },
    "E코스": {
        "color": "purple",
        "time": "12~13분",
        "desc": "논현주공1단지 코스",
        "notice": "입구를 잘 찾아가야하는 코스입니다.",
        "caution": "벌레에 물리지 않도록 벌레기피제 사용을 권장합니다."
    }
}


# 3. 지도 생성 및 마커 표시 (지도 시각화 단계)
m = folium.Map(
    location=[37.40583317, 126.7214872],
    zoom_start=12
)

# 학교 위치 마커
folium.Marker(
    location=[37.404160, 126.719249],
    popup="남동고등학교",
    tooltip="남동고등학교",
    icon=folium.Icon(color='lightblue', icon='info-sign')
).add_to(m)

# 데이터프레임을 이용한 코스 마커
for i in range(len(df)):
    folium.Marker(
        location=[df.iloc[i]['위도'], df.iloc[i]['경도']],
        popup=f'<div style="width:200px"> <strong>{df.iloc[i]["위치명"]}</strong></div>',
        tooltip="클릭해보세요",
        icon=folium.Icon(color='green', icon='info-sign')
    ).add_to(m)
        
# 4. 화면 출력 (컬럼 나누기)
col1, col2 = st.columns([3, 1])

with col1:
    st_folium(m, width=700, height=500)

with col2:
    st.subheader("정보") # 코스정보
    st.info("길이 미끄럽습니다. 주의하세요.")
    st.metric(label="소요시간", value="10분") # 소요시간, 정보 코스별로 넣기
    st.write("주의사항 : 등산화를 착용하세요.")
