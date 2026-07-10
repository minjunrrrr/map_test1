# main.py
import streamlit as st
#import folium
#from streamlit_folium import st_folium
import pandas as pd

# 1. 웹 페이지 설정
st.set_page_config(page_title="남동고 등산 메이트", layout="wide")

st.title("🏞️🏞️ 2026 학교 등산 행사 안내 지도 🏞️🏞️")
st.markdown("우리 동아리가 직접 발로 뛰며 만든 코스 가이드 입니다")
st.markdown("왼쪽 메뉴에서 코스를 선택하고 행사에 참여해 보세요.")
st.markdown("# 큰 제목 ")
st.markdown("## 작은 제목 ")
st.markdown("**굵은 글씨**와 *이탤릭체* ")

# 2. 데이터 읽어보기(데이터 수집 csv)
st.header("헤더입니다")
st.subheader("서브헤더입니다")
st.caption("캡션입니다")
st.code("a=3")

st.text("안녕~~ 남동고등학교 여러분,, 첫 페이지를 만드셨습니다.")


df = pd.read_csv('등산경로.csv', encoding= 'utf-8')
df_lation = df[['위도','경도']]
df_lation = df_lation.rename(columns={'위도':'lat','경도':'lon'})
#st.map(df_lation)

# 3. 지도 생성 및 마커 표시(지도 시각화 단계)
m = folium.Map(
    location=[37.40583317,126.7214872],
    zoom_start=12
)

folium.Marker(
  location= [37.404160, 126.719249],
  popup= "ㅁ ㅁ ㅁ",
  tooltip="남동고등학교",
  icon = folium.Icon(color='lightblue', icon='info-sign')
).add_to(m)


for i in range(len(df)):
    folium.Marker(
        location = [df.iloc[i]['위도'], df.iloc[i]['경도']],
        popup=f'div style="width:200px"> <strong>{df.iloc[i]['위치명']}</strong></div>',
        tooltip="클릭해보세요",
        icon = folium.Icon(color='green', icon= 'info-sign')
        ).add_to(m)
        
# 4. 화면 출력
st_folium(m, width=700, height=500)

# 4. 화면 출력
col1 , col1 = st.colums([3.1])

with col1:
    st_folium(m, width=700, height=500)

with col2:
    st.subheader("정보") # 코스정보
    st.info("길이 미끄럽습니다. 주의하세요.")
    st.martric(lable="소요시간", value="10분") # 소요시간, 정보 코스별로 넣기
    st.write("주의사항 : 등산화를 착용하세요. ")
