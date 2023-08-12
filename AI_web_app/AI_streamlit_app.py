
from api.AI import AIAPI
import streamlit as st
from PIL import Image

@st.cache_resource
def get_api():
    return AIAPI(font="resources/malgun.ttf")

def main():
    api = get_api()
    
    st.title("2023 HAI 여름방학 AI 웹 앱 개발 과제")
    st.markdown("<p style='margin-bottom:30px'></p>", unsafe_allow_html=True)
    
    st.subheader("1. OCR API를 활용한 Image to Text")
    query = st.file_uploader("**이미지를 업로드하세요. (jpg, jpeg, png 파일만 가능)**", type=['jpg', 'jpeg', 'png'])
    
    # 업로드한 이미지 확인
    with st.expander("**업로드한 이미지**"):
        if query is not None:
            st.image(query)
        else:
            st.write("이미지를 업로드하세요.")
            
    # OCR 결과 확인
    with st.expander("**텍스트 인식 결과**", expanded=True) if query is not None else st.expander("**텍스트 인식 결과**"):
        if query is not None:
            ocrText = api.query_image2text(query, key='image2text')
            
            if ocrText != "":
                st.code(f"{ocrText}", language="python")
            # OCR 결과가 없을 경우
            else:
                st.code("텍스트를 인식할 수 없습니다.", language="python")
        else:
            st.write("이미지를 업로드하세요.")
            
    st.markdown("<p style='margin-bottom:25px'></p>", unsafe_allow_html=True)
    
    st.subheader("2. ChatGPT API를 활용한 Text 요약")
    
    # OCR 결과를 ChatGPT에 입력, 요약 결과 확인
    with st.expander("**요약 결과**", expanded=True) if query is not None else st.expander("**요약 결과**"):
        if query is not None:
            # OCR 결과가 없을 경우. 요약 불가능
            if (ocrText == ""):
                st.write("텍스트를 인식할 수 없습니다.")
                return
            # ChatGPT를 통한 요약
            title, summary = api.query_text2text(ocrText)
            st.subheader(title)
            st.markdown(summary)
            
        # 이미지를 업로드하지 않았을 경우
        else:
            st.write("이미지를 업로드하세요.")
        
if __name__ == '__main__':
    main()