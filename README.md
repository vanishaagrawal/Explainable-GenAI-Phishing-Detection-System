# 🔐 AI-Powered Phishing Detection System

This project is a Machine Learning-based web application that detects whether a website is **phishing or legitimate**. It is enhanced with **Generative AI** to provide human-readable explanations for predictions, improving user trust and interpretability.

---

## 🚀 Features

* 🔍 Machine Learning-based phishing detection
* 📊 Confidence score using probability (`predict_proba`)
* 🤖 AI-generated explanation for predictions (GenAI integration)
* ⚡ Fallback logic if AI API is unavailable
* 🌐 Interactive web interface using Flask

---

## 🛠️ Tech Stack

* **Python**
* **Flask**
* **Scikit-learn**
* **NumPy & Pandas**
* **Generative AI (Gemini API)**
* **HTML (Frontend)**

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

## 🧠 How It Works

1. User inputs website features
2. ML model predicts:

   * Phishing 🚨
   * Legitimate ✅
3. Confidence score is calculated
4. Generative AI explains the prediction in simple terms
5. If API fails, fallback explanation is shown

---

## 💡 Key Highlights

* Integrated **Generative AI** with traditional ML model
* Improved interpretability of predictions
* Implemented **fallback mechanism** for reliability
* Built a complete end-to-end web application

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
