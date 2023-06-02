import spacy
nlp = spacy.load("./train.spacy")

while True:
    user_input = input("O que gostaria de saber: ")
    doc = nlp(user_input)

    print(doc.cats)