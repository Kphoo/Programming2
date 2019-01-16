numbers=[]
for i in range(5):
    number=int(input("Number: "))
    numbers.append(number)
print("The first Number is", numbers[0])
print("The Last Number is", numbers[-1])
print("The Smallest Number is", min(numbers))
print("The Largest Number is", max(numbers))
print("The Average Number is", sum(numbers)/len(numbers))



