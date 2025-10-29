import streamlit as st
import requests
import json

# Sửa lại port cho đúng nếu bạn đã đổi (ví dụ: 8080)
API_URL = "http://127.0.0.1:8080/predict" 

st.set_page_config(page_title="Trình Phát hiện Tin giả", page_icon="📰")
st.title("📰 Trình Phát hiện Tin tức Giả/Thật")
st.write("Dán nội dung bài báo vào ô dưới đây để kiểm tra.")

user_input = st.text_area("Nội dung bài báo", height=200)

if st.button("Kiểm tra"):
    if user_input:
        try:
            payload = {"text": user_input}
            response = requests.post(API_URL, json=payload)

            if response.status_code == 200:
                data = response.json()
                
                # --- SỬA LỖI Ở ĐÂY ---
                # Kiểm tra xem API có trả về lỗi không
                if "error" in data:
                    st.error(f"Lỗi từ Backend API: {data.get('error')}")
                
                # Nếu không có lỗi, thì mới hiển thị kết quả
                else:
                    prediction = data.get("prediction")
                    confidence = data.get("confidence")

                    if prediction == "Tin Thật":
                        st.success(f"Đây là **Tin Thật** (Độ tin cậy: {confidence*100:.2f}%)")
                    else:
                        st.error(f"Đây là **Tin Giả** (Độ tin cậy: {confidence*100:.2f}%)")
                    
                    st.write("Chi tiết JSON trả về:")
                    st.json(data)
                # --- KẾT THÚC SỬA LỖI ---

            else:
                st.error(f"Lỗi từ API (Status code: {response.status_code}): {response.text}")

        except requests.exceptions.ConnectionError:
            st.error(f"Lỗi: Không thể kết nối đến Backend API ({API_URL}). Bạn đã chạy 'uvicorn' chưa?")
        except Exception as e:
            st.error(f"Đã xảy ra lỗi: {e}")
    else:
        st.warning("Vui lòng nhập nội dung tin tức để kiểm tra.")