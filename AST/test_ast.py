"""
test_ast.py

Arquivo de teste para validar a implementação da AST de MiniJava
"""

from astminijava import *
from sample_program import program, print_ast

def test_basic_structure():
    """Testa a estrutura básica da AST"""
    print("=== Teste 1: Estrutura Básica ===")
    
    # Verifica se o programa tem a estrutura correta
    assert isinstance(program, Program), "program deve ser uma instância de Program"
    assert isinstance(program.main_class, MainClass), "main_class deve ser uma instância de MainClass"
    assert isinstance(program.classes, list), "classes deve ser uma lista"
    
    print("✓ Estrutura básica está correta")

def test_main_class():
    """Testa a classe principal"""
    print("\n=== Teste 2: Classe Principal ===")
    
    assert program.main_class.name == "Main", f"Esperado 'Main', obtido '{program.main_class.name}'"
    print(f"✓ Classe principal: {program.main_class.name}")

def test_point_class():
    """Testa a classe Point"""
    print("\n=== Teste 3: Classe Point ===")
    
    assert len(program.classes) == 1, f"Esperado 1 classe, obtido {len(program.classes)}"
    
    point_class = program.classes[0]
    assert isinstance(point_class, ClassDecl), "point_class deve ser uma instância de ClassDecl"
    assert point_class.name == "Point", f"Esperado 'Point', obtido '{point_class.name}'"
    assert point_class.extends is None, "Point não deve herdar de nenhuma classe"
    
    print(f"✓ Classe: {point_class.name}")
    print(f"✓ Herança: {point_class.extends}")
    
    # Testa as variáveis
    assert len(point_class.var_decls) == 2, f"Esperado 2 variáveis, obtido {len(point_class.var_decls)}"
    
    var_names = [var.name for var in point_class.var_decls]
    assert "x" in var_names, "Variável 'x' não encontrada"
    assert "y" in var_names, "Variável 'y' não encontrada"
    
    for var in point_class.var_decls:
        assert isinstance(var.var_type, Type), f"Tipo de {var.name} deve ser Type"
        assert var.var_type.base_type == "int", f"Tipo de {var.name} deve ser 'int'"
        print(f"✓ Variável: {var.var_type.base_type} {var.name}")

def test_types():
    """Testa a criação de diferentes tipos"""
    print("\n=== Teste 4: Tipos ===")
    
    # Testa tipos primitivos
    int_type = Type("int")
    float_type = Type("float")
    boolean_type = Type("boolean")
    string_type = Type("String")
    
    assert int_type.base_type == "int"
    assert int_type.array_dimensions == 0
    print("✓ Tipo int criado corretamente")
    
    # Testa arrays
    int_array = Type("int", 1)
    int_matrix = Type("int", 2)
    
    assert int_array.array_dimensions == 1
    assert int_matrix.array_dimensions == 2
    print("✓ Arrays criados corretamente")

def test_class_with_inheritance():
    """Testa uma classe com herança"""
    print("\n=== Teste 5: Classe com Herança ===")
    
    # Cria uma classe que herda de Point
    colored_point = ClassDecl(
        name="ColoredPoint",
        extends="Point",
        var_decls=[VarDecl(Type("int"), "color")],
        method_decls=[]
    )
    
    assert colored_point.name == "ColoredPoint"
    assert colored_point.extends == "Point"
    assert len(colored_point.var_decls) == 1
    assert colored_point.var_decls[0].name == "color"
    
    print(f"✓ Classe {colored_point.name} herda de {colored_point.extends}")

def test_method_declaration():
    """Testa declaração de método"""
    print("\n=== Teste 6: Declaração de Método ===")
    
    # Cria um método simples
    method = MethodDecl(
        return_type=Type("int"),
        name="getX",
        params=[]
    )
    
    assert method.return_type.base_type == "int"
    assert method.name == "getX"
    assert len(method.params) == 0
    
    print(f"✓ Método {method.name} retorna {method.return_type.base_type}")
    
    # Cria um método com parâmetros
    method_with_params = MethodDecl(
        return_type=Type("void"),
        name="setPosition",
        params=[
            VarDecl(Type("int"), "newX"),
            VarDecl(Type("int"), "newY")
        ]
    )
    
    assert len(method_with_params.params) == 2
    assert method_with_params.params[0].name == "newX"
    assert method_with_params.params[1].name == "newY"
    
    print(f"✓ Método {method_with_params.name} com {len(method_with_params.params)} parâmetros")

def test_complex_program():
    """Testa um programa mais complexo"""
    print("\n=== Teste 7: Programa Complexo ===")
    
    # Cria um programa com múltiplas classes
    complex_program = Program(
        main_class=MainClass("Game"),
        classes=[
            ClassDecl("Player", None, 
                     [VarDecl(Type("int"), "score")], 
                     [MethodDecl(Type("void"), "move", [])]),
            ClassDecl("Enemy", "GameObject", 
                     [VarDecl(Type("boolean"), "isActive")], 
                     [])
        ]
    )
    
    assert len(complex_program.classes) == 2
    assert complex_program.classes[0].name == "Player"
    assert complex_program.classes[1].name == "Enemy"
    assert complex_program.classes[1].extends == "GameObject"
    
    print("✓ Programa complexo criado com sucesso")
    print("  - Classe Player sem herança")
    print("  - Classe Enemy herda de GameObject")

def run_all_tests():
    """Executa todos os testes"""
    print("Iniciando testes da AST de MiniJava\n")
    
    try:
        test_basic_structure()
        test_main_class()
        test_point_class()
        test_types()
        test_class_with_inheritance()
        test_method_declaration()
        test_complex_program()
        
        print("\nTodos os testes passaram com sucesso!")
        print("\nResumo da AST criada:")
        print_ast(program)
        
    except AssertionError as e:
        print(f"\nTeste falhou: {e}")
    except Exception as e:
        print(f"\nErro inesperado: {e}")

if __name__ == "__main__":
    run_all_tests() 