import argparse

parser = argparse.ArgumentParser(description="UNITS CONVERSOR")

parser.add_argument("--type", choices=["km-mi", "mi-km", "c-f", "f-c"],
                    required=True, help='CONVERT "km-mi","mi-km","c-f","f-c"')

parser.add_argument("value", type=float, help="Units you want to convert")

args = parser.parse_args()

print("Hello, this is UNITS CONVERSOR")

def km_to_mi(km): return km * 0.621371
def mi_to_km(mi): return mi / 0.621371
def c_to_f(c): return (c * 9/5) + 32
def f_to_c(f): return (f - 32) * 5/9

if args.type == "km-mi":
    print(f"{args.value} km = {km_to_mi(args.value):.2f} mi")
elif args.type == "mi-km":
    print(f"{args.value} mi = {mi_to_km(args.value):.2f} km")
elif args.type == "c-f":
    print(f"{args.value} °C = {c_to_f(args.value):.2f} °F")
elif args.type == "f-c":
    print(f"{args.value} °F = {f_to_c(args.value):.2f} °C")
