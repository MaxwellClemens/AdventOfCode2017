import re

def hasCorrectRepititions(value):
    match = re.search(r'^(\d)(\1)(?!\2)|(\d)(\d)(?!\3)(\4)(?!\4)', value)
    return match is not None

def isNonDecending(value):
    intValues = [int(val) for val in value]
    sortedValues = sorted(intValues)
    return intValues == sortedValues

count = 0
for i in range(236491,713787):
    stringValue = str(i)
    if hasCorrectRepititions(stringValue) and isNonDecending(stringValue):
        count += 1
print(count)