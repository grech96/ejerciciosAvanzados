
from collections import Counter
lista_angramas = ['eat','te','ate','appa','papa','tea','for','rof','che','hec','ech']
word = 'for'

result = list(filter(lambda x: (Counter(word) == Counter(x)), lista_angramas)) 

print(result)
