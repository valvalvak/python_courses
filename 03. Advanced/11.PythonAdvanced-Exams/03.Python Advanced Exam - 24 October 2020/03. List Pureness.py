from collections import deque


def best_list_pureness(values, k):
    values = deque(values)

    def calc_pureness(values):
        pureness = 0
        for (idx, val) in enumerate(values):
            pureness += idx * val
        return pureness

    k = min(k, len(values))
    best_rotation = 0
    best_pureness = calc_pureness(values)

    for rotations in range(k + 1):
        current_pureness = calc_pureness(values)
        if best_pureness < current_pureness:
            best_rotation = rotations
            best_pureness = current_pureness

        values.rotate()

    return f"Best pureness {best_pureness} after {best_rotation} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)

test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)

test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
