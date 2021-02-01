set_a = set()
set_b = set()

input_a = input()
input_b = input()

for a in input_a:
    set_a.add(a)

for b in input_b:
    set_b.add(b)

print(len(input_a) - len(set_a))
print(len(input_b) - len(set_b))

diff = set_a.symmetric_difference(set_b)
print(len(diff))
