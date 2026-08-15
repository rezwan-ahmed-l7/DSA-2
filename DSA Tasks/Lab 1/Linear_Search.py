print("Enter numbers: ")
numbers = list(map(int, input().split()))

target = int(input("Target: "))

found = False

for index in range(len(numbers)):
    if numbers[index] == target:
        print("Element found at index: ", index)
        found = True
        break

if not found:
    print(-1)