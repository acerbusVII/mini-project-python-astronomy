planet = ["Kepler-22b", "Kepler-452b", "Kepler-186f", "Proxima Centauri b"]
jarak_bumi = [600, 1400, 500, 4.24] #tahun cahaya
radius = [2.4, 1.6, 1.1, 1.3] #kali radius bumi
temperatur = [295, 265,188, 234] #Kelvin

#menampilkan seluruh dataset
print(planet)
print(jarak_bumi)
print(radius)
print(temperatur)

#menampilkan total jarak semua planet dari Bumi
total_jarak_planet = sum(jarak_bumi)
print(total_jarak_planet)

#menampilkan rata-rata jarak planet dari Bumi
rata_rata_jarak_planet = sum(jarak_bumi) / len(jarak_bumi)
print(rata_rata_jarak_planet)

#menampilkan radius terbesar
radius_terbesar = max(radius)
print(radius_terbesar)

#menampilkan radius terkecil
radius_terkecil = min(radius)
print(radius_terkecil)

#menampilkan selisih termperatur tertinggi dan terendah
selisih_temperatur = max(temperatur) - min(temperatur)
print(selisih_temperatur)

#menampilkan nama planet pertama dan terakhir
planet_pertama = planet[0]
print(planet_pertama)

planet_terakhir = planet[-1]
print(planet_terakhir)

#menampilkan temperatur planet kedua
temperatur_planet_kedua = temperatur[1]
print(temperatur_planet_kedua)