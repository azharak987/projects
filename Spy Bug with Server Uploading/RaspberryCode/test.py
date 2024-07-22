import pyaudio
import wave
import json
import requests
from datetime import datetime
chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 2
headers = {"Authorization": "Bearer ya29.A0ARrdaM9eTp5tWDdgT1WG60U6fc6oIDr3BDW041-NReAgN1UcZRD1zBpjC8vjUi0qf5JLSawko8EBepfbT65JDnAqU83fKkeeDl85k1aw_htHdfTqE5dhwSDxzaPeNhGO23-fknFCVMHxz319TmY_yj3UVT_w"}

for i in range(1, 10000000):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H.%M.%S")
    filename = dt_string+".wav"
    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    print('Recording')

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

    print('Finished recording')

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()