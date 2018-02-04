from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize
from nltk.misc import babelfish
from nltk.util import skipgrams


text1=gutenberg.raw("bible-kjv.txt")
text2=gutenberg.raw("shakespeare-caesar.txt")
#print(text2)
text3=sent_tokenize(text2,'english')
text4=text3[0:2]
print("text3")
print(text3)
#text4=text3[:1]
#print(text[1:5])]
##print(text3[1:5])
#print(sent_tokenize(text1)[1:15])
print("text4")
print(text4)
str1=""
for v in text4:
    str1=str1.join(v)
print(list(skipgrams(str1.split(),2,2)))
















