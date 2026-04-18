planet = ["Mercury", "Venus", "Earth", "Mars"]
jarak = [57.9, 108.2, 149.6, 227.9] #juta km
diameter = [4879, 12104, 12742, 6779] #km

#menampilkan total jarak semua planet
total_jarak_planet = sum(jarak)
print(total_jarak_planet)

#menampilkan rata-rata jarak planet
rata_rata_jarak_planet = sum(jarak) / len(jarak)
print(rata_rata_jarak_planet)

#menampilkan diameter planet terbesar
diameter_planet_terbesar = max(diameter)
print(diameter_planet_terbesar)

#menampilkan diameter planet terkecil
diameter_planet_terkecil = min(diameter)
print(diameter_planet_terkecil)

#menampilkan selisih diameter antara planet terbesar dan terkecil
selisih_diameter = diameter_planet_terbesar - diameter_planet_terkecil
print(selisih_diameter)

#menampilkan jarak planet pertama dan terakhir
jarak_planet_pertama = jarak[0]
print(jarak_planet_pertama)

jarak_planet_terakhir = jarak[-1]
print(jarak_planet_terakhir)