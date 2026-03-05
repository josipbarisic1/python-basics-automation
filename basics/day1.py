# asks the user for a number
# prints numbers from 1 to that number
# tells whether the number is even or odd

while True:
    number = input("Provide a number: ")

    if not number.isdigit():
        print("Number must be an Integer.")
        continue

    number = int(number)
    
    if number < 1:
        print("Number must be > 1.")
    else:
        break

for x in range(1, number + 1):
    if x % 2 == 0:
        print(f"{x}  (even)")
    else:
        print(f"{x}  (odd)")