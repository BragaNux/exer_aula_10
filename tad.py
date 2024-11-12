class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerdo = None
        self.direito = None

class ABB:
    def __init__(self):
        self.raiz = None

    def inserir(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir(self.raiz, valor)

    def _inserir(self, no, valor):
        if valor < no.valor:
            if no.esquerdo is None:
                no.esquerdo = No(valor)
            else:
                self._inserir(no.esquerdo, valor)
        else:
            if no.direito is None:
                no.direito = No(valor)
            else:
                self._inserir(no.direito, valor)

    def pre_ordem(self, no):
        if no:
            print(no.valor, end=" ")
            self.pre_ordem(no.esquerdo)
            self.pre_ordem(no.direito)

    def buscar(self, valor):
        return self._buscar(self.raiz, valor)

    def _buscar(self, no, valor):
        if no is None or no.valor == valor:
            return no
        if valor < no.valor:
            return self._buscar(no.esquerdo, valor)
        return self._buscar(no.direito, valor)

    def deletar(self, valor):
        self.raiz = self._deletar(self.raiz, valor)

    def _deletar(self, no, valor):
        if no is None:
            return no
        if valor < no.valor:
            no.esquerdo = self._deletar(no.esquerdo, valor)
        elif valor > no.valor:
            no.direito = self._deletar(no.direito, valor)
        else:
            if no.esquerdo is None:
                return no.direito
            if no.direito is None:
                return no.esquerdo
            substituto = self._minimo_valor(no.direito)
            no.valor = substituto.valor
            no.direito = self._deletar(no.direito, substituto.valor)
        return no

    def _minimo_valor(self, no):
        atual = no
        while atual.esquerdo:
            atual = atual.esquerdo
        return atual

if __name__ == "__main__":
    arvore = ABB()
    valores = [20, 10, 30, 5, 15, 25, 35]

    for valor in valores:
        arvore.inserir(valor)

    print("Pré-ordem:")
    arvore.pre_ordem(arvore.raiz)

    print("\n\nBuscando o valor 15:")
    resultado = arvore.buscar(15)
    print("Encontrado!" if resultado else "Não encontrado.")

    print("\nDeletando o valor 20:")
    arvore.deletar(20)

    print("Pré-ordem após deleção:")
    arvore.pre_ordem(arvore.raiz)
