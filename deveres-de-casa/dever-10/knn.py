"""
Dever 10 - Algoritmo K-NN

Objetivo:
Aplicar o algoritmo K-NN ao dataset Breast Cancer Wisconsin,
comparando diferentes valores de K e métricas de distância.

"""

import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


class AnaliseKNN:
    """Executa análise utilizando K-NN."""

    def __init__(self):
        self.dataset = load_breast_cancer()
        self.X = self.dataset.data
        self.y = self.dataset.target

    def preparar_dados(self):
        """Separa treino/teste e normaliza."""

        X_treino, X_teste, y_treino, y_teste = train_test_split(
            self.X,
            self.y,
            test_size=0.2,
            random_state=42
        )

        scaler = StandardScaler()

        X_treino = scaler.fit_transform(X_treino)
        X_teste = scaler.transform(X_teste)

        return X_treino, X_teste, y_treino, y_teste

    def executar(self):

        X_treino, X_teste, y_treino, y_teste = (
            self.preparar_dados()
        )

        resultados = []

        valores_k = [1, 3, 5]
        metricas = ["euclidean", "manhattan"]

        print("Quantidade de registros:",
              self.X.shape[0])

        print("Quantidade de atributos:",
              self.X.shape[1])

        for metrica in metricas:

            print("\n======================")
            print("Distância:", metrica)
            print("======================")

            for k in valores_k:

                modelo = KNeighborsClassifier(
                    n_neighbors=k,
                    metric=metrica
                )

                modelo.fit(
                    X_treino,
                    y_treino
                )

                previsoes = modelo.predict(
                    X_teste
                )

                acuracia = accuracy_score(
                    y_teste,
                    previsoes
                )

                resultados.append(
                    [k, metrica, acuracia]
                )

                print(f"\nK = {k}")
                print(
                    f"Acurácia: {acuracia:.4f}"
                )

                print(
                    confusion_matrix(
                        y_teste,
                        previsoes
                    )
                )

                print(
                    classification_report(
                        y_teste,
                        previsoes
                    )
                )

        tabela = pd.DataFrame(
            resultados,
            columns=[
                "K",
                "Métrica",
                "Acurácia"
            ]
        )

        melhor = tabela.loc[
            tabela["Acurácia"].idxmax()
        ]

        print("\nRESULTADOS")
        print(tabela)

        print("\nMELHOR")
        print(melhor)


def main():
    """Executa programa."""

    analise = AnaliseKNN()
    analise.executar()


if __name__ == "__main__":
    main()