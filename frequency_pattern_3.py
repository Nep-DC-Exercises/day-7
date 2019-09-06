# Create a function that accepts two strings and checks if they are valid anagrams.

string_1 = "pie"
string_2 = "eip"


def anagrams(str1, str2):

    dict1 = {}
    dict2 = {}

    for i in range(len(str1)):
        letter = str1[i]

        if letter not in dict1:
            dict1[letter] = 1
        else:
            dict1[letter] += 1

    for i in range(len(str1)):
        letter = str2[i]

        if letter not in dict2:
            dict2[letter] = 1
        else:
            dict2[letter] += 1

        if dict1 == dict2:
            return True
        else:
            return False


if anagrams(string_1, string_2):
    print("The two strings are anagrams.")
else:
    print("Not anagrams")
