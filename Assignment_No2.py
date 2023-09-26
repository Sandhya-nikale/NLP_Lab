###  Assignment No 2 ###
#Name : Sandhya Govind Nikale
#Batch : B3
#Roll No : 42
#Assignment Title : Assignment to implement Bag of Words and TFIDF using Gensim library.
import gensim
from gensim import corpora
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

###OUTPUT###
'''
Output for Bag of words:
The dictionary has: 20 tokens
{'and': 0, 'but': 1, 'came': 2, 'class': 3, 'grow': 4, 'has': 5, 'have': 6, 'into': 7, 'is': 8, 'learn': 9, 'love': 10, 'me': 11, 'most': 12, 'shown': 13, 'the': 14, 'to': 15, 'touched': 16, 'what': 17, 'you': 18, 'your': 19}
Bag of Words :  [[(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1), (9, 1), (10, 1), (11, 1), (12, 1), (13, 1), (14, 1), (15, 2), (16, 1), (17, 1), (18, 1), (19, 1)]]

Output for TFIDF:
Dictionary : 
[['and', 1], ['but', 1], ['came', 1], ['class', 1], ['grow', 1], ['has', 1], ['have', 1], ['into', 1], ['is', 1], ['learn', 1], ['love', 1], ['me', 1], ['most', 1], ['shown', 1], ['the', 1], ['to', 2], ['touched', 1], ['what', 1], ['you', 1], ['your', 1]]
'''