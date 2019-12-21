import sys
import os

'''
Solving the questions is not a problem but,
doing so while selecting the right data structures for 
optimality is important.
'''
MAX_WIDTH = 25
MAX_HEIGHT = 6
MAX_PIXELS_PER_LAYER = MAX_HEIGHT * MAX_WIDTH

def generate_layers(image):
    layers_indexed = {}
    min_zero_index = 0
    curr_layer_index = 0
    min_zero_count = sys.maxsize

    i = 0
    j = 0
    while i < len(image):
        zero_count = 0
        curr_layer = []

        while j < i + MAX_PIXELS_PER_LAYER and j < len(image):
            curr_layer.append(image[j])
            if image[j] == 0:
                zero_count += 1
            j += 1
        i = j

        layers_indexed[curr_layer_index] = curr_layer
        if zero_count < min_zero_count:
            min_zero_index = curr_layer_index
            min_zero_count = zero_count

        curr_layer_index += 1

    print(min_zero_count, min_zero_index)
    print(layers_indexed[min_zero_index].count(1) * layers_indexed[min_zero_index].count(2))

if __name__ == "__main__":
    with open('input.txt', 'r') as fp:
        image = fp.read()
        image = list(map(int, image))
        # print(len(image))
        generate_layers(image)