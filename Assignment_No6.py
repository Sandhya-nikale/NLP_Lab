"""
Assignment No 6
Name - Sandhya Nikale
Batch - B3
Roll No - 42
Assignment Title : Implement and visualize Dependency Parsing of Textual Input using Standford CoreNLP and Spacy library

"""
import spacy
nlp = spacy.load("en_core_web_sm")
multiline_text = """
In whispers of night, stars softly gleam,
Moonbeams dance in a cosmic stream.
Silent symphony, a celestial theme,
Nature's poetry, an eternal dream.
"""

multiline_doc = nlp(multiline_text)

for token in multiline_doc:
    print(
        f"""
TOKEN: {token.text}
=====
{token.tag_ = }
{token.head.text = }
{token.dep_ = }"""
    )

displacy.serve(multiline_doc, style="dep")

#Output 
'''
TOKEN: 

=====
token.tag_ = '_SP'
token.head.text = 'In'
token.dep_ = 'dep'

TOKEN: In
=====
token.tag_ = 'IN'
token.head.text = 'In'
token.dep_ = 'ROOT'

TOKEN: whispers
=====
token.tag_ = 'NNS'
token.head.text = 'In'
token.dep_ = 'pobj'

TOKEN: of
=====
token.tag_ = 'IN'
token.head.text = 'whispers'
token.dep_ = 'prep'

TOKEN: night
=====
token.tag_ = 'NN'
token.head.text = 'of'
token.dep_ = 'pobj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'gleam'
token.dep_ = 'punct'

TOKEN: stars
=====
token.tag_ = 'NNS'
token.head.text = 'gleam'
token.dep_ = 'nsubj'

TOKEN: softly
=====
token.tag_ = 'RB'
token.head.text = 'gleam'
token.dep_ = 'advmod'

TOKEN: gleam
=====
token.tag_ = 'JJ'
token.head.text = 'dance'
token.dep_ = 'amod'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'dance'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = ','
token.dep_ = 'dep'

TOKEN: Moonbeams
=====
token.tag_ = 'NNP'
token.head.text = 'dance'
token.dep_ = 'compound'

TOKEN: dance
=====
token.tag_ = 'NN'
token.head.text = 'In'
token.dep_ = 'pobj'

TOKEN: in
=====
token.tag_ = 'IN'
token.head.text = 'dance'
token.dep_ = 'prep'

TOKEN: a
=====
token.tag_ = 'DT'
token.head.text = 'stream'
token.dep_ = 'det'

TOKEN: cosmic
=====
token.tag_ = 'JJ'
token.head.text = 'stream'
token.dep_ = 'amod'

TOKEN: stream
=====
token.tag_ = 'NN'
token.head.text = 'in'
token.dep_ = 'pobj'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'dance'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = '.'
token.dep_ = 'dep'

TOKEN: Silent
=====
token.tag_ = 'JJ'
token.head.text = 'symphony'
token.dep_ = 'amod'

TOKEN: symphony
=====
token.tag_ = 'NN'
token.head.text = 'symphony'
token.dep_ = 'ROOT'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'symphony'
token.dep_ = 'punct'

TOKEN: a
=====
token.tag_ = 'DT'
token.head.text = 'theme'
token.dep_ = 'det'

TOKEN: celestial
=====
token.tag_ = 'JJ'
token.head.text = 'theme'
token.dep_ = 'amod'

TOKEN: theme
=====
token.tag_ = 'NN'
token.head.text = 'symphony'
token.dep_ = 'appos'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'theme'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = ','
token.dep_ = 'dep'

TOKEN: Nature
=====
token.tag_ = 'NNP'
token.head.text = 'poetry'
token.dep_ = 'poss'

TOKEN: 's
=====
token.tag_ = 'POS'
token.head.text = 'Nature'
token.dep_ = 'case'

TOKEN: poetry
=====
token.tag_ = 'NN'
token.head.text = 'theme'
token.dep_ = 'conj'

TOKEN: ,
=====
token.tag_ = ','
token.head.text = 'poetry'
token.dep_ = 'punct'

TOKEN: an
=====
token.tag_ = 'DT'
token.head.text = 'dream'
token.dep_ = 'det'

TOKEN: eternal
=====
token.tag_ = 'JJ'
token.head.text = 'dream'
token.dep_ = 'amod'

TOKEN: dream
=====
token.tag_ = 'NN'
token.head.text = 'poetry'
token.dep_ = 'appos'

TOKEN: .
=====
token.tag_ = '.'
token.head.text = 'symphony'
token.dep_ = 'punct'

TOKEN:

=====
token.tag_ = '_SP'
token.head.text = '.'
token.dep_ = 'dep'
'''