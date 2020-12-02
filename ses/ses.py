import speech_recognition as sr
r = sr.Recognizer()
d= sr.AudioFile('gh.wav')
with d as kaynak:
    r.adjust_for_ambient_noise(kaynak)
    ses=r.record(kaynak)
    sonuc = r.recognize_google(ses,language='tr-TR', show_all=True)
print(sonuc)
