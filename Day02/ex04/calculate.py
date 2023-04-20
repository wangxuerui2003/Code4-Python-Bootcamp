def calculate(n1: int, op: str, n2: int):
    if op == '+':
        return (n1 + n2)
    elif op == '-':
        return (n1 - n2)
    elif op == '*':
        return (n1 * n2)
    elif op == '/':
        return (n1 / n2)
    
print(calculate(10,'+',10))
print(calculate(10,'-',10))
print(calculate(10,'*',10))
print(calculate(10,'/',10))
    