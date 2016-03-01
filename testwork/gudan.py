# NOTE: this requires PyAudio because it uses the Microphone class
import speech_recognition as sr
r = sr.Recognizer()
"""
['__class__',
 '__delattr__',
 '__dict__',
 '__doc__',
 '__enter__',
 '__exit__',
 '__format__',
 '__getattribute__',
 '__hash__',
 '__init__',
 '__module__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 'adjust_for_ambient_noise',
 'dynamic_energy_adjustment_damping',
 'dynamic_energy_ratio',
 'dynamic_energy_threshold',
 'energy_threshold',
 'listen',
 'listen_in_background',
 'non_speaking_duration',
 'pause_threshold',
 'phrase_threshold',
 'recognize_att',
 'recognize_google',
 'recognize_ibm',
 'recognize_sphinx',
 'recognize_wit',
 'record']
"""


import wikipedia as wiki
import os

def hktry(txt):
    sdata=wiki.search(txt)
    for data in sdata:
        print data
    saytxt=wiki.page(sdata[0]).content[:500]
    saytxt=saytxt.encode('ascii','ignore')
    os.system('google_speech "'+saytxt+'"')


with sr.Microphone() as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

try:
    txt=r.recognize_google(audio)
    print txt
    hktry(txt)

except LookupError:
    print("Could not understand audio")
