# Selection Sort

num = int(input("Enter the number of elements: "))
arr = list(map(int, input("Enter the elements : ").split()))

for i in range(num):
    smallest = i
    for j in range(i + 1, num):
        if arr[j] < arr[smallest]:
            smallest = j
    arr[i], arr[smallest] = arr[smallest], arr[i]

print("Sorted!")
for i in arr:
    print(i, end=" ")
