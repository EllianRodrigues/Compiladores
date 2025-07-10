## IF688 – Teoria e Implementação de Linguagens Computacionais

### Atividade – Modelagem de uma AST em Python para MiniJava

Este exercício tem como objetivo exercitar a **modelagem de uma Árvore de Sintaxe Abstrata (AST)** em Python para um subconjunto da linguagem MiniJava, com base na mesma gramática utilizada na Atividade 3 (*recursive-descent parsing*).

A ideia é representar a estrutura lógica dos programas, capturando apenas os elementos **essenciais e semânticos**, ignorando detalhes puramente sintáticos.

### **Gramática de Referência**

A gramática abaixo define um subconjunto da linguagem MiniJava, conforme já visto na atividade anterior:

```ebnf
Program ::= MainClass Classes
MainClass ::= "class" <IDENTIFIER> "{" "public static void main(String[] a) { System.out.println(); } }"
Classes ::= ClassDecl Classes | ϵ
ClassDecl ::= "class" <IDENTIFIER> ClassA
ClassA ::= "extends" <IDENTIFIER> "{" ClassB | "{" ClassB
ClassB ::=  "}"
          | "static" VarDecl ClassB
          | VarDecl ClassB
          | "public" MethodDecl ClassC
ClassC ::=  "}"
          | "public" MethodDecl ClassC
VarDecl ::= Type <IDENTIFIER> ";"
MethodDecl ::= Type <IDENTIFIER> "(" MethodA
MethodA ::= ")" "{" "}"
          | Type <IDENTIFIER> MethodB
MethodB ::= ")" "{" "}"
          | "," Type <IDENTIFIER> MethodB
Type ::= SimpleType ArrayPart
SimpleType ::= "boolean"
          | "float"
          | "int"
          | <IDENTIFIER>
ArrayPart ::= ϵ
          | "[" "]" ArrayPart
```

### **Atividade a ser realizada**

Você deverá:

1. **Projetar uma estrutura de classes Python** para representar a AST da linguagem MiniJava, com base na gramática acima.

   * Utilize uma classe por entidade relevante da linguagem (ex: `Program`, `MainClass`, `ClassDecl`, etc.).
   * Decida o que deve ou não ser representado na AST. Por exemplo, símbolos como `{` e `;` podem ser omitidos.
   * O mecanismo de herança pode ser usado se fizer sentido.

2. **Instanciar manualmente uma AST** para o seguinte programa MiniJava de exemplo:

```java
class Main {
    public static void main(String[] a) {
        System.out.println();
    }
}

class Point {
    int x;
    int y;
}
```

3. **Escrever um pequeno texto** comentando as decisões de modelagem que foram tomadas.

   * O que você optou por representar ou omitir?
   * Como modelou listas, herança e elementos opcionais?
   * Houve dificuldades de representar alguma parte da gramática?

### **Entrega**

Você deverá entregar **três arquivos**:

* `astminijava.py`: sua implementação das classes da AST.
* `sample_program.py`: uma instância manual da AST representando o programa de exemplo.
* `justificativa.txt` ou `justificativa.md`: um pequeno texto (até 1 página) explicando suas decisões de modelagem.


## ATENÇÃO!

* O foco está na clareza da modelagem e na sua capacidade de justificar as escolhas feitas.
* Não é necessário implementar parsing, apenas a estrutura da AST e sua instanciação manual. Se desejar implementar um _parser_, vide sugestão abaixo.

### Atividade Opcional (Integração com a Atividade 3)
Se desejar ir além, você pode estender o parser construído na Atividade 3 de forma que ele, ao invés de apenas aceitar ou rejeitar o programa de entrada, construa e retorne uma instância da AST utilizando as classes desenvolvidas nesta atividade. Essa integração é opcional, mas altamente recomendada para quem deseja reforçar o entendimento do papel do parser como etapa de construção da representação interna do programa como AST.