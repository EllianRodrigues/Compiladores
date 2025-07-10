# Justificativa de Modelagem da AST

## Elementos Representados na AST

### Classes Principais
- **Program**: Representa o programa completo, contendo a classe principal e uma lista de outras classes
- **MainClass**: Representa a classe principal com seu nome
- **ClassDecl**: Representa uma declaração de classe com nome, herança opcional, variáveis e métodos
- **VarDecl**: Representa uma declaração de variável com tipo e nome
- **MethodDecl**: Representa uma declaração de método com tipo de retorno, nome e parâmetros
- **Type**: Representa tipos da linguagem (primitivos, classes ou arrays)

### Herança na AST
Utilizei herança através da classe base `ASTNode` para:
- **Uniformidade**: Todos os nós da AST compartilham uma interface comum
- **Polimorfismo**: Permite tratar diferentes tipos de nós de forma uniforme
- **Extensibilidade**: Facilita adicionar funcionalidades comuns a todos os nós

## Elementos Omitidos

### Símbolos Sintáticos
- **Chaves `{}`**: Omitidas pois são apenas delimitadores sintáticos
- **Ponto e vírgula `;`**: Omitidos pois são apenas terminadores de declaração
- **Parênteses `()`**: Omitidos pois são apenas delimitadores de parâmetros
- **Palavras-chave**: `class`, `public`, `static`, `extends` são omitidas pois são implícitas na estrutura

### Justificativa das Omissões
A AST deve capturar apenas a **estrutura semântica** do programa, não sua representação sintática. Símbolos como chaves e ponto e vírgula não carregam informação semântica relevante.

## Representação de Listas e Elementos Opcionais

### Listas
- **Classes**: Representadas como `List[ClassDecl]` no `Program`
- **Variáveis**: Representadas como `List[VarDecl]` no `ClassDecl`
- **Métodos**: Representadas como `List[MethodDecl]` no `ClassDecl`
- **Parâmetros**: Representados como `List[VarDecl]` no `MethodDecl`

### Elementos Opcionais
- **Herança**: Representada como `Optional[str]` no `ClassDecl` (None quando não há herança)
- **Dimensões de Array**: Representadas como `int` no `Type` (0 para tipos não-array)

## Dificuldades Encontradas

### 1. Representação do Método Main
O método `main` da classe principal não está explicitamente representado na AST, pois a gramática o define como fixo. Isso simplifica a modelagem, mas pode ser uma limitação se quisermos representar outros métodos na classe principal.

### 2. Arrays
A representação de arrays através de `array_dimensions` é simples mas funcional. Uma alternativa seria usar uma estrutura recursiva `ArrayType(Type)`, mas a abordagem atual é mais direta.

### 3. Tipos Primitivos vs Classes
Todos os tipos são representados pela mesma classe `Type`, diferenciando apenas pelo `base_type`. Isso simplifica a modelagem, mas poderia ser mais específico com classes separadas para tipos primitivos.

## Vantagens da Modelagem Escolhida

1. **Simplicidade**: Estrutura clara e fácil de entender
2. **Extensibilidade**: Fácil adicionar novos tipos de nós
3. **Consistência**: Padrão uniforme para todos os elementos
4. **Eficiência**: Representação compacta sem redundância

## Exemplo de Uso

A AST criada representa fielmente o programa de exemplo:
- Classe `Main` como classe principal
- Classe `Point` com duas variáveis `int` (`x` e `y`)
- Estrutura hierárquica clara e navegável