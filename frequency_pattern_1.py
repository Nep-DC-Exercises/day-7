# Given two arrays write a function to find out if two arrays have the same frequency of digits.

array_1 = [1, 2, 3, 4]
array_2 = [1, 2, 3, 4]
frequency_1 = {}
frequency_2 = {}

# populate two dictionaries with key of the number in the array and the value is how frequent it shows up


def frequency(arr1, arr2, dict1, dict2):

    for i in arr1:

        if i not in dict1:
            dict1[i] = 1

        else:
            dict1[i] += 1

    for i in arr2:

        if i not in dict2:
            dict2[i] = 1

        else:
            dict2[i] += 1


frequency(array_1, array_2, frequency_1, frequency_2)

if frequency_1 == frequency_2:

    print("The two arrays have the same frequency of digits.")

else:

    print("The to arrays do not have the same frequency of digits.")
