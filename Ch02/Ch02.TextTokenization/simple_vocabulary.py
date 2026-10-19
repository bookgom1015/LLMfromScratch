import re

class SimpleVocabulary:
    def __init__(self, text):
        self.preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', text)
        self.preprocessed = [item.strip() for item in self.preprocessed if item.strip()]        
        self.all_tokens = sorted(set(self.preprocessed))
        self.all_tokens.extend(["<|endoftext|>", "<|unk|>"])
        self.vocab_size = len(self.all_tokens)
        self.vocab = {token:integer for integer,token in enumerate(self.all_tokens)}
        
    def get(self):
        return self.vocab