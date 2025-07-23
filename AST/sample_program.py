"""
sample_program.py

Este arquivo deve conter a criação manual de uma instância da AST
para o programa MiniJava de exemplo fornecido no enunciado da atividade.
"""

from astminijava import *

# Criando a AST para o programa de exemplo:
# class Main {
#     public static void main(String[] a) {
#         System.out.println();
#     }
# }
# 
# class Point {
#     int x;
#     int y;
# }

# Definindo tipos
int_type = Type("int")
string_type = Type("String")
void_type = Type("void")

# Criando a classe principal (Main)
main_class = MainClass("Main")

# Criando a classe Point
# Variáveis da classe Point
x_var = VarDecl(int_type, "x")
y_var = VarDecl(int_type, "y")

# Classe Point (sem herança, com duas variáveis int, sem métodos)
point_class = ClassDecl(
    name="Point",
    extends=None,  # Não herda de nenhuma classe
    var_decls=[x_var, y_var],
    method_decls=[]  # Sem métodos
)

# Criando o programa completo
program = Program(
    main_class=main_class,
    classes=[point_class]
)

# Função para imprimir a estrutura da AST
def print_ast(node, indent=0):
    """Função auxiliar para imprimir a estrutura da AST"""
    print(" " * indent + type(node).__name__)
    
    if isinstance(node, Program):
        print_ast(node.main_class, indent + 2)
        for cls in node.classes:
            print_ast(cls, indent + 2)
    elif isinstance(node, MainClass):
        print(" " * (indent + 2) + f"name: {node.name}")
    elif isinstance(node, ClassDecl):
        print(" " * (indent + 2) + f"name: {node.name}")
        if node.extends:
            print(" " * (indent + 2) + f"extends: {node.extends}")
        for var in node.var_decls:
            print_ast(var, indent + 4)
        for method in node.method_decls:
            print_ast(method, indent + 4)
    elif isinstance(node, VarDecl):
        print(" " * (indent + 2) + f"type: {node.var_type.base_type}, name: {node.name}")
    elif isinstance(node, MethodDecl):
        print(" " * (indent + 2) + f"return_type: {node.return_type.base_type}, name: {node.name}")
        for param in node.params:
            print_ast(param, indent + 4)

if __name__ == "__main__":
    print("Estrutura da AST para o programa de exemplo:")
    print_ast(program)