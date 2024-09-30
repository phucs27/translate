import torch
from datasets import load_dataset
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Trainer, TrainingArguments

# Bước 1: Tải dataset opus-100 với tham số "en-vi"
dataset = load_dataset("Helsinki-NLP/opus-100", "en-vi")

# Bước 2: Chia dataset thành train, valid và test
train_dataset = dataset['train']
valid_dataset = dataset['validation']
test_dataset = dataset['test']

# Bước 3: Tải model và tokenizer
model = AutoModelForSeq2SeqLM.from_pretrained("./models/nllb-200-distilled-600M")
tokenizer = AutoTokenizer.from_pretrained("./models/nllb-200-distilled-600M")


# Bước 4: Tokenize dữ liệu
def tokenize_function(examples):
    # Sử dụng các trường trong examples cho từng bản ghi
    inputs = [example['translation']['en'] for example in examples]
    targets = [example['translation']['vi'] for example in examples]

    return tokenizer(
        inputs,
        targets,
        padding="max_length",
        truncation=True,
        max_length=128  # Có thể điều chỉnh chiều dài tối đa
    )


# Áp dụng tokenize cho tập dữ liệu huấn luyện và kiểm tra
train_tokenized = train_dataset.map(tokenize_function, batched=True)
valid_tokenized = valid_dataset.map(tokenize_function, batched=True)

# Bước 5: Định nghĩa các tham số huấn luyện
training_args = TrainingArguments(
    output_dir="./results",
    evaluation_strategy="epoch",
    learning_rate=2e-5,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=16,
    num_train_epochs=3,
    weight_decay=0.01,
    save_total_limit=2,
    logging_dir='./logs',  # Thư mục để lưu log
)

# Bước 6: Khởi tạo Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_tokenized,
    eval_dataset=valid_tokenized,
)

# Bước 7: Huấn luyện model
trainer.train()

# Bước 8: Lưu model
trainer.save_model("./fine_tuned_nllb")

print("Huấn luyện hoàn tất và model đã được lưu!")
