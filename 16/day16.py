def buildPattern(basePattern, index):
    pattern = []
    for num in basePattern:
        for k in range(index):
            pattern.append(num)
    return pattern

def part2(data):
    offset = int(''.join(map(str, data[:7])))
    data = (data*10000)[offset:]
    for _ in range(100):
        suffix_sum = 0
        for i in range(len(data)-1, -1, -1):
            data[i] = suffix_sum = (suffix_sum + data[i]) % 10
    return ''.join(map(str, data[:8]))

data = list(map(int, open("input.txt").read()))
print(part2(data[:]))

# fileInput = open("input.txt", "r").read()

# signal = fileInput.strip()
# offset = int(signal[0:7])
# signal = (signal * 10000)[offset:]

# basePattern = [0,1,0,-1]

# for count in range(100):
#     newSignal = ""
#     for i in range(len(signal)):
#         pattern = buildPattern(basePattern, i+1)
#         values = []

#         for j in range(len(signal)):
#             num = int(signal[j]) * pattern[(j + 1) % len(pattern)]
#             values.append(num)
        
#         sum = 0
#         for value in values:
#             sum += value
#         newSignal += str(sum)[len(str(sum))-1]
#     signal = newSignal

# print(signal[0:8])