"""
astminijava.py

Este arquivo deve conter a definição das classes que representam a Árvore de Sintaxe Abstrata (AST)
para o subconjunto da linguagem MiniJava definido na Atividade da disciplina IF688.
"""

from typing import List, Optional

class ASTNode:
    """Classe base para todos os nós da AST"""
    pass

# Exemplo de início de modelagem:
class Program(ASTNode):
    """Representa um programa MiniJava completo"""
    def __init__(self, main_class: 'MainClass', classes: List['ClassDecl']):
        self.main_class = main_class
        self.classes = classes

class MainClass(ASTNode):
    """Representa a classe principal do programa"""
    def __init__(self, name: str):
        self.name = name

class ClassDecl(ASTNode):
    """Representa uma declaração de classe"""
    def __init__(self, name: str, extends: Optional[str], var_decls: List['VarDecl'], method_decls: List['MethodDecl']):
        self.name = name
        self.extends = extends  # None se não herda de nenhuma classe
        self.var_decls = var_decls
        self.method_decls = method_decls

class VarDecl(ASTNode):
    """Representa uma declaração de variável"""
    def __init__(self, var_type: 'Type', name: str):
        self.var_type = var_type
        self.name = name

class MethodDecl(ASTNode):
    """Representa uma declaração de método"""
    def __init__(self, return_type: 'Type', name: str, params: List['VarDecl']):
        self.return_type = return_type
        self.name = name
        self.params = params

class Type(ASTNode):
    """Representa um tipo na linguagem"""
    def __init__(self, base_type: str, array_dimensions: int = 0):
        self.base_type = base_type  # "boolean", "float", "int" ou nome de classe
        self.array_dimensions = array_dimensions  # número de dimensões do array
