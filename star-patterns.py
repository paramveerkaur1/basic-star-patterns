# pyramid building character unit
unit = '*'

print("Creating lower triangular star pattern:")
rows=int(input("Enter number of rows:"))
res=''
print("Pattern Output:")
# using each for loop iteration to display one line of pattern
for i in range(rows):
    # generating a string with star count equal to row number
    # creates lower triangular star pattern automatically as output is left aligned  
    res= unit*(i+1)
    print(res)
       
               
print("Creating upper triangular star pattern:")
rows=int(input("Enter number of rows:"))
res=''
print("Pattern Output:")
# using each for loop iteration to display one line of pattern
# creating reverse loop with index starting from no of rows and decreasing by 1
for i in range(rows, 0, -1):
    # generating a string with star count equal to index
    res = unit*i
    print(res)
    

print("Creating pyramid star pattern:")
rows=int(input("Enter number of rows:"))
res=''
space=" "
# using each for loop iteration to display one line of pattern
print("Pattern Output:")
for i in range(rows):
    # generating a string starting with spaces
    res= space*(rows-i-1)
    # appending stars to the string containing spaces
    res += unit*(2*i+1)
    print(res)
