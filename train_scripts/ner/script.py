import json
import random
import os
from spacy.training import Example

current_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_path, "data.json")


def train_ner(nlp):
    # Cria um componente NER em branco
    ner = nlp.add_pipe("ner")

    labels = ["DIRECTOR", "AUTHORS", "RELEASED", "GENDER"]

    # Adiciona os rotulos ao componente
    for label in labels:
        ner.add_label(label)

    # Faz a leitura do arquivo JSON onde se encontra os dados de treinamento
    file = open(file_path, "r", encoding='utf-8')
    train_data = json.load(file)["annotations"]

    # Transforma as entidades dos dados de treinamento em tuplas
    for i in train_data:
        entities = []
        for m in i[1]["entities"]:
            entities.append(tuple(m))
            i[1]["entities"] = entities

    # Épocas(loop) para treinar o modelo (NER Component)
    epochs = 30

    # Percorre os componentes desabilitando e deixando apenas o componente NER para ser treinado
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']

    with nlp.disable_pipes(*other_pipes):

        # Inicializa os pesos do modelo NER para 0 (Modelo esquece tudo o que sabe)
        optimizer = nlp.begin_training()

        for i in range(epochs):
            random.shuffle(train_data)

            # Obtem os dados de treinamento do arquivo JSON
            for text, annotation in train_data:
                # Cria um objeto DOC
                doc = nlp.make_doc(text.lower())

                # Cria um exemplo com os dados de treinamento
                example = Example.from_dict(doc, annotation)

                # Atualiza o modelo com os exemplos de treinamento usando o algoritmo SGD (Stochastic Gradient Descent)
                nlp.update([example], sgd=optimizer)
