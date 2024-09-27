# Define the first function to perform translation based on patterns
def Solve():
    # Input arrays containing words or codes to be translated
    arr1 = ['Hola', 'Mundo']
    arr2 = ['Mundo', 'World', 'Lunes', 'Monday', 'Hola', 'Hello']

    # Initialize an empty array to store the translated words
    newarr = []
    
    # Check if any of the words in arr2 contain numbersssss
    hasNumber = any(char.isdigit() for char in ''.join(arr2))
    
    # Iterate through each word in arr1
    for i in range(len(arr1)):
        # If the word in arr1 contains digits
        if hasNumber and any(char.isdigit() for char in arr1[i]):
            char = ''
            k = 0
            # Iterate through the characters in the word
            while k < len(arr1[i]):
                # Iterate through even-indexed elements in arr2
                for j in range(0, len(arr2), 2):
                    # If the current substring matches an element in arr2
                    if arr1[i][k:k+2] == arr2[j]:
                        # Append the corresponding translation from odd-indexed element
                        char += arr2[j+1]
                k += 2
            # Add the translated word to newarr
            newarr.append(char)
        # If the word in arr1 doesn't contain digits
        else:
            # Iterate through even-indexed elements in arr2
            for j in range(0, len(arr2), 2):
                # If the current word matches an element in arr2
                if arr2[j] == arr1[i]:
                    # Append the corresponding translation from odd-indexed element
                    newarr.append(arr2[j+1])

    # Return the translated words as a single string
    return ' '.join(newarr)

# Call and print the result of the first translation function
print(Solve())

# Define the second function for a different set of translations
def Solve2():
    # Similar logic as the first function, but with different input arrays
    arr3 = ['mieux', 'vaut', 'prévenir', 'que', 'guérir']
    arr4 = ['merci', 'thank you', 'que', 'than', 'malade', 'sick', 'mieux', 'better', 'guérir', 'to heal',
            'chien', 'dog', 'vaut prévenir', 'to prevent', 'beurre', 'butter', 's\il vous plaît', 'please']
    newarr = []
    hasNumber = any(char.isdigit() for char in ''.join(arr3))

    for i in range(len(arr3)):
        if hasNumber and any(char.isdigit() for char in arr3[i]):
            char = ''
            k = 0
            while k < len(arr3[i]):
                for j in range(0, len(arr4), 2):
                    if arr3[i][k:k+2] == arr4[j]:
                        char += arr4[j+1]
                k += 2
            newarr.append(char)

        else:
            for j in range(0, len(arr4), 2):
                if arr4[j] == arr3[i]:
                    newarr.append(arr4[j+1])

    return ' '.join(newarr)

# Call and print the result of the second translation function
print(Solve2())

# Define the third function for another set of translations
def Solve3():
    # Similar logic as the first two functions, but with different input arrays
    arr5 = ['5748494348', '574159', '544845', '57494E44', '424C4F5753']
    arr6 = ['41', 'A', '42', 'B', '43', 'C', '44', 'D', '45', 'E', '46', 'F', '47', 'G', '48', 'H', '49', 'I',
            '4A', 'J', '4B', 'K', '4C', 'L', '4D', 'M', '4E', 'N', '4F', 'O', '50', 'P', '51', 'Q', '52', 'R', '53', 'S', '54',
            'T', '55', 'U', '56', 'V', '57', 'W', '58', 'X', '59', 'Y', '5A', 'Z']

    newarr = []
    hasNumber = any(char.isdigit() for char in ''.join(arr5))

    for i in range(len(arr5)):
        if hasNumber and any(char.isdigit() for char in arr5[i]):
            char = ''
            k = 0
            while k < len(arr5[i]):
                for j in range(0, len(arr6), 2):
                    if arr5[i][k:k+2] == arr6[j]:
                        char += arr6[j+1]
                k += 2
            newarr.append(char)

        else:
            for j in range(0, len(arr6), 2):
                if arr6[j] == arr5[i]:
                    newarr.append(arr6[j+1])

    return ' '.join(newarr)

# Call and print the result of the third translation function
print(Solve3())
