## Tipos de Árvores

### 1. Árvore Rubro-Negra (Red-Black Tree)

- **O que é**: Uma árvore binária de busca balanceada.
- **Para que serve**: Garante operações eficientes de busca, inserção e deleção com complexidade O(log n), mesmo em casos de dados desbalanceados.
- **Como funciona**:
  - Cada nó é vermelho ou preto.
  - A raiz da árvore é sempre preta.
  - Nós vermelhos não podem ter filhos vermelhos.
  - Todos os caminhos da raiz até uma folha têm o mesmo número de nós pretos.
  - Após inserções ou deleções, são realizadas rotações e recolorimentos para manter o balanceamento.

---

### 2. Árvore B

- **O que é**: Uma árvore balanceada que pode ter múltiplos filhos, projetada para armazenar grandes volumes de dados.
- **Para que serve**: Comumente utilizada em sistemas de arquivos e bancos de dados, garantindo operações eficientes de leitura e escrita.
- **Como funciona**:
  - Cada nó pode armazenar várias chaves e ter múltiplos filhos.
  - Mantém a altura da árvore baixa, reduzindo o número de acessos ao disco.
  - Operações de inserção e deleção reorganizam os nós para manter o balanceamento.

---

### 3. Árvore B+

- **O que é**: Uma variação da Árvore B, otimizada para consultas sequenciais e range queries.
- **Para que serve**: Amplamente utilizada em bancos de dados para acesso rápido e ordenado aos registros.
- **Como funciona**:
  - Os dados são armazenados apenas nos nós folha.
  - Os nós folha estão ligados entre si por ponteiros, facilitando percursos sequenciais.
  - Os nós internos armazenam apenas as chaves para navegação rápida durante a busca.

---
