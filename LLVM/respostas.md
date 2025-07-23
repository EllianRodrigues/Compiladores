# Respostas — Atividade LLVM IR

## 2. Código C e Geração de IR

### a) Como estão representadas as funções `soma`, `multiplica` e `calcula` em IR?
No LLVM IR, cada função do C é representada por um bloco iniciado por `define`, seguido do tipo de retorno e dos parâmetros explicitamente tipados. Por exemplo:

```llvm
define dso_local i32 @soma(i32 %a, i32 %b) {
entry:
  %add = add nsw i32 %a, %b
  ret i32 %add
}
```
- O nome da função aparece após o `@`.
- Os parâmetros são nomeados como `%a`, `%b` e possuem tipo explícito (`i32` para `int`).
- O corpo da função é composto por instruções LLVM, como `add` (adição) e `ret` (retorno).
- O mesmo padrão se repete para `multiplica` e `calcula`, mudando apenas o nome e as operações internas.

### b) O que aparece no IR que representa a condição `if (valor > 10)`?
A condição é representada por duas instruções principais:
- `icmp sgt i32 %valor, 10`: faz a comparação se `%valor` é maior que 10 (signed greater than).
- `br i1 %cmp, label %if.then, label %if.else`: faz o desvio condicional para o bloco correto dependendo do resultado da comparação.

Exemplo:
```llvm
%cmp = icmp sgt i32 %valor, 10
br i1 %cmp, label %if.then, label %if.else
```

### c) Como são representadas as chamadas às funções auxiliares em IR?
As chamadas de função aparecem como instruções `call`, especificando o tipo de retorno, o nome da função e os argumentos:

```llvm
%call = call i32 @multiplica(i32 %valor, i32 2)
```
- O resultado da chamada pode ser armazenado em uma variável temporária (`%call`).
- O mesmo ocorre para chamadas à função `soma`.

--- 

## 3. Modificação do Código (`operacoes_mod.c` e `operacoes_mod.ll`)

### a) Como o `if (temp % 2 == 0)` aparece no IR?
- O operador `%` é representado por `srem` (signed remainder), que calcula o resto da divisão inteira.
- A comparação com zero é feita por `icmp eq`.
- O desvio condicional é feito por `br`.

Exemplo:
```llvm
%rem = srem i32 %temp, 2
%cmp = icmp eq i32 %rem, 0
br i1 %cmp, label %if.then, label %if.else
```

### b) Como o operador `%` (módulo) é representado no LLVM IR?
- Pelo comando `srem` (signed remainder), usado para inteiros com sinal.

### c) Quais são os blocos básicos criados pela nova lógica condicional?
- Cada bloco básico começa com um rótulo, como `entry:`, `if.then:`, `if.else:`, `if.end:`.
- A lógica condicional cria pelo menos três blocos básicos: um para o início, um para o caso verdadeiro, um para o caso falso e um para o final.
- Cada bloco contém uma sequência de instruções sem desvios internos.

--- 

## 4. Otimização com `opt` (`operacoes_opt.ll`)

### a) Que mudanças ocorreram na função `main` após a otimização?
- O código da função `main` ficou mais compacto, com remoção de variáveis intermediárias e simplificação de instruções.
- O otimizadoreliminou as atribuições desnecessárias e reorganizar o fluxo para melhorar a performance.

### b) Alguma função foi *inlined*? Como identificar?
- Sim, funções pequenas como `calcula`, `soma` ou `multiplica` podem ser "inlined" (coladas no lugar da chamada).
- Para identificar, observe se o corpo da função aparece diretamente dentro da função chamadora e se a instrução `call` desaparece do IR.
- Se não houver mais chamada explícita (`call`) para a função, e as operações aparecem diretamente, a função foi inlined.

### c) Alguma variável intermediária foi eliminada? Por quê?
- Sim, variáveis temporárias que não são necessárias podem ser removidas pelo otimizador para simplificar o código e melhorar a performance.
- Isso ocorre porque o LLVM faz análise de uso e elimina variáveis que podem ser substituídas diretamente pelo valor calculado.

--- 

## 5. Grafo de Fluxo de Controle (CFG) (não consegui criar os grafos, vou supor apenas :(((   )

### a) Quantos blocos básicos você consegue identificar na função `calcula`?
- Normalmente, pelo menos quatro: bloco de entrada (`entry`), bloco do `if` verdadeiro (`if.then`), bloco do `if` falso (`if.else`) e bloco final (`if.end`).
- Se houver retornos antecipados (como em funções auxiliares), pode haver blocos extras.

### b) Quais são os caminhos possíveis a partir da condição `if (temp % 2 == 0)`?
- Dois caminhos principais: um para o caso em que a condição é verdadeira (`if.then`), levando à multiplicação, e outro para o caso falso (`if.else`), levando à divisão.
- Cada caminho executa operações diferentes e termina no bloco final.

### c) O fluxo de controle inclui blocos de erro ou casos não triviais (e.g., retorno precoce)?
- Sim, por exemplo, na função `divide`, há um retorno precoce se `y == 0`, criando um bloco de saída antecipada.
- Isso é representado no CFG como um bloco que termina com um `ret` sem passar pelo bloco final.

### d) Há blocos com apenas instruções de salto? O que isso indica?
- Sim, blocos que apenas redirecionam o fluxo (`br`) são comuns para organizar o controle e facilitar otimizações.
- Isso indica pontos de decisão (como após uma comparação) ou junção de caminhos (merge) no fluxo do programa.

--- 