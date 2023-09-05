###  Assignment No 1 ###
#Name : Sandhya Govind Nikale
#Batch : B3
#Roll No : 42
#Assignment Title : Text pre-processing using NLP operation : perform Tokenization
#Stop word removal, Punctuation removal,using Spacy or NLTK Library 

#import library
 
import spacy
nlp=spacy.load("en_core_web_sm")
from collections import Counter

print("\n##########   Sentence Detection    ###############\n")
#Sentence Detection

text1=("My name is Sandhya "
       "I am the student of Information-technology"
       "My college name is Sanjivani College of Engineering, Kopargaon")

about_doc=nlp(text1)
sentences=list(about_doc.sents)
len(sentences)

for sentence in sentences:
    print(f"{sentence[:5]}...")
print("\n#############       Tokenization         ###############\n")

#tokenization

for token in about_doc:
    print(token,token.idx)
print("\n###############           Stop Words Removal       ###############\n")

#stop words removal

spacy_stopwords=spacy.lang.en.stop_words.STOP_WORDS
len(spacy_stopwords)
print()
for stop_word in list(spacy_stopwords)[:15]:
    print(stop_word)

print([token for token in about_doc if not token.is_stop])

print("\n###############          Lemmatization            ###############\n")

for token in about_doc:
    if str(token)!= str(token.lemma_):
        print(f"{str(token):>20}:{str(token.lemma_)}")

print("\n###############           Word Frequency       ###############\n")

words=[
    token.text
    for token in about_doc
    if not token.is_stop and not token.is_punct
]
print(Counter(words).most_common(5))

print("\n###############           Part_of_speech Tagging       ###############\n")

for token in about_doc:
    print(
        f"""
        TOKEN:{str(token)}
        =====
        TAG: {str(token.tag_):10} POS: {token.pos_}
        EXPLANATION: {spacy.explain(token.tag_)}"""
    )
"""
##########   Sentence Detection    ###############

My name is Sandhya I...

#############       Tokenization         ###############

My 0
name 3
is 8
Sandhya 11
I 19
am 21
the 24
student 28
of 36
Information 39
- 50
technologyMy 51
college 64
name 72
is 77
Sanjivani 80
College 90
of 98
Engineering 101
, 112
Kopargaon 114

###############           Stop Words Removal       ###############


beyond
own
have
back
n't
as
third
any
‘m
otherwise
however
anyhow
an
’ve
no
[Sandhya, student, Information, -, technologyMy, college, Sanjivani, College, Engineering, ,, Kopargaon]

###############          Lemmatization            ###############

                  My:my
                  is:be
                  am:be
                  is:be

###############           Word Frequency       ###############

[('Sandhya', 1), ('student', 1), ('Information', 1), ('technologyMy', 1), ('college', 1)]

###############           Part_of_speech Tagging       ###############


        TOKEN:My
        =====
        TAG: PRP$       POS: PRON
        EXPLANATION: pronoun, possessive

        TOKEN:name
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:is
        =====
        TAG: VBZ        POS: AUX
        EXPLANATION: verb, 3rd person singular present

        TOKEN:Sandhya
        =====
        TAG: NNP        POS: PROPN
        EXPLANATION: noun, proper singular

        TOKEN:I
        =====
        TAG: PRP        POS: PRON
        EXPLANATION: pronoun, personal

        TOKEN:am
        =====
        TAG: VBP        POS: AUX
        EXPLANATION: verb, non-3rd person singular present

        TOKEN:the
        =====
        TAG: DT         POS: DET
        EXPLANATION: determiner

        TOKEN:student
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:of
        =====
        TAG: IN         POS: ADP
        EXPLANATION: conjunction, subordinating or preposition

        TOKEN:Information
        =====
        TAG: NNP        POS: PROPN
        EXPLANATION: noun, proper singular

        TOKEN:-
        =====
        TAG: HYPH       POS: PUNCT
        EXPLANATION: punctuation mark, hyphen

        TOKEN:technologyMy
        =====
        TAG: NNP        POS: PROPN
        EXPLANATION: noun, proper singular

        TOKEN:college
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:name
        =====
        TAG: NN         POS: NOUN
        EXPLANATION: noun, singular or mass

        TOKEN:is
        =====
        TAG: VBZ        POS: AUX
        EXPLANATION: verb, 3rd person singular present

        TOKEN:Sanjivani
        =====
        TAG: NNP        POS: PROPN
        EXPLANATION: noun, proper singular

        TOKEN:College
        =====
        TAG: NNP        POS: PROPN
        EXPLANATION: noun, proper singular

        TOKEN:of
        =====
        TAG: IN         POS: ADP
        EXPLANATION: conjunction, subordinating or preposition

        TOKEN:Engineering
        =====
        TAG: NNP        POS: PROPN
        EXPLANATION: noun, proper singular

        TOKEN:,
        =====
        TAG: ,          POS: PUNCT
        EXPLANATION: punctuation mark, comma

        TOKEN:Kopargaon
        =====
        TAG: NNP        POS: PROPN
        EXPLANATION: noun, proper singular
        """