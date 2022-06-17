

from nltk.stem import PorterStemmer


e_words= ["Please wait", "I am waiting", "I waited", "He waits"]

ps =PorterStemmer()

for w in e_words:
 rootWord=ps.stem(w)
 print(rootWord)



#Lemmatization:

# import these modules
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print("rocks :", lemmatizer.lemmatize("rocks"))

print("corpora :", lemmatizer.lemmatize("corpora"))

# a denotes adjective in "pos"

print("better :", lemmatizer.lemmatize("better", pos ="a"))

print(dir(lemmatizer.lemmatize))

print("\n\n")
help(lemmatizer.lemmatize)
