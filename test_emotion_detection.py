from EmotionDetection import emotion_detector

result = emotion_detector("I am glad this happened")
print("joy" if result["dominant_emotion"] == "joy" else "Failed")

result = emotion_detector("I am really mad about this")
print("anger" if result["dominant_emotion"] == "anger" else "Failed")

result = emotion_detector("I feel disgusted just hearing about this")
print("disgust" if result["dominant_emotion"] == "disgust" else "Failed")

result = emotion_detector("I am so sad about this")
print("sadness" if result["dominant_emotion"] == "sadness" else "Failed")

result = emotion_detector("I am really afraid that this will happen")
print("fear" if result["dominant_emotion"] == "fear" else "Failed")
