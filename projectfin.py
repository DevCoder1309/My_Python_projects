import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
volume = engine.getProperty('volume')
engine.setProperty('volume', 10.0)
rate = engine.getProperty('rate')

engine.setProperty('rate', rate - 25)

a = ['America']
b = ['Poland']
c = ['Singapore']
d = ['Indonesia']
e = ['Bangladesh']
f = ['France']
g = ['Germany']
h = ['Egypt']
i = ['Vietnam']
j = ['Nepal']
k = ['China']
l = ['Russia']
m = ['Ukraine']
n = ['Srilanka']
o = ['Japan']
p = ['Hong Kong']
q = ['Malaysia']
s = ['Bahrain']
t = ['Saudi Arabia']
u = ['Switzerland']
v = ['United Kingdom']
w = ['Canada']
x = ['Argentina']
y = ['Norway']
z = ['Turkey']
aa= ['South Africa']
bb= ['Australia']
cc= ['New Zealand']
dd= ['Kenya']
ee= ['Ghana']


while True:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        engine.say("what is the amount in indian rupee")
        engine.runAndWait()
        audio = r.listen(source)
        try:
            print("You said:- " + r.recognize_google(audio))
        except sr.UnknownValueError:
            print("Could not understand audio")
            engine.say('I didnt get that. Rerun the code')
            engine.runAndWait()
            exit()
        with sr.Microphone() as source:
            engine.say("Which country ")
            engine.runAndWait()
            audio_country = r.listen(source)
    if r.recognize_google(audio_country) in a:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)/80)
        engine.say(f"the value is {var_2} dollars")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in b:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.053)
        engine.say(f"the value is {var_2} polish zloty")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in c:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.016)
        engine.say(f"the value is {var_2} dollars")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in d:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*188.75)
        engine.say(f"the value is {var_2} indonesian rupiah ")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in e:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*1.26)
        engine.say(f"the value is {var_2} taka")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in f:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.011)
        engine.say(f"the value is {var_2} euros")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in g:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.011)
        engine.say(f"the value is {var_2} euros")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in h:
        var_1 = r.recognize_google(audio)
        var_2 = str(int(var_1)*0.3)
        engine.say(f"the value is {var_2} egyption pound")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in i:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*285.31)
        engine.say(f"the value is {var_2} vietnamese dong")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in j:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*1.61)
        engine.say(f"the value is {var_2} nepalese rupee")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in k:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.084)
        engine.say(f"the value is {var_2} chinese yuan")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in l:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.78)
        engine.say(f"the value is {var_2} russian ruble")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in m:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.45)
        engine.say(f"the value is {var_2} ukrainian hryvnia")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in n:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*4.46)
        engine.say(f"the value is {var_2} srilankan rupees")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in o:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*1.65)
        engine.say(f"the value is {var_2} japanese yen")
        engine.runAndWait()
        exit() 
    elif r.recognize_google(audio_country) in p:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.094)
        engine.say(f"the value is {var_2} hong kong dollar")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in q:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.054)
        engine.say(f"the value is {var_2} malaysian ringitt")
        engine.runAndWait()
        exit() 
    elif r.recognize_google(audio_country) in s:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.0046)
        engine.say(f"the value is {var_2} bahraini dinar")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in t:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.046)
        engine.say(f"the value is {var_2} saudi riyal")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in u:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.011)
        engine.say(f"the value is {var_2} swiss franc")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in v:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.0099)
        engine.say(f"the value is {var_2} british pound sterling")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in w:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.016)
        engine.say(f"the value is {var_2} canadian dollar")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in x:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*2.09)
        engine.say(f"the value is {var_2} argentine peso")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in y:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.12)
        engine.say(f"the value is {var_2} norwegian krone")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in z:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.23)
        engine.say(f"the value is {var_2} turkish lira")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in aa:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.21)
        engine.say(f"the value is {var_2} south african rand")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in bb:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.018)
        engine.say(f"the value is {var_2} australian dollar")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in cc:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.019)
        engine.say(f"the value is {var_2} new zealand dollar")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in dd:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*1.49)
        engine.say(f"the value is {var_2} kenyan shilling")
        engine.runAndWait()
        exit()
    elif r.recognize_google(audio_country) in ee:
        var_1 = r.recognize_google(audio)
        var_2 = str(float(var_1)*0.11)
        engine.say(f"the value is {var_2} ghanaian cedi")
        engine.runAndWait()
        exit()
    
    
    
    
    
    
    
    