from spacy.training import Example
from spacy.pipeline.textcat import DEFAULT_SINGLE_TEXTCAT_MODEL
import random
import json
import os

current_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_path, "data.json")


def train_textcat(nlp):
    config = {
        "threshold": 0.5,
        "model": DEFAULT_SINGLE_TEXTCAT_MODEL
    }

    # Cria um componente NER em branco
    textcat = nlp.add_pipe("textcat", config=config)

    # Adiciona os rotulos ao componente
    labels = ["RANDOM_MOVIE", "DIRECTOR_NAME"]

    # Adiciona os rotulos ao componente
    for label in labels:
        textcat.add_label(label)

    # Faz a leitura do arquivo JSON onde se encontra os dados de treinamento
    file = open(file_path, "r", encoding='utf-8')
    train_data = json.load(file)

    train_examples = [Example.from_dict(nlp.make_doc(text), label) for text, label in train_data]

    textcat.initialize(lambda: train_examples, nlp=nlp)

    # Épocas(loop) para treinar o modelo (TextCat Component)
    epochs = 30

    with nlp.select_pipes(enable="textcat"):
        # Inicializa os pesos do modelo TextCat para 0 (Modelo esquece tudo o que sabe)
        optimizer = nlp.begin_training()

        for i in range(epochs):
            random.shuffle(train_data)
            for text, label in train_data:
                # Cria um objeto DOC
                doc = nlp.make_doc(text)

                # Cria um exemplo com os dados de treinamento
                example = Example.from_dict(doc, label)

                # Atualiza o modelo com os exemplos de treinamento usando o algoritmo SGD (Stochastic Gradient Descent)
                nlp.update([example], sgd=optimizer)
