# Programming Assignment -11 02072022


# 1. Write a Python program to find words which are greater than given length k?

def find_words(strLine, k):
    words = strLine.split(" ")
    for strTemp in words:
        if len(strTemp) > k:
          print(strTemp)

k = int(input("Enter length of word"))
actualText = input("Enter the whole string line")
find_words(actualText, k)

# 2. Write a Python program for removing i-th character from a string ?

def replace_item(i):
    s = "Python string manipulation"
    s = s.replace(s[i], "", 1)
    return s

def remove_item(strText, i):
    for j in range(len(strText)):
        if j == i:
            strText = strText.replace(strText[i], "", 1)
            return strText

print(replace_item(4))
print(remove_item("Python string manipulation", 5))


# 3. Write a Python program to split and join a string ?

def split_join_string(strWords):
    lst_split_string = strWords.split(" ")
    str_delimiter = "-"
    joined_string = str_delimiter.join(lst_split_string)
    return joined_string

actualText = input("Enter the whole string line")
print(split_join_string(actualText))

# 4. Write a Python to check if a given string is binary string or not?

def find_binary_string(strWord):
    for i in myStr:
        if (i != '0' and i != '1'):
            return "This is not a binary string"
            break
        else:
            continue
    return "This is a binary string"

myStr = input('Enter the string : ')
print(find_binary_string(myStr))


# 5. Write a Python program to find uncommon words from two Strings?

def find_uncommon_words(mystr1, mystr2):
    lststr1 = mystr1.split()
    lststr2 = mystr2.split()
    uncommonWords = ""
    for words in lststr1:
        if words not in lststr2:
            uncommonWords = uncommonWords + " " + words
    for words in lststr2:
        if words not in lststr1:
            uncommonWords = uncommonWords + " " + words
    return uncommonWords

actualText1 = input('Enter first string : ')
actualText2 = input('Enter second string : ')
print(find_uncommon_words(actualText1,actualText2))

# 6. Write a Python to find all duplicate characters in string?

def find_duplicate(str1):
    strDuplicate=set()
    for i in str1:
        count_i = str1.count(i)
        if(count_i > 1):
            strDuplicate.add(i)
    return strDuplicate


actualText1 = input('Enter the duplicate string : ')
print(find_duplicate(actualText1))

# 7. Write a Python Program to check if a string contains any special character?

def find_special(str1):
    strSpecials='[@_!#$%^&*()<>?/\|}{~:]'
    for i in str1:
        if i in strSpecials:
            return "string contains special character"
            break
        else:
            continue
    return "string doesn't contains special character"

actualText1 = input('Enter the special string : ')
print(find_special(actualText1))





