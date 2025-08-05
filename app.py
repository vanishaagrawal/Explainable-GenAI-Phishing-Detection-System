from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import pickle
import os

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

features = ['UsingIP', 'LongURL', 'ShortURL', 'Symbol@', 'Redirecting//',
            'PrefixSuffix-', 'SubDomains', 'HTTPS', 'DomainRegLen', 'Favicon',
            'NonStdPort', 'HTTPSDomainURL', 'RequestURL', 'AnchorURL',
            'LinksInScriptTags', 'ServerFormHandler', 'InfoEmail', 'AbnormalURL',
            'WebsiteForwarding', 'StatusBarCust', 'DisableRightClick',
            'UsingPopupWindow', 'IframeRedirection', 'AgeofDomain',
            'DNSRecording', 'WebsiteTraffic', 'PageRank', 'GoogleIndex',
            'LinksPointingToPage', 'StatsReport']

@app.route('/')
def index():
    return render_template('index.html', features=features)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        input_data = [int(request.form.get(f, 0)) for f in features]
        prediction = model.predict([input_data])[0]
        prob = model.predict_proba([input_data])[0]
        confidence = round(np.max(prob) * 100, 2)

        # Save inputs + prediction to logs
        os.makedirs('logs', exist_ok=True)
        log_df = pd.DataFrame([input_data + [prediction]], columns=features + ['Prediction'])
        log_df.to_csv('logs/prediction_log.csv', mode='a', header=not os.path.exists('logs/prediction_log.csv'), index=False)

        result = "Phishing 🚨" if prediction == 1 else "Legitimate ✅"
        return render_template('index.html', features=features, result=result, confidence=confidence)
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
