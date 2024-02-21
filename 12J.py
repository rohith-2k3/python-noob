# num = 122
# reverse_number = 0
# print("Given Number ", num)
# while num > 0:
#     reminder = num % 10
#     reverse_number = (reverse_number * 10) + reminder
#     num = num // 10
# print("Revere Number ", reverse_number)

#conditions
# 1.
# x=0
# while x<10:
#     x+=1
#     if x%2==0:
#         print(x,"is even.")
#         continue
#     print(x,"is odd.")

# text = input("Enter a text: ")

# reversed_text = ""
# for i in range(len(text) - 1, -2, -1):  # Reverse the text character by character
#     print(text[i])
#     reversed_text += text[i]
# print(reversed_text)

#loops
# x=50
# for i in range(1,x+1):
#     for j in range(1,11):
#         r=i*j
#         print("{}x{}={}".format(i,j,r))
#     print("{} table is ended".format(i))

#==>Patterns
# for i in range(1,7):
#     for j in range(1,i):
#         print("*",end=" ")
#     print("")

# num_rows = 5

# for i in range(num_rows):
#     for j in range(num_rows):
#         if i == 0 or i == num_rows - 1 or j == 4-i:
#             print('*', end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# x=0
# y=1
# counter=0
# while counter!=15:
#     print(x,end=" ")
#     x,y=y,x+y
#     counter+=1
# prime or not until limit
# x=100
# for i in range(2,x+1):
#     for j in range(2,i):
#         if i%j==0:
#             print("{} is not prime because is multiplication of {}x{}".format(i,j,i//j))
#             break
#     else:
#         print("{}is prime".format(i))
# x=101// particular no
# for i in range(2,int(x//2)+1):
#     if x%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")
# Take user input for the number of rows and columns
# num_rows = int(input("Enter the number of rows: "))
# num_cols = int(input("Enter the number of columns: "))

# # Initialize an empty matrix
# matrix = []

# # Take user input for each element of the matrix
# for i in range(num_rows):
#     row = []
#     for j in range(num_cols):
#         element = int(input(f"Enter element at position ({i+1}, {j+1}): "))
#         row.append(element)
#     matrix.append(row)


# # Print the matrix
# print(matrix)
# for row in matrix:
#     for element in row:
#         print(element, end=' ')
#     print()

# m1=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]
# m2=[
#     [3,4,5],
#     [6,7,8],
#     [7,8,9]
# ]
# def mm(m1,m2):
#     r1,c1=len(m1),len(m1[0])
#     r2,c2=len(m2),len(m2[0])

#     if c1!=r2:
#         print("not possible")
#         return None
    
#     result = [[0] * c2 for i in range(r1)]
#     for i in range(m1):
#         for j in range(c2):
#             for k in range(c1):
#                 result[i][j]+=m1[i][k]*m2[k][j]
#     return result
# print(mm(m1,m2))

# rows=int(input("1st m row"))
# columns=int(input("1st m col"))
# ro=int(input("2nd m row"))
# c=int(input("2nd m col"))
# m1=[]
# for i in range(rows):
#     r=[]
#     for j in range(columns):
#         e=int(input(f"enter the number ({i+1,j+1}): "))
#         r.append(e)
#     m1.append(r)
# print("matrix 1:",m1)
# m2=[]
# for i in range(ro):
#     r=[]
#     for j in range(c):
#         e=int(input(f"enter the number ({i+1,j+1}): "))
#         r.append(e)
#     m2.append(r)
# print("matrix 2:",m2)

# r1,c1=len(m1),len(m1[0])
# r2,c2=len(m2),len(m2[0])
# result=[[0]*c1 for i in range(r2)]
# for i in range(r1):
#     for j in range(c1):
#         for k in range(c2):
#             result[i][j]+=m1[i][k]*m2[k][j]
# for i in result:
#     print(i,end="\n")

# for i in range(5):
#     for j in range(5):
#         print("*",end="")
#     print("")
# r=2
# for i in range(1,10):
#     if i<6:
#         for j in range(i):
#             print("*",end="")
#     else:
#         for k in range(i-r,0,-1):
#             print("*",end="")
#         r+=2
#     print("")
# x=4
# for i in range(1,x+2):
#     space=(" ")*x
#     print(space,end="")
#     for j in range(i):
#         print("*",end="")
#     x-=1
#     print()
# for i in range(5,0,-1):
#     stars="*" *i
#     space=" "*(5-i)
#     print(space+stars)

# rows = 5

# for i in range(1, rows + 1):
#     spaces = "h" * (rows - i)
#     stars = "*" * (2 * i - 1)
#     print(spaces + stars)
# for i in range(1,rows+1):
#     space=(" ")*(rows-i)
#     print(space,end="")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# r = 5
# for i in range(1,r+1):
#     for j in range(1, 2*r):
#         if i >= 1 and (j == r - i + 1 or j == r + i - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# r = 5
# for i in range(r,0,-1):
#     for j in range(1, 2*r):
#         if i >= 1 and (j == r - i + 1 or j == r + i - 1):
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()
# rows = 5

# for i in range(rows):
#     # Print leading spaces
#     for j in range(rows - i - 1):
#         print(" ", end="")

#     # Initialize coef for the current row
#     coef = 1

#     # Calculate and print the values in each row
#     for j in range(i + 1):
#         print(coef, end=" ")

#         # Update coef for the next value
#         coef = coef * (i - j) // (j + 1)

#     print()

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
print(fac(4))
