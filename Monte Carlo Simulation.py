import random
num_win=0
n= int (input("Enter number of round:"))
for i in range(0,n):
 num1 = 1+int(random.randint(1,6))
 num2 = 1+int(random.randint(1,6))
 sum = num1+num2
 if sum == 7 or sum == 11:
     print("You Win")
     num_win=num_win+1
 elif sum == 2 or sum==3 or sum ==12:
     print("You Lost")
 else:
     new_sum=sum
     while(1):
         num1 = 1+int(random.randint(1,6))
         num2 = 1+int(random.randint(1,6))
         sum = num1+num2
         if sum==new_sum:
             num_win=num_win+1
             print("You Win")
             break
         elif sum==7:
             print("You lost")
             break
p= float(num_win)/n

print("Number Of Win :")
print(num_win)
print("Number Of Lost :")
print(n-num_win)

print("Estimate of Winning Probability :")
print(p)

