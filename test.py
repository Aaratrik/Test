import math
expr = None  # dy/dx = f(x, y)

def f(x, y):
    allowed = {"x": x, "y": y, "sin": math.sin, "cos": math.cos, "tan": math.tan,
               "exp": math.exp, "sqrt": math.sqrt, "log": math.log, "pi": math.pi}
    return eval(expr, {"__builtins__": {}}, allowed)


def euler_method(x0, y0, xt, h):
    print("\nEuler's Method: ")
    print("{:<10}{:<15}{:<15}".format("x", "y", "dy/dx"))

    x = x0
    y = y0
    n = int(round((xt - x0) / h))

    print(f"{x:<10.4f}{y:<15.6f}{f(x, y):<15.6f}")

    for i in range(n):
        slope = f(x, y)
        y = y + h * slope
        x = x + h
        print(f"{x:<10.4f}{y:<15.6f}{f(x, y):<15.6f}")

    return y

if __name__ == "__main__":
    expr = input("Enter dy/dx = f(x, y) in terms of x and y, using ** for powers (e.g. x**2 + y): ")

    x0 = float(input("Enter initial x0: "))
    y0 = float(input("Enter initial y0: "))
    xt = float(input("Enter target x: "))
    h = float(input("Enter step size h: "))

    y_final = euler_method(x0, y0, xt, h)

    print(f"\nApproximate y at x = {xt} is y = {y_final:.6f}")