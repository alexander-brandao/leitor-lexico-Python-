"""
Spyder Editor

This is a temporary script file.
""" 

# Alexander Costa Brandao ra: 21709858
# Lucas Xerfan            ra: 21601914
# Murilo Augusto          ra: 21654310
# Rodrigo Rollo           ra: 21750924


import sys

class Lista:
     def __init__(self):
         self.items = []
     def isEmpty(self):
         return self.items == []
     def push(self, item):
         self.items.append(item)
     def pop(self):
         return self.items.pop()
     def peek(self):
         return self.items[self.size()-1]
     def size(self):
         return len(self.items) 
class Executar:
    def __init__(self):
        self.Lista = Lista()
        self.precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}
    def hasLessOrEqualPriority(self, a, b):
        if a not in self.precedence:
            return False
        if b not in self.precedence:
            return False
        return self.precedence[a] <= self.precedence[b]
    def isOperator(self, x):
        ops = ['+', '-', '/', '*']
        return x in ops
    def isOperand(self, ch):
        return ch.isalpha() or ch.isdigit()
    def isOpenParenthesis(self, ch):
        return ch == '('
    def isCloseParenthesis(self, ch):
        return ch == ')'
    def toPostfix(self, expr):
        expr = expr.replace(" ", "")
        self.Lista = Lista()
        output = ''
        for c in expr:
            if self.isOperand(c):
                output += c
            else:
                if self.isOpenParenthesis(c):
                    self.Lista.push(c)
                elif self.isCloseParenthesis(c):
                    operator = self.Lista.pop()
                    while not self.isOpenParenthesis(operator):
                        output += operator
                        operator = self.Lista.pop()              
                else:
                    while (not self.Lista.isEmpty()) and self.hasLessOrEqualPriority(c,self.Lista.peek()):
                        output += self.Lista.pop()
                    self.Lista.push(c)

        while (not self.Lista.isEmpty()):
            output += self.Lista.pop()
        return output
    
    def convert(self, expr):
        try:
            result = eval(expr);
        except:
            result = expr
        print ("""
            Expressão original: {}
            Posfixa: {}
        """.format(expr, self.toPostfix(expr)))

def main(argv):
    infix = Executar()
    while True:
        infix_expression = input("Digite uma expressão infixa ou ""sair"": ")
        if (infix_expression.lower() == 'sair'):
            break
        infix.convert(infix_expression)


if __name__ == "__main__":
    main(sys.argv)
