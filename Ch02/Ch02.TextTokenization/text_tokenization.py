import os
import requests
import tiktoken
import torch
import gpt_dataset as ds
from simple_vocabulary import SimpleVocabulary
from simple_tokenizer import SimpleTokenizer

file_path = "./Ch02/Ch02.TextTokenization/the-verdict.txt"

if not os.path.exists(file_path):
    url = (
        "https://raw.githubusercontent.com/rasbt/"
        "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
        "the-verdict.txt"
    )
    
    response = requests.get(url, timeout=50)
    response.raise_for_status()
    
    with open(file_path, "wb") as f:
        f.write(response.content)
        
with open(file_path, "r", encoding="utf-8") as f:
        raw_text = f.read()
        
vocabulary = SimpleVocabulary(raw_text);
tokenizer = tiktoken.get_encoding("gpt2")

#dataloader = ds.create_dataloader(raw_text, batch_size=8, max_length=4, stride=4, shuffle=False);
#data_iter = iter(dataloader)
#inputs, targets = next(data_iter)

vocab_size = 50257
output_dim = 256

embedding_layer = torch.nn.Embedding(vocab_size, output_dim)
