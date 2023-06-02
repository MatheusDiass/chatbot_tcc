import spacy
from textcat.script import train_textcat
from ner.script import train_ner

def train_components():
    nlp = spacy.blank("pt")

    # Realiza o treinamento do componente textcat (Classificação de Texto)
    train_textcat(nlp)

    # Realiza o treinamento do componente NER (Reconhecimento Entidade Nomeada)
    train_ner(nlp)

    # Salva os modelos treinados para uso em outros scripts python
    nlp.to_disk("./train.spacy")


train_components()
