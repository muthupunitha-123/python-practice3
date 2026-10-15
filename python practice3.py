1)automorphic or not
n=int(input("Enter a number:"))
square=n*n
if str(square).endswith(str(n)):
  print(n,"is an automarphic number")
else:
  print(n,"is not an automarphic number")
output:
Enter a number:25
25 is an automarphic number
2)Neon number or not
n=int(input("Enter a number"))
square=n*n
sum_digits=sum(int(digit)for digit in str(square))
if sum_digits==n:
  print(n,"is a neon number")
else:
  print(n,"is not a neon number")
  output:
Enter a number18
18 is not a neon number
3)perfect number
n=int(input("Enter a number:"))
sum_divisors=0
for i in range(1,n):
      if n%i==0:
         sum_divisors+=i
      if n>0 and sum_divisors==n:
        print(n,"is a perfect number")
      else:
        print(n,"is not a perfect number")
  output:
Enter a number:56
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
56 is not a perfect number
