def explain_prediction(url, prediction):
    try:
        from google import genai

        client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

        prompt = f"""
        A phishing detection model predicted:

        Input Features: {url}
        Prediction: {prediction}

        Explain in simple and clear terms why this could be phishing or safe.
        """

        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt,
        )

        return response.text

    except Exception as e:
        # ✅ FALLBACK (IMPORTANT)
        if prediction == 1:
            return "This website appears to be phishing due to suspicious patterns, possible lack of HTTPS, or abnormal URL structure."
        else:
            return "This website appears legitimate as it follows normal security practices and does not show suspicious behavior."