from pydrive.auth import GoogleAuth
from pydrive.drive import  GoogleDrive

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

folder = "1L51sp_-7E4m7ZYeoj3PLcviragio0oaR"
directory = "D:/Freelance Projects/Spy Bug with Server Uploading/RaspberryCode/"
name = "output.wav"
filepath = directory+name
file1 = drive.CreateFile({'parents' : [{'id': folder}], 'title' : name})
file1.SetContentFile(filepath)
file1.Upload()