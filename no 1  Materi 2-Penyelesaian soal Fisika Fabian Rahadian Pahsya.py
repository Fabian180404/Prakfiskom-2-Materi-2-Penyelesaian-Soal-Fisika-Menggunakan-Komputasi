# Diketahui
n = 1.50  # indeks bias medium
R1 = 22  # jari-jari kelengkungan permukaan lensa R1 (dalam cm)
R2 = 17.5  # jari-jari kelengkungan permukaan lensa R2 (dalam cm)

# Menggunakan persamaan pembuat lensa
# 1/f = (n - 1) * (1/R1 + 1/R2)

f_inverse = (n - 1) * (1/R1 + 1/R2)  # menghitung 1/f
f = 1 / f_inverse  # menghitung jarak fokus f

f  # hasil jarak fokus lensa (f) dalam cm

print(" Jarak Fokus Lensa : ",f, "cm")
