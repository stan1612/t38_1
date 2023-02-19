import spacy
nlp = spacy.load('en_core_web_md') 
# In "sm" mode i got a UserWarning: [W007] stating that model which I am using has no word vevtors loaded and it may give not useful similarity judgements
# example 1
word1 = nlp("apple")
word2 = nlp("iPhone")
word3 = nlp("kiwi")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
# the interesting bit about this is that it knows that monkeys do like bananas and cats don't and level of similarity 
# example 2
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
# example 3
sentence_to_compare ="Why is my cat on the car"
sentences = ["where did my dog go","Hello, there is my car","I\'ve lost my car in my car","I\'d like my boat back","I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence +" - ",similarity)