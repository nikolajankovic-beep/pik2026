import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 1. Učitavanje SVA TRI fajla sa podacima
podaci_20 = np.loadtxt('najgori_odziv_2.txt') 
podaci_25 = np.loadtxt('najgori_odziv_2_5.txt') 
podaci_30 = np.loadtxt('najgori_odziv_3.txt') 

# 2. Ekstrakcija vremena i napona ZA SVAKI FAJL POSEBNO
t_20 = podaci_20[:, 0] * 1e12  
v_in = podaci_20[:, 1]          
v_out_20 = podaci_20[:, 3]        

t_25 = podaci_25[:, 0] * 1e12  
v_out_25 = podaci_25[:, 3]

t_30 = podaci_30[:, 0] * 1e12  
v_out_30 = podaci_30[:, 3]

# 3. Kreiranje grafika 
fig, ax = plt.subplots(figsize=(12, 6), dpi=300)

# Crtanje zajedničkog ulaza (Crna boja, malo tanja linija da ide u pozadinu)
ax.plot(t_20, v_in, color='black', linewidth=1.5, linestyle='--', label='Ulaz A (Zajednički)')

# Crtanje sva tri izlaza sa VISOKO-KONTRASTNIM bojama
ax.plot(t_20, v_out_20, color='#0052cc', linewidth=2.5, label='Izlaz F ($W_p/W_n = 2.0$)') # Jaka Plava
ax.plot(t_25, v_out_25, color='#e60000', linewidth=2.5, label='Izlaz F ($W_p/W_n = 2.5$)') # Jaka Crvena
ax.plot(t_30, v_out_30, color='#009933', linewidth=2.5, label='Izlaz F ($W_p/W_n = 3.0$)') # Jaka Zelena

# 4. Pragovi merenja (Siva boja umesto plave, da ne zbunjuju oči)
ax.axhline(0.15, color='gray', linestyle='--', linewidth=1, alpha=0.8)
ax.axhline(1.35, color='gray', linestyle='--', linewidth=1, alpha=0.8)
ax.text(5, 0.17, '10% $V_{DD}$', color='gray', alpha=0.9, fontsize=10, fontweight='bold')
ax.text(5, 1.37, '90% $V_{DD}$', color='gray', alpha=0.9, fontsize=10, fontweight='bold')

# 5. Ulepšavanje
ax.set_title('Zbirni tranzijentni odziv: Uticaj parazitnih kapacitivnosti PMOS mreže', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Vreme [ps]', fontsize=12)
ax.set_ylabel('Napon [V]', fontsize=12)

ax.set_ylim(-0.2, 1.8)
ax.set_xlim(0, 500)

ax.grid(True, linestyle=':', alpha=0.6)
ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.3))

ax.legend(loc='upper right', fontsize=11, frameon=True, edgecolor='black', framealpha=0.9)

# 6. Čuvanje
plt.tight_layout()
plt.savefig('odziv_svi.png', dpi=300, bbox_inches='tight')
plt.show()
