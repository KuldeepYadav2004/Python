import pyaudio
import wave

def record_audio(filename, duration=5, channels=1, rate=44100, chunk=1024):
    p = pyaudio.PyAudio()

    # Open stream for recording
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=chunk)

    print(f"Recording for {duration} seconds...")

    frames = []

    for _ in range(0, int(rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Finished recording.")

    # Stop and close stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save to WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(rate)
    wf.writeframes(b''.join(frames))
    wf.close()


def play_audio(filename, chunk=1024):
    wf = wave.open(filename, 'rb')
    p = pyaudio.PyAudio()

    # Open stream for playback
    stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                    channels=wf.getnchannels(),
                    rate=wf.getframerate(),
                    output=True)

    print("Playing back audio...")

    data = wf.readframes(chunk)

    while data:
        stream.write(data)
        data = wf.readframes(chunk)

    stream.stop_stream()
    stream.close()
    p.terminate()


if __name__ == "__main__":
    audio_file = "test_audio.wav"
    record_audio(audio_file, duration=5)
    play_audio(audio_file)
