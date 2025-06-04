### Como Usar

Para colocar o interpretador em funcionamento, siga estes passos:

#### 1. Usando o Modo Interativo (`main_user.py`)

Para interagir diretamente com o interpretador, digitando comandos um por um:

* **Execute:**
    ```bash
    python main_user.py
    ```

* **Exemplo de Interação:**
    ```
    >>> x = 10
    >>> y = x + 5
    >>> y 
    >>> Resultado: 15
    >>> y * 2
    Resultado: 30
    >>> 4 + 2
    Resultado: 6
    ```

#### 1. Usando o Modo de Arquivo (`main.py`)

Para processar uma sequência de comandos definidos em um arquivo de texto:

1.  **Crie ou atualize o arquivo `input.txt`** com as expressões e atribuições que você deseja que o interpretador processe.

    **Exemplo de `input.txt`:**
    ```
    # Testes básicos de operações aritméticas
    4+2
    4*4
    2/2

    # Testes com variáveis e atribuições
    x=10
    y = x + 3
    y*2
    ```

2.  **Execute:**
    ```bash
    python main.py
    ```
    O programa lerá e executará cada linha do `input.txt`, exibindo os resultados das expressões no terminal.