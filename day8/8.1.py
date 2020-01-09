zmin = 25*6*2
image = True
with open("input.txt", 'r') as f:
    while True:
        image = f.read(25 * 6).strip()
        if not image:
            break
        # This can be done much more efficiently, but the input is of
        # reasonable size so...
        z = image.count('0')
        if z < zmin:
            zmin = z
            ret = image.count('1') * image.count('2')

print(ret)
