# -*- coding: utf-8 -*-
import os
import requests
from flask import Flask, render_template, request, jsonify
from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

app = Flask(__name__)

translator_key = os.environ.get("TRANSLATOR_KEY")
translator_region = "eastus"
language_key = os.environ.get("LANGUAGE_KEY")
language_endpoint = "https://ai-language-127.cognitiveservices.azure.com/"

lang_client = TextAnalyticsClient(endpoint=language_endpoint, credential=AzureKeyCredential(language_key))

def translate(text, to_lang):
    headers = {
        "Ocp-Apim-Subscription-Key": translator_key,
        "Ocp-Apim-Subscription-Region": translator_region,
        "Content-Type": "application/json"
    }
    params = {"api-version": "3.0", "to": to_lang}
    response = requests.post("https://api.cognitive.microsofttranslator.com/translate",
                             params=params, headers=headers, json=[{"text": text}])
    result = response.json()[0]
    detected_lang = result["detectedLanguage"]["language"]
    translated_text = result["translations"][0]["text"]
    return detected_lang, translated_text

def analyze(text):
    result = lang_client.analyze_sentiment([text])[0]
    return result.sentiment, round(result.confidence_scores.positive, 2), round(result.confidence_scores.negative, 2)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_text():
    data = request.get_json()
    user_text = data.get("text", "")

    # 先检测语言，决定翻译方向
    detected_lang, translated = translate(user_text, "en")  # 先翻译成英文用于情感分析

    if detected_lang == "en":
        # 输入是英文，额外翻译一份中文给用户看
        _, translated_zh = translate(user_text, "zh-Hans")
        display_translation = translated_zh
        analysis_text = user_text  # 英文直接分析
    else:
        # 输入是中文（或其他语言），翻译成英文
        display_translation = translated
        analysis_text = translated

    sentiment, pos, neg = analyze(analysis_text)

    return jsonify({
        "detected_lang": detected_lang,
        "translated": display_translation,
        "sentiment": sentiment,
        "positive": pos,
        "negative": neg
    })

if __name__ == "__main__":
    app.run(debug=True)
