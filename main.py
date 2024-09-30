from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

datas = "Helsinki-NLP/opus-100"
model_name = "facebook/nllb-200-distilled-600M"
is_download = False


def download_model():
    model = AutoModelForSeq2SeqLM.from_pretrained("facebook/nllb-200-distilled-600M")
    tokenizer = AutoTokenizer.from_pretrained("facebook/nllb-200-distilled-600M")
    # TFAutoModelForSeq2SeqLM
    model.save_pretrained("./models/nllb-200-distilled-600M")
    print("done!")
    tokenizer.save_pretrained("./models/nllb-200-distilled-600M")
    print("done!!")


if is_download:
    download_model()


from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline
model = AutoModelForSeq2SeqLM.from_pretrained("./models/nllb-200-distilled-600M")
tokenizer = AutoTokenizer.from_pretrained("./models/nllb-200-distilled-600M")
translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="vie_Latn", tgt_lang='kor_Hang',
                      max_length=400)
input = input("input text")
print(translator(input))


