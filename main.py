import numpy
import random

letters = list("abcdefghijklmnopqrstuvwxyz")
num = list('1234567890')

full_vocab = letters + num
id = 0

alphabet = []

for i in range(len(full_vocab)):
  x = {full_vocab[0+i]: id}
  alphabet.append(x) 
  id += 1
  
print(alphabet)