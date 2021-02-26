# Kelly Shungu
"""
In this program I am going to convert numbers into words.
We have a text file with numbers, which we have to convert to the words.
"""

# open text file for input and read data from file
with open("TextFile.txt") as f:
    data = f.read()
    li = data.split(" ")
numericHold = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']


# create new list empf for numeric data
emp = []
for i in li:

# check if input file contain numeric values append into list emp:
    if i.isnumeric():
        emp.append(int(i))
    elif not i.isnumeric():
        for j in i:
            if j in numericHold:
                print(i, "is invalid")
                break
            else:
                pass

# making the Lists for numbers to convert in words ones,twenties,thousands
ones = ["", "one ", "two ", "three ", "four ", "five ", "six ", "seven ", "eight ", "nine ", "ten ", "eleven ",
        "twelve ", "thirteen ", "fourteen ", "fifteen ", "sixteen ", "seventeen ", "eighteen ", "nineteen "]

twenties = ["", "", "twenty ", "thirty ", "forty ", "fifty ", "sixty ", "seventy ", "eighty ", "ninety "]

thousands = ["", "thousand ", "million ", "billion ", "trillion ", "quadrillion ", "quintillion ", "sextillion ",
             "septillion ", "octillion ", "nonillion ", "decillion ", "undecillion ", "duodecillion ", "tredecillion ",
             "quattuordecillion ", "quintillion", "sextillion ", "septillion ", "Duodecillion ",
             "tredecillion ", "quintillion "]


def num999(n):
    c = n % 10  # singles digit
    b = ((n % 100) - c) / 10  # tens digit
    a = ((n % 1000) - (b * 10) - c) / 100  # hundreds digit
    t = ""
    h = ""
    if a != 0 and b == 0 and c == 0:
        t = ones[int(a)] + "hundred "
    elif a != 0:
        t = ones[int(a)] + "hundred and "
    if b <= 1:
        h = ones[n % 100]
    elif b > 1:
        h = twenties[int(b)] + ones[int(c)]
    st = t + h
    return st


# this function converts number to word
def number_To_Word(num):
    if num == 0:
        return 'zero'

    i = 3
    n = str(num)
    word = ""
    k = 0
    while i == 3:
        nw = n[-i:]
        n = n[:-i]
        if int(nw) == 0:
            word = num999(int(nw)) + thousands[int(nw)] + word
        else:
            word = num999(int(nw)) + thousands[k] + word
        if n == '':
            i = i + 1
        k += 1
    return word[:-1]



# final loop,gets values from numeric list emp:
for val in emp:
    if len(emp) == 0:
        print("invalid num")
        break
    else:
        print(number_To_Word(val))
