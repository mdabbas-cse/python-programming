fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in fruits:
  if x == "banana":
    break
  print(x)

for x in fruits:
  if x == "banana":
    continue
  print(x)

print("range(6)")
# range(6)
for x in range(6):
  print(x)

print("range(2, 6)")
# start from 2, end at 5
for x in range(2, 6):
  print(x)

print("range(2, 30, 3)")
# start from 2, end at 30, increment by 3
for x in range(2, 30, 3):
  print(x)

print("range(6, 0, -1)")
# else in for loop
for x in range(6):
  print(x)
else:
  print("Finally finished!")


# nested for loop
print("nested for loop")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

# pass statement
print("pass statement")
for x in [0, 1, 2]:
  pass
