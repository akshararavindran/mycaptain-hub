

t = int(input("How many terms? "))


n1, n2 = 0, 1
count = 0


if t <= 0:
   print("Please enter a positive integer:")
elif t == 1:
   print("Fibonacci sequence upto",t,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < t:
       print(n1)
       n3 = n1 + n2
       n1 = n2
       n2 = n3
       count=count+1