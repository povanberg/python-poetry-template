import pypoetry_template.math

if __name__ == "__main__":

    a: float = 10.0
    b: float = 3.5

    res = pypoetry_template.math.mul(a, b)

    print("Simple product: ")
    print(f"{a} x {b} = {res}")
