###  Assignment No 2 ###
#Name : Sandhya Govind Nikale
#Batch : B3
#Roll No : 42
#Assignment Title : Assignment to implement Bag of Words and TFIDF using Gensim library.
import gensim
from gensim import corpora,models
from gensim.utils import simple_preprocess


#text2 = open('sample_text.txt', encoding='utf-8')

text2 = ["""I came into your class", "To learn and to grow", "But, what has touched me most",
   "is the love you have shown"""]

tokens2 = []
# for line in text2.read().split('.'):
for line in text2[0].split('.'):
    tokens2.append(simple_preprocess(line, deacc=True))

g_dict2 = corpora.Dictionary(tokens2)

print("The dictionary has: " + str(len(g_dict2)) + " tokens")
print(g_dict2.token2id)
print("\n")

g_bow =[g_dict2.doc2bow(token, allow_update = True) for token in tokens2]
print("Bag of Words : ", g_bow)

text = ["""I came into your class", "To learn and to grow", "But, what has touched me most",
   "is the love you have shown"""]
g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])

g_tfidf = models.TfidfModel(g_bow, smartirs='ntc')

print("\n TF-IDF Vector:")
for item in g_tfidf[g_bow]:
    print([[g_dict[id], np.around(freq, decimals=2)] for id, freq in item])

''' 
######### Bag Of Words ##########
The dictionary has: 13 tokens
{'and': 0, 'gave': 1, 'joy': 2, 'kind': 3, 'me': 4, 'mind': 5, 'of': 6, 'peace': 7, 're': 8, 'so': 9, 'teacher': 10, 'thank': 11, 'you': 12}


Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 3)]]

########### TFIDF ##########

Dictionary : 
[['and', 1], ['gave', 1], ['joy', 1], ['kind', 1], ['me', 1], ['mind', 1], ['of', 1], ['peace', 1], ['re', 1], ['so', 1], ['teacher', 1], ['thank', 1], ['you', 3]]

########## TF-IDF Vector ########

 TF-IDF Vector:
[['and', 0.22], ['gave', 0.22], ['joy', 0.22], ['kind', 0.22], ['me', 0.22], ['mind', 0.22], ['of', 0.22], ['peace', 0.22], ['re', 0.22], ['so', 0.22], ['teacher', 0.22], ['thank', 0.22], ['you', 0.65]]
'''
