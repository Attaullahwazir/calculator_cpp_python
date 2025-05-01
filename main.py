import ctypes
from struct import calcsize

# Load the shared library
calc = ctypes.CDLL("./calc.so")

# Define the argument and return types ( optional but good practice)

calc.add.argtypes = [ctypes.c_int, ctypes.c_int]
calc.add.restype = ctypes.c_int

calc.subtract.argtypes = [ctypes.c_int, ctypes.c_int]
calc.subtract.restype = ctypes.c_int

calc.multiply.argtypes = [ctypes.c_int, ctypes.c_int]
calc.multiply.restype = ctypes.c_int

calc.divide.argtypes = [ctypes.c_int, ctypes.c_int]
calc.divide.restype = ctypes.c_int

calc.modulo.argtypes = [ctypes.c_int, ctypes.c_int]
calc.modulo.restype = ctypes.c_int

calc.square.argtypes = [ctypes.c_int, ctypes.c_int]
calc.square.restype = ctypes.c_int


def main():
  print("==== Simple C++ & Python Calculator ====")

  a = int(input("Enter Frist number: "))
  b = int(input("Enter Second number: "))

  print("Choose an Operation: ")
  print(
      "1. Addition\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulo\n6. Square")
  choice = int(input("Enter Choice: "))
  if choice == 1:
    result = calc.add(a, b)
    print(f"The result of {a} + {b} is {result}")
  elif choice == 2:
    result = calc.subtract(a, b)
    print(f"The result of {a} - {b} is {result} ")
  elif choice == 3:
    result = calc.multiply(a, b)
    print(f"The result of {a} - {b} is {result} ")
  elif choice == 4:
    result = calc.divide(a, b)
    print(f"The result of {a} - {b} is {result} ")
  elif choice == 5:
    result = calc.modulo(a, b)
    print(f"The result of {a} % {b} is {result} ")

  elif choice == 2:
    result = calc.square(a, b)
    print(f"The result of {a} ** {b} is {result} ")
  else:
    print("Invalid Choice")


if __name__ == "__main__":
  main()
