f = open('input.txt', 'r')
input = str.splitlines(f.read())

sum_sublist = sum([int(input[i])  for i in range(3)])
count = 0
for x in range(3,len(input)):
    if sum_sublist < sum_sublist - int(input[x-3]) + int(input[x]):
        count += 1
    sum_sublist += int(input[x]) - int(input[x-3])
        
print(count)
