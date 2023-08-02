import json
import requests

def emotion_predictor(text_to_analyze):
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyze } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=myobj, headers=header)
    status_code = response.status_code
    
    if status_code == 400:
        formatted_output = { 'anger': None,
                             'disgust': None,
                             'fear': None,
                             'joy': None,
                             'sadness': None,
                             'dominant_emotion': None }
    else:
        response_dict = json.loads(response.text)
        emotions = response_dict['emotionPredictions'][0]['emotion']
        dominant_emotion = ''
        for emotion, score in emotions.items():
            if dominant_emotion == '' or score > emotions[dominant_emotion]:
                dominant_emotion = emotion
                emotions['dominant_emotion'] = dominant_emotion
            return emotions
   