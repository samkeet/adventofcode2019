def is_not_decreasing(num):
    prev = num % 10
    num /= 10
    while num:
        next_rem = int(num % 10)
        if next_rem > prev:
            return False
        prev = next_rem
        num = int(num/10)
    return True

def has_same_adjacent_digits(num):
    prev = num % 10
    num /= 10

    while num:
        next_rem = int(num % 10)
        if next_rem == prev:
            return True
        prev = next_rem
        num = int(num/10)
    return False

if __name__ == "__main__":
    low, high = 134792, 675810
    possibilites = range(low, high)
    count = list(filter(lambda x: has_same_adjacent_digits(x) and is_not_decreasing(x), possibilites))
    print(len(count))