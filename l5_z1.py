n = int(input("n = "))
print(f"Enter {n} array elements:")
arr = [int(input()) for _ in range(n)]
print("Original array: ", arr)

# Знаходження добутку елементів з непарними індексами
product = 1  # Початкове значення добутку
for i in range(1, len(arr), 2):  
    product *= arr[i]
print("Product of elements with odd indices: ", product)
