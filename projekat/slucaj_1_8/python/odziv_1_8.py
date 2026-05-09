import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

# 1. Učitavanje podataka 
podaci = np.loadtxt('/home/Nikola.Jankovic/projekat/slucaj_1_8/python/odziv_1_8.txt') 

t = podaci[:, 0] * 1e12  
v_in = podaci[:, 1]          
v_out = podaci[:, 3]        

# --- FUNKCIJA ZA AUTOMATSKO NALAŽENJE PRESEKA (Hirurška preciznost) ---
def nadji_presek(vreme, napon, prag, smer, pocetno_vreme):
    idx = np.where(vreme > pocetno_vreme)[0]
    t_sub, v_sub = vreme[idx], napon[idx]
    for i in range(len(v_sub)-1):
        if smer == 'rast' and v_sub[i] <= prag <= v_sub[i+1]:
            return np.interp(prag, [v_sub[i], v_sub[i+1]], [t_sub[i], t_sub[i+1]])
        elif smer == 'pad' and v_sub[i] >= prag >= v_sub[i+1]:
            return np.interp(prag, [v_sub[i+1], v_sub[i]], [t_sub[i+1], t_sub[i]])
    return None

# Automatski nalazimo vremena za RAST (izlaz raste nakon 100ps)
tr_10 = nadji_presek(t, v_out, 0.15, 'rast', 80)
tr_90 = nadji_presek(t, v_out, 1.35, 'rast', 80)

# Automatski nalazimo vremena za PAD (izlaz pada nakon 200ps)
tf_90 = nadji_presek(t, v_out, 1.35, 'pad', 180)
tf_10 = nadji_presek(t, v_out, 0.15, 'pad', 180)

# 2. Kreiranje grafika 
fig, ax = plt.subplots(figsize=(12, 6))

# Crtanje signala
ax.plot(t, v_in, color='#d62728', linewidth=2, linestyle='--', label='Ulaz A (Pobuda)')
ax.plot(t, v_out, color='#2ca02c', linewidth=3, label='Izlaz F (Odziv)')

# 3. Pragovi merenja (10% i 90%)
ax.axhline(0.15, color='blue', linestyle='--', linewidth=1.5, alpha=0.7, label='10% $V_{DD}$ (0.15V)')
ax.axhline(1.35, color='blue', linestyle='--', linewidth=1.5, alpha=0.7, label='90% $V_{DD}$ (1.35V)')

# 4. === AUTOMATSKO KOTIRANJE "OD DO" ===
visina_kote = 0.75 

# --- Kotiranje za RAST (tr) ---
ax.annotate('', xy=(tr_10, visina_kote), xytext=(tr_90, visina_kote),
            arrowprops=dict(arrowstyle='<|-|>', color='black', lw=1.5))
# Vertikalni graničnici od preseka do kote
ax.plot([tr_10, tr_10], [0.15, visina_kote], color='black', linestyle=':', lw=1.5)
ax.plot([tr_90, tr_90], [visina_kote, 1.35], color='black', linestyle=':', lw=1.5)
# Tekst (vrednost vučemo iz tvoje tabele za odnos 2.0)
# Python sam računa razliku u vremenu i zaokružuje na jednu decimalu!
ax.text((tr_10 + tr_90)/2, visina_kote + 0.08, rf'$t_r = {(tr_90 - tr_10):.1f}$ ps', 
        ha='center', va='bottom', fontsize=12, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))

# --- Kotiranje za PAD (tf) ---
ax.annotate('', xy=(tf_90, visina_kote), xytext=(tf_10, visina_kote),
            arrowprops=dict(arrowstyle='<|-|>', color='black', lw=1.5))
# Vertikalni graničnici od preseka do kote
ax.plot([tf_90, tf_90], [visina_kote, 1.35], color='black', linestyle=':', lw=1.5)
ax.plot([tf_10, tf_10], [0.15, visina_kote], color='black', linestyle=':', lw=1.5)
# Tekst (vrednost vučemo iz tvoje tabele za odnos 2.0)
# Python sam računa razliku u vremenu
ax.text((tf_90 + tf_10)/2, visina_kote + 0.08, rf'$t_f = {(tf_10 - tf_90):.1f}$ ps', 
        ha='center', va='bottom', fontsize=12, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8))

# 5. Ulepšavanje
ax.set_title('Tranzijentni odziv: Vremena rasta i pada (Odnos $W_p / W_n = 1.8$)', fontsize=14, fontweight='bold', pad=15)
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
plt.savefig('odziv_1_8.svg', format='svg', bbox_inches='tight')
plt.show()
