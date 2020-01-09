height = 6
width = 25
dims = height * width

image = dims * ['2']

layers = []

with open("input.txt", 'r') as f:
    while True:
        layer = f.read(dims).strip()
        if not layer:
            break
        layers.append(layer)

for i in range(len(image)):
    for layer in layers:
        if layer[i] != '2':
            image[i] = layer[i] if layer[i] == '1' else ' '
            break

    if i % width == width-1:
        row = ''.join(image[i-(width-1):i])
        print(row)
