           # LEARNING TO  MAKE PYRAMID IN PYTHON
#(1)
s=''
for i in range(8):
    s+='*'           #use of asterisk to make pyramid or right aggle triangle 
    print(s)

#(2)
a=''
b=''
for i in range(8):
    a+='*'
    print(a,end='')
    b+='*'      #Two right ange phase each other (Pyramid)
    print(b.rjust(8*2-i))

#(3)
for i in range(8):
    for j in range(i):
        print(i,end='') #1 22 333 4444 55555...THis will be printed in vertically as a Pyramid form
    print()

#(4)
for i in range(8):
    for j in range(1,i+1):
        print(j,end='') #1 12 123 1234 12345...this will be printed in a pyramid form
    print()

print("\n")
#(5)
b=0
for i in range(8,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end='') #b+=1 and print(b,end='') helps to print 11111111 2222222 333333 44444 5555 666 77 8 (inverted pyramid)
    print('\r')       
        
#(6)
for i in range(8,0,-1):  # Eg. rows=8 and num=rows
    for j in range(1,i+1):
        print(8,end='')  #Then #print(num,end=') 
    print()    # 88888888 8888888 888888 88888 8888 888 88 8 (inverted pyramid)

#(7)
for i in range(8,0,-1):
    for j in range(i):  #print(i,end='') =) 55555 4444 333 22 1 (inverted pyramid)
        print(j,end='') #print(j,end='') =) 012345 01234 0123 012 01 0 (inverted pyramid)
    print()
#(8)
for i in range(8):  #if range(8,0,-1) =) out will be...54321 4321 321 21 1
    for j in range(i,0,-1):  # 1 21 321 4321 54321... 
        print(j,end='')
    print()
    
print('\n')
#(9)      
rows = 5
i = 1
while i <= rows:
    j = 1
    while j <= i:
        print((i * 2 - 1), end=" ") #if here only(i-2), the output will be 0 11 22 333 4444..
        j = j + 1
    i = i + 1
    print('')

#(10)
a=1
b=2
c=b
for i in range(2,6):
    for j in range(a,b):
        c-=1
        print(c,end='')
    print()
    a=b
    b+=i
    c=b
#(11)
def pattern(n):
    k=2*n-2
    for i in range(0,n):
        for j in range(0,k):
             print(end=' ') #space between ''
        k-=1        # use of subtract ( - )
        for j in range(0,i+1):
            print('*',end=' ') #space between ''
        print('\r')
pattern(5)
#(12)
def pattern(n):
    k=2*n-2
    for i in range(n,-1,-1):
        for j in range(k,0,-1):
            print(end=' ')
        k+=1
        for j in range(0,i+1):
            print('*',end=' ')
        print('\r')
pattern(4)
#(13)
n=8
ascii=65
for i in range(n):
    print((n-i-1)*' ', end=' ')  #space between ( - )
    for j in range(0, i+1):
        print(chr(ascii), end=' ')  #space between ( - )
        ascii+=1
    print()
#(14)
for i in range(7):
    for j in range(7):
        if j == 0 or i - j == 3 or i + j == 3:
            print("*", end="")
        else:
            print(end=" ")
    print()
#
for i in range(5):
    for j in range(5):
        if i + j == 2 or i - j == 2 or i + j == 6 or j - i == 2:
            print("*", end="")
        else:
            print(end=" ")
    print()
#
def pattern(n):
     k = 2 * n - 2
     for i in range(0, n):
          for j in range(0 , k):
               print(end=" ")
          k = k - 1
          for j in range(0 , i + 1 ):
               print("* ", end="")
          print("\r")
     k = n - 2
     for i in range(n , -1, -1):
          for j in range(k , 0 , -1): 
               print(end=" ")
          k = k + 1
          for j in range(0 , i + 1):
                print("* ", end="")
          print("\r")
pattern(5)
#
def pattern(n):
      for i in range(0, n):
           for j in range(0, i + 1):
                print("* ", end="")
           print("\r")
      for i in range(n, 0 , -1):
          for j in range(0, i + 1):
               print("* ", end="")
          print("\r")
 
pattern(5)