#acp
num = int(input("Enter a number: "))
odd_numbers = [i for i in range(num) if i % 2 != 0]
print("Odd numbers below", num, "are:", odd_numbers)