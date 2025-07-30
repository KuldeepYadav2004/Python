import sounddevice as sd
duration = 3  # seconds
print("Recording...")
audio = sd.rec(int(duration * 44100), samplerate=44100, channels=1)
sd.wait()
print("Done")
