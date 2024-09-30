import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer, pipeline

# Load model and tokenizer
@st.cache_resource
def load_model():
    model = AutoModelForSeq2SeqLM.from_pretrained("./models/nllb-200-distilled-600M")
    tokenizer = AutoTokenizer.from_pretrained("./models/nllb-200-distilled-600M")
    translator = pipeline('translation', model=model, tokenizer=tokenizer, src_lang="vie_Latn", tgt_lang='eng_Latn', max_length=400)
    return translator

translator = load_model()

# Streamlit app layout
st.title("Translate")
st.write(" ")

# Input text box
input_text = st.text_area("Input Text", placeholder="...")

# Translation button
if st.button("Translate"):
    if input_text.strip() == "":
        st.error("Vui lòng nhập văn bản trước khi dịch.")
    else:
        # Translate the input text
        translation = translator(input_text)
        translated_text = translation[0]['translation_text']
        st.success("Translation:")
        st.write(translated_text)

# https://github.com/facebookresearch/flores/tree/main/flores200#languages-in-flores-200