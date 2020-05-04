# Felszin es terfogatszamito
length = float(input('Kerlek ird be a hosszusagat a testnek: '))
width = float(input('Kerlek ird be a szelesseget a testnek: '))
height = float(input('Kerlek ird be a magassagat a testnek: '))
# Felszin
SA = 2 * (length * width + length * height + width * height)

# Terfogat
Volume = length * width * height

print("\n A felszine testnek = %.2f " %SA)
print(" A terfogata a testnek = %.2f" %Volume);