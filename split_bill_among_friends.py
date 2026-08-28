"""Split Bill Among Friends
Create a program to split the restaurant bill among friends.

Get an integer input for the total number of friends and assign it to the total_friends variable.
Get an integer input for the restaurant bill and assign it to the bill variable.
Calculate the tax amount, which is 20% of the bill"""

# Replace ___ with your code

# get input value for total number of friends 
tf=int(input())

# get input value for bill 
tb=int(input())

# calculate the tax amount
tax=tb*20/100

# divide the total bill among friends
tb=tb+tax
sb=tb/tf
# print the split amount
print(sb)
