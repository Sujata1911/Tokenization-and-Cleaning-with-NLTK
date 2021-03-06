#load data
filename='metamorphosis_clean.txt'
file=open(filename,'rt')
text=file.read()
file.close()

#split into words
from nltk.tokenize import word_tokenize
tokens=word_tokenize(text)

#stemming of words
from nltk.stem.porter import PorterStemmer
porter = PorterStemmer()
stemmed = [porter.stem(word) for word in tokens]
print(stemmed[:100])

#all words will automatically be converted to lowercase, no lowecase() required
