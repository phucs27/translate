from pydub import AudioSegment

m4a_file = r'D:\0_Workplace\data_audio\vi_322_3.m4a' # I have downloaded sample audio from this link https://getsamplefiles.com/sample-audio-files/m4a
wav_filename = r'D:\0_Workplace\data_audio\vi_322_3.wav'

sound = AudioSegment.from_file(m4a_file, format='m4a')
sound.export(wav_filename, format='wav')