import requests

def emotion_detector(text_to_analyze:str):

    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    body = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(URL, headers=headers, json=body)

    output = response.json().get("emotionPredictions")

    emotions = output[0].get("emotion")

    emotions['dominant_emotion'] = max(emotions, key=emotions.get)

    return emotions
if __name__=="__main__":
    print(emotion_detector(" I am so happy I am doing this."))