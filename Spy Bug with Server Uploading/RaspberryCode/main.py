import pyaudio
import wave
from datetime import datetime
from pydrive.auth import GoogleAuth
from pydrive.drive import  GoogleDrive
import os
gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = "1L51sp_-7E4m7ZYeoj3PLcviragio0oaR"
directory = "/home/pi/Desktop/Code/"
chunk = 1024  # Record in chunks of 1024 samples
sample_format = pyaudio.paInt16  # 16 bits per sample
channels = 2
fs = 44100  # Record at 44100 samples per second
seconds = 600
previousFile = ""

while(1):
    now = datetime.now()
    dt_string = now.strftime("%d-%m-%Y-%H.%M.%S")
    filename = dt_string + ".mp3"
    p = pyaudio.PyAudio()  # Create an interface to PortAudio
    #filename = "output.wav"
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
    print("Uploading...")
    filepath = directory+filename
    file1 = drive.CreateFile({'parents': [{'id': folder}], 'title': filename})
    file1.SetContentFile(filepath)
    try:
        file1.Upload()
        print("Uploaded.")
        print("Deleting")
        try:
            os.remove(previousFile)
            print("Deleted")
        except:
            print("File Does not exist")
        previousFile = filepath
    except:
        print("File Not uploaded")
