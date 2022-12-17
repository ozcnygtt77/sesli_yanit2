import speech_recognition as sr
from playsound import playsound

class RTE1453():
    def __init__(self):
        self.isSpoke = False
        pass
    def record(self):
        vr = sr.Recognizer()
        print("dinliyorum...") 
        
        with sr.Microphone() as source:
            m_audio = vr.listen(source)
            voice = ""

            try: 
                voice = vr.recognize_google(m_audio, language = 'tr-TR')    

            except sr.UnknownValueError:
                print("anlamadım") 
            
            except sr.RequestError:
                print('sisteme erişilmiyor internet bağlantısı yok')
            return voice
    def speak(self, voice):
        self.isSpoke = not self.isSpoke
        voice = voice.lower()
        print(voice)

        if "elma" in voice:
            playsound("./voice/gene-caktin.wav")

rte1453 = RTE1453()
voice = rte1453.record()
rte1453.speak(voice)