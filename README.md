# nlp-fake-news-classifier
An NLP project for detecting fake news articles using classical ML models and BERT.
# 📰 Fake News Detection with NLP

## 📌 Overview
This project aims to build a **Fake News Detection system** using **Natural Language Processing (NLP)** techniques.  
We implemented both **classical deep learning models (CNN + LSTM)** and **state-of-the-art Transformer models (BERT)** to classify news articles as **True (1)** or **Fake (0)**.

The project covers the full pipeline:
1. Data preprocessing and cleaning
2. Handling class imbalance
3. Feature extraction (TF-IDF, Tokenization)
4. Model training (CNN+LSTM, BERT)
5. Model evaluation (classification report, confusion matrix, metrics)
6. Inference demo for new input text

---

## 📂 Dataset
- **Source**: Custom dataset with two CSV files  
  - `DataSet_Misinfo_TRUE.csv` → True news  
  - `DataSet_Misinfo_FAKE.csv` → Fake news  
- **Columns**:  
  - `text`: News article content  
  - `label`: Target label (`1 = True`, `0 = Fake`)

---

## ⚙️ Installation
Clone this repository and install dependencies:

```bash
git clone https://github.com/hdyzute/fake-news-detection.git
cd fake-news-detection

# Install required packages
pip install -r requirements.txt

## 🧠 Models

### 1. CNN + LSTM (Keras / TensorFlow)
- Word Embeddings  
- Convolution + Pooling layers  
- Bi-directional LSTM  
- Fully connected + Dropout  

### 2. BERT (HuggingFace Transformers + PyTorch)
- Tokenization with **bert-base-uncased**  
- Fine-tuning on news dataset  
- Optimization with **AdamW** and **learning rate scheduler**

---

## 🛠️ Tech Stack

- **Languages**: Python  

- **Libraries**:  
  - **NLP**: NLTK, Scikit-learn, HuggingFace Transformers  
  - **Deep Learning**: TensorFlow, PyTorch  
  - **Data Handling**: Pandas, NumPy  
  - **Visualization**: Matplotlib, Seaborn  
  - **Imbalance Handling**: imbalanced-learn (SMOTE)  

## Demo giao diện
![Demo](https://raw.githubusercontent.com/hdyzute/nlp-fake-news-classifier/main/demo.png)

![Demo](https://raw.githubusercontent.com/hdyzute/nlp-fake-news-classifier/8b68227048a8826b755b31b336f161bb35a7780a/demo.png)

![Demo](https://raw.githubusercontent.com/hdyzute/nlp-fake-news-classifier/main/8b68227048a8826b755b31b336f161bb35a7780a/demo.png)

https://raw.githubusercontent.com/hdyzute/nlp-fake-news-classifier/8b68227048a8826b755b31b336f161bb35a7780a/demo.png

