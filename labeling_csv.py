import os
import csv

# Hàm tạo file CSV
def create_csv(csv_filename):
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Ghi tiêu đề cột: Filename, Label
        writer.writerow(['Filename', 'Label', 'classID'])

# Hàm ghi tên file và nhãn vào file CSV
def write_labels_to_csv(audio_file, label, classid, csv_filename):
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        # Ghi thông tin file và nhãn
        writer.writerow([audio_file, label, classid])

# Hàm để quét thư mục và gán nhãn
def label_audio_files_in_folders(data_folder, csv_filename):
    # Duyệt qua các thư mục con trong thư mục chính
    for root, dirs, files in os.walk(data_folder):
        for folder in dirs:
            # Folder name chính là nhãn (label)

            label = folder  # en, ko, vi,...
            
            folder_path = os.path.join(root, folder)
            
            # Duyệt qua các file audio trong thư mục
            for audio_file in os.listdir(folder_path):
                if audio_file.endswith(".wav"):  # Chỉ xử lý file .wav
                    audio_file_path = os.path.join(folder, audio_file)

                    if label == "fold_vi":
                        classid = 1
                    if label == "fold_en":
                        classid = 2
                    if label == "fold_ko":
                        classid = 3
                    # print(audio_file_path)
                    # Ghi tên file và nhãn vào file CSV
                    write_labels_to_csv(audio_file, label, classid, csv_filename)

# Ví dụ sử dụng
data_folder = r"D:\0_Workplace\Project_Python\audio_process\data\train"  # Thư mục chứa các file âm thanh
csv_filename = r"D:\0_Workplace\Project_Python\audio_process\data\train\audio_labels2.csv"
classid = 0
# Tạo file CSV mới
create_csv(csv_filename)

# Gán nhãn cho các file audio trong thư mục
label_audio_files_in_folders(data_folder, csv_filename)
