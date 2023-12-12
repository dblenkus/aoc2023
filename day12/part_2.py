from functools import cache


@cache
def count(condition, groups, position, group_count, current_count):
    def hash_count():
        return count(condition, groups, position + 1, group_count, current_count + 1)

    def dot_count():
        if current_count == 0:
            return count(condition, groups, position + 1, group_count, 0)
        elif group_count < len(groups) and current_count == groups[group_count]:
            return count(condition, groups, position + 1, group_count + 1, 0)
        return 0

    if position == len(condition):
        return 1 if len(groups) == group_count else 0
    if condition[position] == "#":
        return hash_count()
    if condition[position] == ".":
        return dot_count()

    return hash_count() + dot_count()


result = 0
with open("input.txt", "r") as file:
    for line in file:
        line = line.strip()
        condition, groups = line.split(" ")
        groups = [int(group) for group in groups.split(",")] * 5
        condition = "?".join([condition] * 5) + "."

        result += count(condition, tuple(groups), 0, 0, 0)

print(result)
