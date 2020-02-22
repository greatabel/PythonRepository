import re


product_review = '''This is a fine milk, but the product
line appears to be limited in available colors. I
could only find white.'''  # <1>

sentence_pattern = re.compile(r'(.*?\.)(\s|$)', re.DOTALL)  # <2>
matches = sentence_pattern.findall(product_review)  # <3>
sentences = [match[0] for match in matches]  # <4>
print(sentences)