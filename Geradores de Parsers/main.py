from antlr4 import *
from ArithmeticLexer import ArithmeticLexer
from ArithmeticParser import ArithmeticParser
from collections import defaultdict 

class ArithmeticVisitor:
    def __init__(self):
        self.variables = defaultdict(int) 

    def visit(self, ctx):
        if isinstance(ctx, ArithmeticParser.ProgramContext):
            return self.visitProgram(ctx)
        elif isinstance(ctx, ArithmeticParser.StatementContext):
            return self.visitStatement(ctx)
        elif isinstance(ctx, ArithmeticParser.AssignmentContext):
            return self.visitAssignment(ctx)
        elif isinstance(ctx, ArithmeticParser.ExprContext):
            return self.visitExpr(ctx)
        elif isinstance(ctx, ArithmeticParser.TermContext):
            return self.visitTerm(ctx)
        elif isinstance(ctx, ArithmeticParser.FactorContext):
            return self.visitFactor(ctx)
        else:
            return self.visitChildren(ctx)

    def visitChildren(self, ctx):
        
        result = None
        for child in ctx.children:
            result = self.visit(child)
        return result

    def visitProgram(self, ctx: ArithmeticParser.ProgramContext):
        last_result = None
        for statement_ctx in ctx.statement():
            last_result = self.visit(statement_ctx)
        return last_result

    def visitStatement(self, ctx: ArithmeticParser.StatementContext):
        if ctx.assignment():
            return self.visit(ctx.assignment())
        elif ctx.expr():
            return self.visit(ctx.expr())

    def visitAssignment(self, ctx: ArithmeticParser.AssignmentContext):
        var_name = ctx.VAR().getText()
        value = self.visit(ctx.expr())
        self.variables[var_name] = value
        return None 

    def visitExpr(self, ctx: ArithmeticParser.ExprContext):
        result = self.visit(ctx.term(0))
        for i in range(1, len(ctx.term())):
            op = ctx.getChild(i * 2 - 1).getText()
            if op == '+':
                result += self.visit(ctx.term(i))
            else:
                result -= self.visit(ctx.term(i))
        return result

    def visitTerm(self, ctx: ArithmeticParser.TermContext):
        result = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            op = ctx.getChild(i * 2 - 1).getText()
            if op == '*':
                result *= self.visit(ctx.factor(i))
            else: 
                divisor = self.visit(ctx.factor(i))
                if divisor == 0:
                    raise ZeroDivisionError("Divisão por zero!")
                result /= divisor
        return result

    def visitFactor(self, ctx: ArithmeticParser.FactorContext):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.VAR():
            var_name = ctx.VAR().getText()
            if var_name not in self.variables:  
                pass 
            return self.variables[var_name]
        else: 
            return self.visit(ctx.expr())

def main():
    visitor = ArithmeticVisitor()

    while True:
        try:
            expression = input(">>> ")

            lexer = ArithmeticLexer(InputStream(expression))
            stream = CommonTokenStream(lexer)
            parser = ArithmeticParser(stream)

            tree = parser.program() 

            if parser.getNumberOfSyntaxErrors() > 0:
                print("Erro de sintaxe!")
                continue

            result = visitor.visit(tree)

            if result is not None:
                print("Resultado:", result)

        except Exception as e:
            print(f"Erro: {e}")

if __name__ == '__main__':
    main()