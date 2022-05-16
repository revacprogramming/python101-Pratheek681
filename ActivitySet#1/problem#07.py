# Strings

text = ("X-DSPAM-Confidence:    0.8475")
z= text.find('0.8475')
x = len(text)
print(float(text[z:x]))