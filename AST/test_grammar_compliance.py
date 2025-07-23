"""
test_grammar_compliance.py

Teste específico para validar se a AST está em conformidade com a gramática fornecida
"""

from astminijava import *

def test_grammar_compliance():
    """Testa se a AST está em conformidade com a gramática fornecida"""
    print("Testando conformidade com a gramática...\n")
    
    # Teste 1: Program ::= MainClass Classes
    print("=== Teste: Program ::= MainClass Classes ===")
    program = Program(
        main_class=MainClass("TestMain"),
        classes=[]
    )
    assert isinstance(program.main_class, MainClass)
    assert isinstance(program.classes, list)
    print("✓ Program contém MainClass e Classes")
    
    # Teste 2: MainClass ::= "class" <IDENTIFIER> "{" "public static void main(String[] a) { System.out.println(); } }"
    print("\n=== Teste: MainClass ===")
    main_class = MainClass("TestMain")
    assert isinstance(main_class.name, str)
    print(f"✓ MainClass com nome: {main_class.name}")
    
    # Teste 3: ClassDecl ::= "class" <IDENTIFIER> ClassA
    print("\n=== Teste: ClassDecl ===")
    class_decl = ClassDecl("TestClass", None, [], [])
    assert isinstance(class_decl.name, str)
    assert class_decl.extends is None or isinstance(class_decl.extends, str)
    print(f"✓ ClassDecl: {class_decl.name}")
    
    # Teste 4: ClassA ::= "extends" <IDENTIFIER> "{" ClassB | "{" ClassB
    print("\n=== Teste: ClassA (herança) ===")
    class_with_extends = ClassDecl("ChildClass", "ParentClass", [], [])
    assert class_with_extends.extends == "ParentClass"
    print(f"✓ Classe herda de: {class_with_extends.extends}")
    
    # Teste 5: ClassB ::= "}" | "static" VarDecl ClassB | VarDecl ClassB | "public" MethodDecl ClassC
    print("\n=== Teste: ClassB (variáveis e métodos) ===")
    class_with_vars = ClassDecl("TestClass", None, 
                               [VarDecl(Type("int"), "x")], [])
    assert len(class_with_vars.var_decls) > 0
    print(f"✓ Classe com {len(class_with_vars.var_decls)} variável(is)")
    
    class_with_methods = ClassDecl("TestClass", None, [],
                                  [MethodDecl(Type("void"), "test", [])])
    assert len(class_with_methods.method_decls) > 0
    print(f"✓ Classe com {len(class_with_methods.method_decls)} método(s)")
    
    # Teste 6: VarDecl ::= Type <IDENTIFIER> ";"
    print("\n=== Teste: VarDecl ===")
    var_decl = VarDecl(Type("int"), "testVar")
    assert isinstance(var_decl.var_type, Type)
    assert isinstance(var_decl.name, str)
    print(f"✓ VarDecl: {var_decl.var_type.base_type} {var_decl.name}")
    
    # Teste 7: MethodDecl ::= Type <IDENTIFIER> "(" MethodA
    print("\n=== Teste: MethodDecl ===")
    method_decl = MethodDecl(Type("int"), "testMethod", [])
    assert isinstance(method_decl.return_type, Type)
    assert isinstance(method_decl.name, str)
    assert isinstance(method_decl.params, list)
    print(f"✓ MethodDecl: {method_decl.return_type.base_type} {method_decl.name}()")
    
    # Teste 8: MethodA ::= ")" "{" "}" | Type <IDENTIFIER> MethodB
    print("\n=== Teste: MethodA (parâmetros) ===")
    method_with_params = MethodDecl(Type("void"), "testMethod",
                                   [VarDecl(Type("int"), "param1")])
    assert len(method_with_params.params) > 0
    print(f"✓ Método com {len(method_with_params.params)} parâmetro(s)")
    
    # Teste 9: MethodB ::= ")" "{" "}" | "," Type <IDENTIFIER> MethodB
    print("\n=== Teste: MethodB (múltiplos parâmetros) ===")
    method_multi_params = MethodDecl(Type("void"), "testMethod", [
        VarDecl(Type("int"), "param1"),
        VarDecl(Type("float"), "param2"),
        VarDecl(Type("boolean"), "param3")
    ])
    assert len(method_multi_params.params) == 3
    print(f"✓ Método com {len(method_multi_params.params)} parâmetros")
    
    # Teste 10: Type ::= SimpleType ArrayPart
    print("\n=== Teste: Type ===")
    simple_type = Type("int")
    array_type = Type("int", 1)
    multi_array_type = Type("float", 2)
    
    assert simple_type.array_dimensions == 0
    assert array_type.array_dimensions == 1
    assert multi_array_type.array_dimensions == 2
    
    print(f"✓ Tipo simples: {simple_type.base_type}")
    print(f"✓ Array 1D: {array_type.base_type}[]")
    print(f"✓ Array 2D: {multi_array_type.base_type}[][]")
    
    # Teste 11: SimpleType ::= "boolean" | "float" | "int" | <IDENTIFIER>
    print("\n=== Teste: SimpleType ===")
    boolean_type = Type("boolean")
    float_type = Type("float")
    int_type = Type("int")
    class_type = Type("MyClass")
    
    assert boolean_type.base_type == "boolean"
    assert float_type.base_type == "float"
    assert int_type.base_type == "int"
    assert class_type.base_type == "MyClass"
    
    print("✓ Tipos primitivos: boolean, float, int")
    print("✓ Tipo de classe: MyClass")
    
    # Teste 12: ArrayPart ::= ϵ | "[" "]" ArrayPart
    print("\n=== Teste: ArrayPart ===")
    no_array = Type("int", 0)
    one_dim = Type("int", 1)
    two_dim = Type("int", 2)
    three_dim = Type("int", 3)
    
    assert no_array.array_dimensions == 0
    assert one_dim.array_dimensions == 1
    assert two_dim.array_dimensions == 2
    assert three_dim.array_dimensions == 3
    
    print("✓ Arrays de 0 a 3 dimensões testados")
    
    print("\nTodos os testes de conformidade com a gramática passaram!")
    print("A AST está em conformidade com a gramática fornecida.")

def test_edge_cases():
    """Testa casos extremos e especiais"""
    print("\nTestando casos extremos...\n")
    
    # Teste: Classe vazia
    empty_class = ClassDecl("EmptyClass", None, [], [])
    assert len(empty_class.var_decls) == 0
    assert len(empty_class.method_decls) == 0
    print("✓ Classe vazia criada com sucesso")
    
    # Teste: Método com muitos parâmetros
    many_params = [VarDecl(Type("int"), f"param{i}") for i in range(10)]
    method_many_params = MethodDecl(Type("void"), "complexMethod", many_params)
    assert len(method_many_params.params) == 10
    print(f"✓ Método com {len(method_many_params.params)} parâmetros")
    
    # Teste: Array com muitas dimensões
    big_array = Type("int", 10)
    assert big_array.array_dimensions == 10
    print(f"✓ Array com {big_array.array_dimensions} dimensões")
    
    # Teste: Nome de classe com caracteres especiais (simulado)
    special_class = ClassDecl("My_Class_123", None, [], [])
    assert special_class.name == "My_Class_123"
    print(f"✓ Classe com nome especial: {special_class.name}")
    
    print("\nTodos os casos extremos testados com sucesso!")

if __name__ == "__main__":
    test_grammar_compliance()
    test_edge_cases() 