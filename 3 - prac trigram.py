
# implement a tri-gram model 


import nltk
import string

from nltk.corpus import reuters
from nltk.corpus import stopwords
from nltk import FreqDist




# collect data from internet
# data come from
# https://en.wikipedia.org/wiki/Artificial_intelligence
# wikipedia use any text

data = '''Artificial intelligence (AI) is intelligence demonstrated by machines, as opposed to the natural intelligence displayed by animals including humans. AI research has been defined as the field of study of intelligent agents, which refers to any system that perceives its environment and takes actions that maximize its chance of achieving its goals.[a]

The term "artificial intelligence" had previously been used to describe machines that mimic and display "human" cognitive skills that are associated with the human mind, such as "learning" and "problem-solving". This definition has since been rejected by major AI researchers who now describe AI in terms of rationality and acting rationally, which does not limit how intelligence can be articulated.[b]

AI applications include advanced web search engines (e.g., Google), recommendation systems (used by YouTube, Amazon and Netflix), understanding human speech (such as Siri and Alexa), self-driving cars (e.g., Tesla), automated decision-making and competing at the highest level in strategic game systems (such as chess and Go).[2][citation needed] As machines become increasingly capable, tasks considered to require "intelligence" are often removed from the definition of AI, a phenomenon known as the AI effect.[3] For instance, optical character recognition is frequently excluded from things considered to be AI,[4] having become a routine technology.[5]

Artificial intelligence was founded as an academic discipline in 1956, and in the years since has experienced several waves of optimism,[6][7] followed by disappointment and the loss of funding (known as an "AI winter"),[8][9] followed by new approaches, success and renewed funding.[7][10] AI research has tried and discarded many different approaches since its founding, including simulating the brain, modeling human problem solving, formal logic, large databases of knowledge and imitating animal behavior. In the first decades of the 21st century, highly mathematical-statistical machine learning has dominated the field, and this technique has proved highly successful, helping to solve many challenging problems throughout industry and academia'''


# step 1
# convert text into lower case data
# for uni scale

data = data.lower()
print("\n********************** Converted into a lowercase data *****************************\n\n")
print(data)
print()



# step 2
# clean the data remove punctuation and stopwords
# using re module
# this munction convert data into tokens auto matically 

sw = stopwords.words("english")
sw

def text_cleaning(a):
    
    #cleaning = [char for char in a if char not in string.punctuation]
    clean = []
    for char in a :
        if char not in string.punctuation:
            clean.append(char)
    
    clean_1=''.join(clean)
    
    #cleaning =  [word for word in cleaning.split() if word.lower() not in stopwords.words('english')]
    
    cleaning = []
    for word in clean_1.split():
        if word not in sw:
            cleaning.append(word)
    
    return cleaning


data = text_cleaning(data)
print("\n********************** Clean Data *****************************\n\n")
print(data)
print()



# step 3
# convert the data into bigrams , trigrams


bigrams  = list(nltk.bigrams(data))

tigrams  = list(nltk.trigrams(data))

print("\n*************************************** Bigrams ****************************\n\n")
print(bigrams)
print()

print("\n*************************************** Trigrams ****************************\n\n")
print(tigrams)
print()



# Generate the frequency of ngrams

# step 4

#####    Here you can check the frequency of the word

# checkthe frequency of the words 
# for that we required library 

from nltk.probability import FreqDist

fdist = FreqDist()

#cheking the frequncy of the words

for word in data:
    fdist[word.lower()]+=1

fdist_top50=fdist.most_common(50)
fdist_top50

print("\n*************************************** Frequency of word ****************************\n\n")
print(fdist_top50)
print()

print(type(fdist_top50))

print("\n*************************************** Trigram *****************************************\n\n")
print(list(nltk.trigrams(fdist_top50)))
















