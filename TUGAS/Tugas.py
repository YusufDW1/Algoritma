berat = float(input("Masukkan berat barang (kg): "))
jarak = float(input("Masukkan jarak pengiriman (km): "))

if jarak >= 100:
    biaya_per_kg = 15000
else:
    biaya_per_kg = 10000

biaya_pengiriman = berat * biaya_per_kg

if biaya_pengiriman < 20000:
    biaya_pengiriman = 20000

print(f"Biaya pengiriman untuk berat {berat} kg dan jarak {jarak} km adalah Rp {biaya_pengiriman}")