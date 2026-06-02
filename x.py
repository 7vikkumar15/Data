import numpy as np

# Create Arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([1, 2, 3, 4, 5])

print("Array 1:", arr1)
print("Array 2:", arr2)

# Addition
print("\nAddition:")
print(arr1 + arr2)

# Subtraction
print("\nSubtraction:")
print(arr1 - arr2)

# Multiplication
print("\nMultiplication:")
print(arr1 * arr2)

# Division
print("\nDivision:")
print(arr1 / arr2)

# Maximum and Minimum
print("\nMaximum Value:", np.max(arr1))
print("Minimum Value:", np.min(arr1))

# Mean
print("Mean of Array 1:", np.mean(arr1))

# Reshape Array
new_array = np.array([1, 2, 3, 4, 5, 6])
reshaped = new_array.reshape(2, 3)

print("\nReshaped Array (2x3):")
print(reshaped)