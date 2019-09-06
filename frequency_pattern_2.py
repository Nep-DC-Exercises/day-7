# Given two arrays write a function to determine if each value in our first array contains a corresponding value to the second power in the second array.

array_1 = [1, 2, 3, 4]
array_2 = [1, 4, 9, 16]
truth = []


def comparison(arr1, arr2, list):

    for i in arr1:
        square = i ** 2

        # if the number in array_1 squared is found in array_2, add True to the truth list.
        if square in arr2:
            list.append(True)
        else:
            list.append(False)


# calling the comparison function
comparison(array_1, array_2, truth)

# We check to see if any False values are in the truth array. If there are any, then the second array does not contain each value in array 1 squared.
if False in truth:
    print("The second array does not contain each value of the first array squared")

else:
    print("The second array contains each value of the first array squared.")
