from socket import *

def calculate(expression):

    expression = expression.replace(" ", "")

    for op in "+-*/":
        if op in expression:
            num1, num2 = expression.split(op)
            try:
                num1, num2 = int(num1), int(num2)
            except ValueError:
                return "Error: Invalid Expression"

            if op == '+':
                return str(num1 + num2)
            elif op == '-':
                return str(num1 - num2)
            elif op == '*':
                return str(num1 * num2)
            elif op == '/':
                if num2 == 0:
                    return "Error: Division by zero"
                return f"{num1 / num2:.1f}"

    return "Error: Unsupported Operator"

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9002))
s.listen(5)
print("Waiting...")

while True:
    client, addr = s.accept()
    print("Connection from:", addr)

    while True:
        data = client.recv(1024).decode()
        if not data:
            break

        result = calculate(data)
        client.send(result.encode())

    client.close()
