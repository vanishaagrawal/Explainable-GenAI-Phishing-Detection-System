# 🔐 AI-Powered Phishing Detection System

This project is an Explainable GenAI-powered cybersecurity application that detects phishing websites using Machine Learning and generates human-readable explanations using Generative AI. The system improves transparency, interpretability, and user trust in phishing detection.

## 🚀 Features

* 🔍 Machine Learning-based phishing detection
* 📊 Confidence score using probability (`predict_proba`)
* 🤖 AI-generated explanation for predictions (GenAI integration)
* ⚡ Fallback logic if AI API is unavailable
* 🌐 Interactive web interface using Flask

## 🤖 Generative AI Integration
The project integrates Generative AI (Gemini API) to generate simplified explanations for phishing predictions. Instead of only displaying classification results, the system explains why a website may be considered phishing or legitimate, improving interpretability and user understanding.

## 📈 Model Performance
- Accuracy: 96%
- Precision: 94%
- Recall: 95%
- F1-Score: 94%

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **Scikit-learn**
* **NumPy & Pandas**
* **Generative AI (Gemini API)**
* **HTML (Frontend)**

## 🔄 Project Workflow
1. User enters website-related features
2. Data is preprocessed
3. ML model predicts phishing or legitimate website
4. Confidence score is generated
5. Generative AI explains the prediction
6. Result is displayed on Flask web interface

---

## 📸 Output Screenshot

![Output](screenshot_1.png)

---

## ▶️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/vanishaagrawal/phishing_detector.git
cd phishing_detector
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python app.py
```

### 4. Open in browser

```bash
http://127.0.0.1:5000/
```

---

## 🧠 Prediction Pipeline
- Feature extraction from website data
- ML inference using trained classification model
- Probability estimation using `predict_proba`
- AI-generated explanation using Gemini API
- Fallback response generation for API failures

## 📂 Project Structure
phishing_detector/
│── templates/
│── app.py
│── genai_explainer.py
│── model.pkl
│── dataset.csv
│── prediction_log.csv
│── requirements.txt
│── README.md

---

## 💡 Key Highlights
- Combined Machine Learning with Generative AI
- Built an Explainable AI (XAI) cybersecurity solution
- Implemented confidence-based prediction system
- Designed fallback mechanisms for API reliability
- Developed a complete end-to-end Flask web application

---

## 📌 Future Improvements

* Accept real-time URL input instead of manual features
* Improve UI/UX design
* Deploy the application on cloud (AWS/Render)
* Add user authentication

---

## 👩‍💻 Author

**Vanisha Agrawal**
B.Tech Computer Science

---

## ⭐ If you like this project

Give it a star ⭐ on GitHub!
