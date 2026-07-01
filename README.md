# 🔔 Bip de Senha - Fast Food (Estrutura de Dados: Pilha / Stack)

Aplicação em **Python + Streamlit** que simula o funcionamento dos **bips de
senha** utilizados em redes de fast food (ex: **Giraffas**) para controlar a
entrega de pedidos, usando a estrutura de dados **Pilha (Stack)**, que segue
o princípio **LIFO — Last In, First Out**.

## 📖 Cenário

Em restaurantes fast food, os bips ficam empilhados em uma **torre**, um em
cima do outro. Quando o caixa finaliza o atendimento de um pedido, o
**próximo bip** — ou seja, o que está no **topo da torre** — é vinculado ao
pedido, retirado da torre e entregue ao cliente. Esse comportamento é
exatamente o de uma pilha: o último bip colocado na torre é o primeiro a
ser retirado.

## ⚙️ Funcionalidades

| Funcionalidade         | Operação de pilha correspondente | Descrição                                                                 |
|-------------------------|-----------------------------------|-----------------------------------------------------------------------------|
| ➕ Adicionar bip        | `push` (empilhar)                 | Coloca um bip no topo da torre (bip novo ou devolvido por um cliente).      |
| ➖ Retirar bip          | `pop` (desempilhar)               | Remove o bip do topo, vincula a um pedido e entrega ao cliente.             |
| 👁️ Mostrar bip atual    | `peek` (consultar topo)           | Mostra qual é o próximo bip a ser entregue, sem removê-lo da torre.         |

A aplicação também mantém um **histórico de pedidos entregues** e uma
**visualização gráfica da torre de bips**, do topo até a base.

## 🧠 Estrutura de dados utilizada

A pilha foi implementada na classe `PilhaDeBips` (arquivo `app.py`), usando
uma `list` do Python como estrutura interna, com as operações clássicas de
pilha:

```python
class PilhaDeBips:
    def empilhar(self, bip):      # push
        ...
    def desempilhar(self):        # pop
        ...
    def topo(self):               # peek
        ...
    def esta_vazia(self):
        ...
```

## ▶️ Como executar

1. Clone o repositório:
   ```bash
   git clone <url-do-repositorio>
   cd bip-fastfood-stack
   ```

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

4. Execute a aplicação:
   ```bash
   streamlit run app.py
   ```

5. Acesse no navegador o endereço indicado no terminal (geralmente
   `http://localhost:8501`).

## 📁 Estrutura do projeto

```
bip-fastfood-stack/
├── app.py              # Aplicação Streamlit + implementação da Pilha (Stack)
├── requirements.txt     # Dependências do projeto
└── README.md            # Este arquivo
```

## 🤖 Prompts utilizados para criar a solução

Esta seção documenta os prompts (instruções) utilizados para gerar esta
solução com auxílio de IA, conforme solicitado.

### Prompt principal

> Crie uma solução em python, juntamente com a biblioteca streamlit. Dentro
> do github deve ter o arquivo README com os prompts utilizados para criar
> solução da seguinte situação: Bip de senha em um restaurante fast food.
> Cenário: os bips são utilizados como espécie de senha para os pedidos.
> Eles são colocados em torres, um em cima do outro. Assim que o caixa
> completa o atendimento o próximo bip é vinculado ao pedido e retirado da
> torre e entregue ao cliente. Exemplo: Giraffas. Funcionalidades: adicionar
> bip, retirar bip, mostrar bip atual. Dentro da estrutura de dados em
> pilha stack (LAST IN, FIRST OUT).

### Requisitos extraídos do prompt

- Linguagem: **Python**
- Interface: **Streamlit**
- Estrutura de dados obrigatória: **Pilha (Stack) — LIFO**
- Funcionalidades obrigatórias:
  - Adicionar bip (push)
  - Retirar bip (pop)
  - Mostrar bip atual (peek)
- Contexto de negócio: fluxo de atendimento de pedidos em fast food
  (bips empilhados em uma torre física), com exemplo de referência
  (Giraffas)
- Entregável: repositório com `README.md` documentando os prompts usados

### Decisões de implementação (a partir do prompt)

- A classe `PilhaDeBips` foi criada isoladamente da interface para deixar
  clara a estrutura de dados (pilha pura em Python, usando `list.append` /
  `list.pop`), separando regra de negócio da camada visual do Streamlit.
- O estado da pilha é mantido em `st.session_state` para persistir os bips
  entre as interações do usuário na interface web (o Streamlit reexecuta o
  script a cada interação).
- Foi adicionada uma visualização da torre (topo → base) para reforçar
  visualmente o comportamento LIFO, além de um histórico de pedidos já
  atendidos.
- A funcionalidade "Adicionar bip" contempla dois casos de uso reais de um
  fast food: (1) devolução de um bip por um cliente que já foi atendido
  (retorna ao topo da torre) e (2) cadastro de um bip novo sequencial.

## 📌 Observações

- Este projeto tem fins didáticos, com foco em demonstrar a aplicação
  prática da estrutura de dados **Pilha (Stack)** em um cenário do
  mundo real.
