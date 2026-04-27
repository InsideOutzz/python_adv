try:

    result = 10/0
except ZeroDivisionError:
    print('that shih dosent work vro')

fruits = {
    "apple":5,
    "orange":4,
    "banana":6
}

print(fruits['banana'])

try:
    print(fruits["cherry"])

except KeyError:
    print("that dosent exist vro")