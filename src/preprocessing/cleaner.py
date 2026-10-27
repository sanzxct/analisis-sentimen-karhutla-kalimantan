import re
import pandas as pd

def clean_tweet_text(text):
    if pd.isna(text):
        return ""
    
    text = str(text)
    # 1. Ubah ke huruf kecil (Case Folding)
    text = text.lower()
    # 2. Hapus URL / Tautan
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # 3. Hapus Mention (Karakter @)
    text = re.sub(r'\@\w+', '', text)
    # 4. Hapus Hashtag (#) tapi biarkan teksnya (opsional: re.sub(r'#\w+', '', text) jika ingin teksnya hilang)
    text = re.sub(r'#', '', text)
    # 5. Hapus angka dan tanda baca (Punctuation removal)
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    # 6. Hapus spasi berlebih (Whitespace removal)
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    
    return text