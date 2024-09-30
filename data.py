from datasets import load_dataset
import pandas as pd


# # Tải tập dữ liệu opus-100 với cặp ngôn ngữ tiếng Việt và tiếng Hàn
dataset = load_dataset("Helsinki-NLP/opus-100", "en-vi")
#
# data = {
#     "Vietnamese": [example['translation']['vi'] for example in dataset['train']],
#     "English": [example['translation']['en'] for example in dataset['train']]
# }
#
# df = pd.DataFrame(data)
# print(df.head())
#
# df.to_csv("vi_en_dataset.csv", index=False)


from datasets import load_dataset

# Tải tập dữ liệu từ Tatoeba với cặp ngôn ngữ tiếng Việt - tiếng Hàn
# dataset = load_dataset("tatoeba", lang1="ko", lang2="vi", trust_remote_code=True)

# Hiển thị một vài mẫu dữ liệu
print(dataset['train'][0])

import pandas as pd

# Chuyển đổi tập dữ liệu sang danh sách các cặp câu
data = {
    "Vietnamese": [example['translation']['vi'] for example in dataset['train']],
    "Korean": [example['translation']['ko'] for example in dataset['train']]
}

# Tạo DataFrame từ dữ liệu
# df = pd.DataFrame(data)

# Hiển thị một vài hàng trong DataFrame
# print(df)
# df.to_csv("vi_ko_dataset.csv", index=False)