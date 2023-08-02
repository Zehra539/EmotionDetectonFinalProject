import json
import requests

def emotion_predictor(text_to_analyze):
    if not text_to_analyse.strip():  # Check for empty or blank input
        return None
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    response_dict = json.loads(response.text)
    if response.status_code == 200:
        emotions = response_dict['emotionPredictions'][0]['emotion']
        dominant_emotion = ''
        for emotion, score in emotions.items():
            if dominant_emotion == '' or score > emotions[dominant_emotion]:
                dominant_emotion = emotion
        emotions['dominant_emotion'] = dominant_emotion
        return emotions
    else:
        return None