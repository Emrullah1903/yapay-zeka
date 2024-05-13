import speech_recognition as sr
import pyttsx3
import webbrowser

def sesi_tanima():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Bir şey söyleyin:")
        recognizer.adjust_for_ambient_noise(source)
        ses_verisi = recognizer.listen(source)
        print("Ses verisi alındı.")

    try:
        komut = recognizer.recognize_google(ses_verisi, language="tr-TR").lower()
        print(f"Ses Tanıma Başarılı: {komut}")
        if "youtube'da video ara" in komut:
            video_ara(komut.replace("youtube'da video ara", ""))
        else:
            cevap_ver("Anlaşılan bir komut bulunamadı.")
    except sr.UnknownValueError:
        print("Ses anlaşılamadı.")
    except sr.RequestError as e:
        print(f"Ses tanıma servisi hatası; {e}")

def video_ara(arama_sorgusu):
    url = f"https://www.youtube.com/results?search_query={arama_sorgusu}"
    webbrowser.open(url)

def cevap_ver(cevap_metni):
    engine = pyttsx3.init()
    engine.say(cevap_metni)
    engine.runAndWait()

if __name__ == "__main__":
    sesi_tanima()


def sesi_tanima():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Bir şey söyleyin:")
        recognizer.adjust_for_ambient_noise(source)
        ses_verisi = recognizer.listen(source)
        print("Ses verisi alındı.")

    try:
        metin = recognizer.recognize_google(ses_verisi, language="tr-TR")
        print(f"Ses Tanıma Başarılı: {metin}")
        sorulara_cevap_ver(metin.lower())
    except sr.UnknownValueError:
        print("Ses anlaşılamadı.")
    except sr.RequestError as e:
        print(f"Ses tanıma servisi hatası; {e}")

def sorulara_cevap_ver(ses_metni):
    engine = pyttsx3.init()
    
    # Adjust the rate to make the voice speak more slowly
    engine.setProperty('rate', 150)  # You can experiment with different values

    
    # Add the following lines to set the voice
    voices = engine.getProperty('voices')
    new_voice_id = 0  # Replace with the index of the desired voice
    engine.setProperty('voice', voices[new_voice_id].id)

    if "merhaba" in ses_metni:
        cevap = "merhaba "
    if "nasılsın" in ses_metni:
        cevap = "Ben bir programım, teşekkür ederim. Siz nasılsınız?"
    elif "günün nasıl geçti" in ses_metni:
        cevap = "Günüm iyi geçiyor, teşekkür ederim. Sizinki nasıl geçiyor?"
   
    else:
        cevap = "Anlaşılan bir soru bulunamadı."

    print(cevap)
    engine.say(cevap)
    engine.runAndWait()

if __name__ == "__main__":
    sesi_tanima()
