import numpy as np
import matplotlib.pyplot as plt

# 1. Učitavanje podataka (putanja sa prethodnog koraka)
putanja = '/home/Nikola.Jankovic/projekat/slucaj_2/python/struja.txt'
try:
    podaci = np.loadtxt(putanja)
    vin = podaci[:, 0]
    # i(Vdd) je u koloni 3, množimo sa -1e6 da dobijemo pozitivne mikroampere (uA)
    # Na osnovu slike image_13.png, struja je ovde izuzetno mala relative to 120uA.
    struja_ua = -podaci[:, 3] * 1e6 
except Exception as e:
    print(f"Greška pri učitavanju: {e}")
    exit()

# 2. Pronalaženje vrha (potrebno nam je za poziciju vertikalne linije i dinamički limit osa)
idx_max = np.argmax(struja_ua)
vt_real = vin[idx_max]
imax = struja_ua[idx_max]

# 3. Kreiranje grafika
plt.figure(figsize=(10, 6))

# Estetika: senčenje oblasti ispod krive u teal boji
plt.fill_between(vin, 0, struja_ua, color='teal', alpha=0.15)
# Glavna linija krive, teal boja, deblja linija
plt.plot(vin, struja_ua, color='teal', linewidth=3, label=r'Struja iz izvora za napajanje')

# Vertikalna linija za Vt na ~0.81V, crvena, isprekidana
plt.axvline(x=vt_real, color='red', linestyle='--', alpha=0.6)

# Podešavanja osa, naslova i legendi
plt.title('Zavisnost struje napajanja od ulaznog napona', fontsize=14, pad=15)
plt.xlabel('Ulazni napon $V_{in}$ [V]', fontsize=12)
plt.ylabel('Struja napajanja $i(V_{DD})$ [µA]', fontsize=12)
plt.xlim([0, 1.5])

# --- KLJUČNA PROMENA: Dinamički limit Y-ose ---
# Uklonili smo max(120, ...) i koristimo samo imax * 1.1 da grafik "zumi-ra" pik.
# Ovo garantuje da će se videti "zvono", bez obzira koliko je pik mali.
plt.ylim([0, imax * 1.1]) 

plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper left')

plt.tight_layout()
# Čuvamo kao novi fajl za izveštaj
plt.savefig('/home/Nikola.Jankovic/projekat/slucaj_2/python/struja.svg', format='svg')
plt.show()

print(f"Analiza završena. Dinamički grafik je generisan i sačuvan.")
print(f"Informacija o stvarnom piku: Max struja je {imax:.2f} uA na naponu {vt_real:.2f} V.")
