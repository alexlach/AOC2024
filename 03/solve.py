import re

text = open("03/input.txt").read()

# part 1
matches = re.findall(
    r"mul\((\d+),(\d+)\)", text
)  # match mul(x,y) where x and y are numbers
print(sum(int(x) * int(y) for x, y in matches))

# part 2
current_dont_index = text.find("don't()")
new_text = text[:current_dont_index]
while True:
    current_do_index = text.find("do()", current_dont_index)
    if current_do_index == -1:
        break  # no more do()s, ignore the rest of the text
    current_dont_index = text.find("don't()", current_do_index)
    if current_dont_index == -1:
        new_text += text[current_do_index:]
        break  # no more don't()s, add the rest of the text
    new_text += text[current_do_index:current_dont_index]

matches = re.findall(r"mul\((\d+),(\d+)\)", new_text)
print(sum(int(x) * int(y) for x, y in matches))
