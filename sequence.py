# takes input of length of sequence, start with only 3 and that is minimum input. then loop as many times as needed

n = int(input("Enter the length of the sequence: ")) # Do not change this line
base = [1,2,3]
for i in range(3, n):
    base.append(sum(base[-3:]))

for i in base:
    print(i)