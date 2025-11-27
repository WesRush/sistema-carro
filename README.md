# 🚗 Sistema de Cadastro de Carros

## 📝 Descrição do Projeto

Este projeto é um sistema simples de cadastro e gerenciamento de carros desenvolvido em **Python**. O objetivo principal é a aplicação prática dos conceitos de **Programação Orientada a Objetos (POO)**: **Classes**, **Métodos**, **Herança** e **Encapsulamento**.

O sistema utiliza arquivos **JSON** para armazenar e recuperar os dados de forma persistente. A complexidade da manipulação do JSON é tratada pela classe base, permitindo que a classe `Carro` se concentre apenas em seus atributos, demonstrando **Abstração**.

---

## ✨ Conceitos de POO Demonstrados

| Conceito | Aplicação |
| :--- | :--- |
| **Classes e Objetos** | As classes `BaseModel` e `Carro` definem a estrutura, e a criação de instâncias (ex: `carro = Carro(...)`) gera os objetos. |
| **Herança** | A classe **`Carro` herda** de **`BaseModel`** (Ex: `class Carro(BaseModel):`), ganhando automaticamente métodos de I/O (`salvar()`, `carregar_todos()`, `excluir_registro()`). |
| **Encapsulamento** | Os atributos da classe `Carro` (ex: `self.__marca`) são definidos como **privados** (iniciados com `__`), sendo acessados e modificados apenas por **Getters** e **Setters**. |
| **Abstração** | A classe `Carro` chama `super().salvar(dados)` sem precisar conhecer a lógica interna de manipulação do JSON, focando apenas *o que* fazer (salvar) e não *como* fazer. |

---

---

## ⚙️ Como Executar a Aplicação

### Pré-requisitos
* **Python 3.x** instalado.
* As bibliotecas `json` e `os` são nativas do Python, então **não é necessário instalar pacotes adicionais**.

### Passos de Execução
1. Garanta que a estrutura de pastas e arquivos (`main.py` na raiz, `base.py` e `carro.py` dentro de `models/`) está correta.
2. Abra o terminal (ou Prompt de Comando) na pasta raiz do projeto (`sistema_carros/`).
3. Execute o arquivo principal:

    ```bash
    python main.py
    ```

---

## 🔍 Detalhes dos Módulos

### 1. `models/base.py`

Esta classe funciona como uma camada de **Data Access** (Acesso a Dados), abstrata e genérica, que toda classe de modelo pode herdar para obter persistência em JSON.

| Método | Função |
| :--- | :--- |
| `salvar(dados)` | Carrega a lista, adiciona o novo registro e reescreve o arquivo JSON (modo `w`). |
| `carregar_todos()` | Lê o JSON (modo `r`) e o converte em uma lista Python. |
| `excluir_registro(indice)` | Remove um registro específico pelo índice e salva a lista atualizada. |

### 2. `models/carro.py`

Define as propriedades e comportamentos específicos de um carro, mantendo seus dados internos protegidos.

| Componente | Função |
| :--- | :--- |
| **Herança** | Conecta a classe à `BaseModel` para I/O. |
| **Atributos Privados** | Garantem que `__marca`, `__modelo`, e `__ano` sejam acessados e modificados apenas por métodos controlados. |
| **`salvar_carro()`** | Envia os dados do objeto Carro para o método `salvar()` herdado da classe-mãe. |

### 3. `main.py`

Gerencia a experiência do usuário e a integridade dos dados de entrada.

| Funcionalidade | Conceito |
| :--- | :--- |
| **Menus Dinâmicos** | Utiliza o dicionário `MARCAS_E_MODELOS` para apresentar opções de Marca e Modelo por número, garantindo *inputs* válidos. |
| **Validação Simples** | Usa `while True` e métodos de string (`isdigit()`, `len()`) para garantir que o **Ano** seja um valor numérico de 4 dígitos. |
| **Interação POO** | Cria um objeto `Carro` com os dados validados e simplesmente chama `carro.salvar_carro()` para persistir o objeto. |

---
