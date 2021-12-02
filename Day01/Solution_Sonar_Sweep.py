f = open('input.txt', 'r')
input = str.splitlines(f.read())

prev = int(input[0])
count = 0
for element in input:
    if prev < int(element):
        count += 1
    prev = int(element)
        
    
print(count)
