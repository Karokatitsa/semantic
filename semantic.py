# importing spacy
import spacy

# specifying the model we want to use. Remember to install this model by typing 
# python -m spacy download en_core_web_md into your command line
nlp = spacy.load('en_core_web_md')


# example 1
print("\nexample 1\n----------------------------------------------------")
# Variables with spacy objects 
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

# Outputing similarity between two words
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))


#-------------------NOTICE------------------------------
'''
interesting inferences about the similarity in the output above! 
To point out a couple of things:
● Cat and monkey seem to be similar because they are both animals;
● Similarly, banana and apple are similar because they are both fruits;
● Interestingly, monkey and banana have a higher similarity than monkey and
apple. So we can assume that the model already puts together that
monkeys eat bananas and that is why there is a significant similarity.'''



# example 2
print("\nexample 2\n----------------------------------------------------")
# use two for loops to allow us to undertake a comparison of the words.
# First compare one word (token1) to all the other ‘tokens’ in the string, and then
# do the same for the next word (token2) and repeat the cycle.
# Then print the similarity between words in sentence
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
        
#-------------------NOTICE------------------------------
'''
interesting inferences about the similarity in the output above! 
To point out a couple of things:      
● Interesting fact is that cat does not have any significant similarity
with any of the fruits although monkey does. So, the model does not
explicitly seem to recognise transitive relationships in its calculation.'''


#example 3
print("\nexample 3\n----------------------------------------------------")
# Exeple sentence and list of sentences for compare
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

# Loop for compare our sentence with each sentence in list.
# Then print the similarity between between our sentence and sentences in list
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


# My own example
print("\nMy example\n----------------------------------------------------")
# Variables with spacy objects 
word1 = nlp("car")
word2 = nlp("engine")
word3 = nlp("tree")

# Outputing similarity between two words
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

print()

#-------------------NOTICE------------------------------
'''
when we use model`en_core_web_sm`,
we get a warning message: 
"UserWarning: [W007] The model you're using has no word vectors loaded, 
so the result of the Doc.similarity method will be based on the tagger, parser, 
and NER, which may not give useful similarity judgments. This may happen if 
you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with 
word vectors and only use context-sensitive tensors. You can always add your own 
word vectors, or use one of the larger models instead if available"
That means while using model`en_core_web_md` similarities will be much more 
accurate than `en_core_web_sm`.
'''

