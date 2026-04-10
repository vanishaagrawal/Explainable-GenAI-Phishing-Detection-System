import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

df = pd.read_csv('dataset.csv')
X = df.drop(['Index', 'class'], axis=1)
y = df['class']

model = RandomForestClassifier()
model.fit(X, y)

with open('phishing_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("Model trained and saved as phishing_model.pkl")
