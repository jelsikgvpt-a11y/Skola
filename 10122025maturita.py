def parne_pozicie(zoz: list) -> int:
    z2 = []
    for i in range(len(zoz)):
        if i % 2 == 0:
            z2.append(zoz[i])
    return z2
print(parne_pozicie([1, 2, 3, 4, 5, 6]))  # Očakávaný výstup: [1, 3, 5]
