from fastapi import FastAPI
from pydantic import BaseModel
import pickle
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
import uvicorn
import numpy as np
import re

# Import NLTK (không cần try/except nữa)
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# --- Giá trị từ model của bạn ---
MAX_SEQUENCE_LENGTH = 200 # Đã sửa thành 200

# 1. Khởi tạo ứng dụng FastAPI
app = FastAPI()

# 2. Định nghĩa cấu trúc input
class NewsItem(BaseModel):
    text: str

# 3. Tải mô hình và tokenizer
print("Đang tải tokenizer (tokenizer.pkl)...")
with open('tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

print("Đang tải mô hình Keras (model.h5)...")
model = load_model('model.h5')

# --- Khởi tạo các công cụ tiền xử lý ---
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()
print("Tải mô hình, tokenizer và công cụ NLTK thành công!")


# 4. HÀM TIỀN XỬ LÝ MỚI
def clean_and_preprocess_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    tokens = word_tokenize(text)
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [lemmatizer.lemmatize(word) for word in tokens]
    cleaned_text = ' '.join(tokens)
    return cleaned_text


# 5. Tạo endpoint /predict
@app.post("/predict")
async def predict_news(item: NewsItem):
    try:
        cleaned_text = clean_and_preprocess_text(item.text)
        text_seq = tokenizer.texts_to_sequences([cleaned_text])
        text_padded = pad_sequences(
            text_seq, 
            maxlen=MAX_SEQUENCE_LENGTH,
            padding='post',
            truncating='post'
        )
        prediction_value = model.predict(text_padded)[0][0]

        if prediction_value > 0.5:
            prediction = "Tin Thật"
            confidence = prediction_value
        else:
            prediction = "Tin Giả"
            confidence = 1 - prediction_value

        return {
            "prediction": prediction,
            "confidence": float(confidence),
            "raw_score_from_model": float(prediction_value)
        }
    
    except Exception as e:
        # Trả về lỗi chi tiết
        return {"error": str(e)}

# 6. (Tùy chọn) Chạy app
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)