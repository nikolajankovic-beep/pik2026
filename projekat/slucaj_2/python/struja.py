import numpy as np
import matplotlib.pyplot as plt

putanja = '/home/Nikola.Jankovic/projekat/slucaj_2/python/struja.txt'
try:
    podaci = np.loadtxt(putanja)
    vin = podaci[:, 0]
    struja_ua = -podaci[:, 3] * 1e6 
except Exception as e:
    print(f"Greška pri učitavanju: {e}")
    exit()

idx_max = np.argmax(struja_ua)
vt_real = vin[idx_max]
imax = struja_ua[idx_max]

plt.figure(figsize=(10, 6))

plt.fill_between(vin, 0, struja_ua, color='teal', alpha=0.15)

plt.plot(vin, struja_ua, color='teal', linewidth=3, label=r'Struja iz izvora za napajanje')

plt.axvline(x=vt_real, color='red', linestyle='--', alpha=0.6)

plt.title('Zavisnost struje napajanja od ulaznog napona', fontsize=14, pad=15)
plt.xlabel('Ulazni napon $V_{in}$ [V]', fontsize=12)
plt.ylabel('Struja napajanja $i(V_{DD})$ [µA]', fontsize=12)
plt.xlim([0, 1.5])

plt.ylim([0, imax * 1.1]) 

plt.grid(True, linestyle=':', alpha=0.7)
plt.legend(loc='upper left')

plt.tight_layout()
plt.savefig('/home/Nikola.Jankovic/projekat/slucaj_2/python/struja.svg', format='svg')
plt.show()

