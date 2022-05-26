# lines = []
# with open('the-zen-of-python.txt') as f:
#     lines = f.readlines()

# count = 0
# for line in lines:
#     count += 1

#     print(f'line {count}: {line}')

with open('the-zen-of-python.txt') as f:
    line = f.readline()
    while line:
        line = f.readline()
        print(line)