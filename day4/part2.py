from part1 import is_not_decreasing, has_same_adjacent_digits

def has_even_adjacent_digits(num):
    num = str(num)
    return any(num[i] == num[i+1] and (i == 0 or num[i] != num[i-1]) and (i == 4 or num[i] != num[i+2]) for i in range(5))

if __name__ == "__main__":
    low, high = 134792, 675811
    possibilites = range(low, high)
    filtered = list(filter(lambda x: has_same_adjacent_digits(x) and is_not_decreasing(x), possibilites))
    count = list(filter(has_even_adjacent_digits, filtered))
    print(len(count))