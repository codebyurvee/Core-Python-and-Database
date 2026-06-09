#1. The Walrus Operator :=
# Instead of calculating len() twice:
# if len(data) > 5: print(len(data))

if (n := len([1, 2, 3, 4, 5, 6])) > 5:
    print(f"List is too long with {n} elements")

#. Matrix Multiplication Operator (@)
# Used with libraries like NumPy or custom classes
# matrix_c = matrix_a @ matrix_b

#3. Bitwise Operators
a & b #and
a | b #or
a ^ b #xor
~a    #not 
a >> b #left shift
a << b #right shift



