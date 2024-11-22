#print 
# * * * *
# * * * *
# * * * *
# * * * *
'''
n=int(input())
for i in range(1,n+1):
    print('* '*n)
'''
#print
# *
# * *
# * * *
# * * * *
'''
n=int(input())
for i in range (1,n+1):
    print('* '*i)
'''
#print
#       *
#      * *
#     * * *
#    * * * *
#   * * * * *
'''
n=int(input())
for i in range (1,n+1):
    print(' '*(n-i),"* "*i)

n=int(input())
sp=n-1
for i in range(1,n+1):
    print(' '*sp,'* '*i)
    sp-=1
'''
#print
#     *
#   * * *
#  * * * *
# * * * * *
'''
n=int(input())
for i in range (1,n+1):
    print(' '*(n-i),"*"*(2*i-1))
'''
#print
# ****
#  ***
#   **
#    *
'''
n=int(input())
for i in range(0,n+1,1):
    print(' '*i,'*'*n )
    n-=1
    
n=int(input())
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * i)
'''
#  * * * * * * *
#   * * * * * *
#    * * * * *
#     * * * *
#      * * *
#       * *
#        *
'''
n=int(input())
for i in range (n,0,-1):
    print(' '*(n-i),'* '*i)
'''
#print
#  *********
#   *******
#    *****
#     ***
#      *
'''
n=int(input())
for i in range(n,0,-1):
    print(' '*(n-i),'*'*(2*i-1))
'''
#print
#      *
#     **
#    ***
#   ****
#  *****
'''
n=int(input())
star=1
for i in range(n,0,-1):
    print(' '*i,'*'*star)
    star+=1

n=int(input())
j=1
for i in range (1,n+1):
    print(' '*(n-i),'*'*j)
    j+=1

n=int(input())
for i in range(1,n+1):
    print(' '*(n-i),'*'*i)
'''
#print
# *   *
#  * *
#   *
#  * *
# *   *
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print('*',end='')
        else:
            print(' ',end='')  
    print()
'''

#print
# ****
#  ***
#   **
#    *
#   **
#  ***
# ****
'''
n=int(input())
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * i)
for i in range(2, n + 1):
    print(' ' * (n - i) + '*' * i)
'''
#print
#     *
#    ***
#   *****
#  *******
# *********
# n=int(input())#5
# for i in range(1,n+1):#1,2,3,4,5
#     print(' '*4,'*'*i)
#wap to print
'''
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E 
n=int(input())
dummy=1
for row in range(1,n+1):
    for st in range(1,n+1):
        print(chr(dummy+64),end=' ')
    print()
    dummy+=1
'''
#wap to print
'''
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E 
n=int(input())
for row in range(1,n+1):
    dummy=1
    for st in range(1,n+1):
        print(chr(dummy+64),end=' ')
        dummy+=1
    print()
'''
#wap to print
'''
n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(chr(dummy+64),end=' ')
    dummy+=1
    print()
'''
#wap to print
'''
n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(chr(dummy+64),end=' ')
        if row%2==0:
            dummy+=1
        else:
            dummy+=2
    print()
'''
#wap to print
'''
n=int(input())
dummy=1
for row in range(1,n+1):
    print(chr(dummy+64),end=' ')
    if row%2==1:
        dummy+=1
    else:
        dummy==2
    print()
'''
#wap to print
'''
n=int(input())
spaces=n-1
stars=1
dummy=1
for rows in range(1,spaces+1):
    for sp in range(1,stars+1):
        print(' ',end=' ')
    for st in range(1,stars+1):
        print(chr(dummy+64),end=' ')
    print()
    spaces-=1
    stars+=1
    dummy+=1
'''
#wap to print
'''
n=int(input())
spaces=1
stars=n-1
dummy=1
for rows in range(1,n+1):
    dummy+=1
    for st in range(1,stars+1):
        print(chr(dummy+64),end=' ')
    for sp in range(1,spaces+1):
        print(' ',end=' ')
    print()
    stars-=1
    spaces+=1
'''
#wap to print
'''
n=int(input())
spaces=1
stars=n-1
for rows in range(1,n+1):
    dummy=1
    for st in range(1,stars+1):
        print(chr(dummy+64),end=' ')
    for sp in range(1,spaces+1):
        print(' ',end=' ')
        dummy+=1
    print()
    spaces+=1
    stars-=1
'''

#wap to print
'''
A
B B
C C C
D D D D
E E E E E
n=int(input())
dummy=1
for rows in range(1,n+1):
    for col in range(1,rows+1):
        print(chr(dummy+64),end=' ')
    print()
    dummy+=1
'''
#wap to print
'''
A
  C
    E
      G
        I
n=int(input())
for row in range(1,n+1):
    dummy=1
    for col in range(1,n+1):
        if row==col:
            print(chr(dummy+64),end=' ')
        else:
            print(' ',end=' ')
        dummy+=2
    print()
'''
#wap to print
'''
A F K P U
B G L Q V
C H M R W
D I N S X
E J O T Y
n=int(input())
for row in range(1,n+1):
    dummy=row
    for col in range(1,n+1):
        print(chr(dummy+64),end=' ')
        dummy+=5
    print()
'''
#wap to print
'''
AAAAA
AAAAA
AAAAA
AAAAA
AAAAA
n=int(input())
for i in range(1,n+1):
    print('A'*n)
'''
#wap to print pattern like
'''
* * * * *
*       *
*       *
*       *
* * * * *
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#wap to program to print pattern
'''
         *
      *
    *
  *       
*
'''
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i+j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#write a program to print pattern
'''
*
  *
    *
      *   
        *
'''
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#write a program to print
'''
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''
'''
n=int(input())
for i in range(1,n+1):
    print('* '*n)
'''
#wap to print diamond shape.
'''
          * 
        * * *
      * * * * *
    * * * * * * *
  * * * * * * * * * 
* * * * * * * * * * *
  * * * * * * * * * 
    * * * * * * *
      * * * * * 
        * * *
'''
#wap to print star pattern
'''
*       *
  *   *
* * * * * 
  *   *
*       *
'''
'''
n=int(input())#5
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1 or (i==(n//2)+1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#WAP TO PRINT 
'''
            *
         *  *  *
      *  *  *  *  *  
         *  *  *
            *
'''
#wap to print
'''       
            *
         *  *  *
      *  *  *  *  *
'''
'''      
n=int(input())
for i in range(1,n+1):
    print(' '*(n-i),'*'*(2*i-1))
'''
#wap to print
'''
*****
 ****
  ***
   **
    *
'''
'''
n=int(input())#5
for i in range(n):
    print(' '*i,'*'*n)
    n-=1
'''

#wap to print
'''
*****
****
***
**
*
'''
'''
n=int(input())#5
for i in range(n,1,-1):
    print('*'*i)
'''
#wapt print 
# * * * * *
# *       *
# *       *
# *       *
# * * * * *
'''
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#print
# 11111
# 22222
# 33333
# 44444
# 55555
'''
d=1
n=int(input())
for i in range(1,n+1):
    print(str(i) *n)
    d+=1
'''
#print
# 12345
# 12345
# 12345
# 12345
# 12345
'''
n=int(input())
for i in range(1,n+1):
    d=1
    for j in range(1,n+1):
        print(d,end='')
        d+=1
    print()
'''
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):

#print
# 1
# 22
# 333
# 4444
# 55555
'''
n=int(input())#5
j=1
for i in range(1,n+1):#1,2,3,4,5
        print(str(i)*j) 
        j+=1
'''
#print
#    1
#   222
#  33333
'''
num=int(input())#3
for i in range(1,num+1):#1,2,3
    print(' '*(num-i),str(i)*(2*i-1))
'''
#print
# num=int(input())
# for i in range(num):#0,1,2,3,4.
#     for j in range(num):#0,1,2,3,4.
#         row=''.join(str(i+j+1))
#         print(row,end='')
#     print()+

#print
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
'''
n=int(input())
j=1
k=''
for i in range(2,n+2):#2 3 4 5 6
    print(str(j)+k)
    k=k+' '+str(i)
'''
# n=int(input())#5
# for i in range(1,n+1):#1,2,3,4,5
#     for j in range(1,n+1):#1,2,3,4,5
#         print('* ',end='')
#         if j!=n:
#             print('-',end=' ')
#     print()


#print
# * * * * *
# *       *
# *       *
# *       * 
# * * * * *
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''