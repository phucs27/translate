from pydub import AudioSegment
from datetime import datetime
# Đọc file audio WAV
audio = AudioSegment.from_wav(r'D:\0_Workplace\data_audio\vi_322_1.wav')

# Độ dài mỗi đoạn (đơn vị là mili giây)
segment_length = 5 * 1000  # 10 giây

time = datetime.now()
datetime_str = time.strftime("%Y_%m_%d_%H_%M_%S_%f")
print(datetime_str)

# Cắt và lưu file thành nhiều đoạn
for i in range(0, len(audio), segment_length):
    segment = audio[i:i + segment_length]
    file_name = f"_{i // 1000}_" + datetime_str + ".wav"
    file_path = r'D:\0_Workplace\data_audio\tu_thu\vi' + file_name
    segment.export(file_path, format="wav")
    print(file_path)

print("Completed!")
