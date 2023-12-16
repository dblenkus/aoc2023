def get_hash(word):
    result = 0
    for char in word:
        result = ((result + ord(char)) * 17) % 256
    return result


with open("input.txt", "r") as file:
    line = file.readline().strip()

result = 0
for word in line.split(","):
    result += get_hash(word)

print(result)
