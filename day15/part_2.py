def get_hash(word):
    result = 0
    for char in word:
        result = ((result + ord(char)) * 17) % 256
    return result


with open("input.txt", "r") as file:
    line = file.readline().strip()

boxes = [[] for _ in range(256)]
focal_lengths = {}

for word in line.split(","):
    if word[-1] == "-":
        label = word[:-1]
        box_hash = get_hash(label)
        if label in boxes[box_hash]:
            boxes[box_hash].remove(label)
    else:
        label, focal_length = word.split("=")
        box_hash = get_hash(label)
        focal_lengths[label] = int(focal_length)
        if label not in boxes[box_hash]:
            boxes[box_hash].append(label)

result = 0
for i, lenses in enumerate(boxes, start=1):
    for j, lens in enumerate(lenses, start=1):
        result += i * j * focal_lengths[lens]

print(result)
