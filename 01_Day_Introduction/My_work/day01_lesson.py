# Day 1 lesson file by Samuel

# 1. Printing text and numbers
print("Hello, Python")
print("I am learning Python")
print(2026)

# 2. Arithmetic operators
print(3 + 2)    # addition: 5
print(3 - 2)    # subtraction: 1
print(3 * 2)    # multiplication: 6
print(3 / 2)    # division: 1.5
print(3 ** 2)   # exponent: 9
print(3 % 2)    # modulus (remainder): 1
print(3 // 2)   # floor division: 1

# 3. Order of operations
print(5 + 3 * 2)     # 11, multiplication goes first
print((5 + 3) * 2)   # 16, brackets go first

# 4. Data types
print(type(10))                    # int
print(type(3.14))                  # float
print(type(1 + 3j))                # complex
print(type("Hello"))               # str
print(type([1, 2, 3]))             # list
print(type({"name": "Samuel"}))    # dict
print(type((9.8, 3.14, 2.7)))      # tuple
print(type({9.8, 3.14, 2.7}))      # set

# 5. The one item tuple trap
print(type((5)))     # int
print(type((5,)))    # tuple

# 6. Variables
name = "Samuel"
print("Hello,", name)
print(type(name))