import streamlit as st
import datetime, time, pytz, requests
from PIL import Image

def rerun(t):
    time.sleep(t)
    raise st.script_runner.RerunException(st.script_request_queue.RerunData(None))

st.markdown('<style>body{background-color: Blue;}</style>',unsafe_allow_html=True)    

page = st.selectbox("", ["Trang chủ", "Điều khiển", "Giám sát", "Thống kê"])

if page == "Trang chủ":
    st.write(datetime.datetime.now(pytz.timezone('Asia/Saigon')).strftime("%a %d/%m/%Y, %X"))
    #st.markdown('<p style="font-family:sans-serif; font-size: 40px;"><font color="#ff6600"><b>QUẢN GIA THÔNG MINH</b><br></p>', unsafe_allow_html=True)
    st.markdown('<p style="font-family:sans-serif; font-size: 40px;"><b>QUẢN GIA THÔNG MINH</b><br></p>', unsafe_allow_html=True)
    image = Image.open(requests.get('https://hotondo.com.au/wp-content/uploads/2016/06/Header-1.jpg', stream=True).raw)
    st.image(image, caption='')
    
    col1, col2, col3, col4= st.columns(4)
    
    with col1:
        #st.markdown('<p style="font-family:sans-serif; font-size: 30px;">Nhiệt độ (°C)</p>', unsafe_allow_html=True)
        #st.markdown('<p style="font-family:sans-serif; color:Red; font-size: 50px;">00</p>', unsafe_allow_html=True)
        st.markdown("**Nhiệt độ (°C)**")
        st.write("00")
    with col2:
        st.markdown("**Độ ẩm (%RH)**")
        st.write("00")
        
    with col3:
        st.markdown("**Thiết bị đang bật**")
        st.write("0")
        
    with col4:
        st.markdown("**Công suất tiêu thụ (Wh)**")
        st.write("0.00")
        
    rerun(1)

elif page == "Điều khiển":
    sl = st.slider("pk",0, 3)

elif page == "Page 3":
    st.write("Display details of page 3")
