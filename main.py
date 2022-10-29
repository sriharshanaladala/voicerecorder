import sounddevice

from scipy.io.wavfile import write

fs = 44100
seconds= int(input("enter time duration in seconds"))
print("recoding.......\n")
record_voice=sounddevice.rec(int(seconds*fs),samplerate=fs, channels=2)
sounddevice.wait()
write("out.wav", fs, record_voice)
print("finished....\nplease check it .....")