import sys
from gpt import GPTLanguageModel

path = sys.argv[1]
prompt = sys.argv[2]
gen_type = sys.argv[2]
model = GPTLanguageModel.from_pretrained(path)
print(model.generate(prompt, max_new_tokens=500))
