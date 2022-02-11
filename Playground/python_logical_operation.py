x = True
y = False

print(x and y)
print(x or y)
print(not x)

# for non boolean logical operation give us non boolean value
# so it would be first or second operand

p = 10
q = 20

print(p and q)  # return 20 because first(p) is true so check for other one
print(p or q)  # return 10 because first(p) is true so no need to check second one

m = 0
n = 30

print(m and n)  # return 0 beacuse first(m) is false so no need to check for second one
print(m or n)  # return 30
