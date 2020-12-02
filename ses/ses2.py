import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Konuş")
    audio=r.listen(source)
    try:
        text = r.recognize_google(audio)
        print('Sen ==> {} dedin'.format(text))
    except:
        print('HATA ses algılanmadı')

