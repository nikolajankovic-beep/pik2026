import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def nadji_presek(vreme, napon, prag, smer, pocetno_vreme):
    idx = np.where(vreme > pocetno_vreme)[0]
    t_sub, v_sub = vreme[idx], napon[idx]
    for i in range(len(v_sub)-1):
        if smer == 'rast' and v_sub[i] <= prag <= v_sub[i+1]:
            return np.interp(prag, [v_sub[i], v_sub[i+1]], [t_sub[i], t_sub[i+1]])
        elif smer == 'pad' and v_sub[i] >= prag >= v_sub[i+1]:
            return np.interp(prag, [v_sub[i+1], v_sub[i]], [t_sub[i+1], t_sub[i]])
    return None

podaci_u = np.loadtxt('/home/Nikola.Jankovic/projekat/slucaj_2/pex/python/odziv_nonmatch.txt') 
t_u = podaci_u[:, 0] * 1e12  
v_in = podaci_u[:, 1]        
v_out_u = podaci_u[:, 3]     

podaci_m = np.loadtxt('/home/Nikola.Jankovic/projekat/slucaj_2/pex/python/odziv_match.txt') 
t_m = podaci_m[:, 0] * 1e12  

v_out_m = podaci_m[:, 3]     

tr_10_u = nadji_presek(t_u, v_out_u, 0.15, 'rast', 80)
tr_90_u = nadji_presek(t_u, v_out_u, 1.35, 'rast', 80)
tf_90_u = nadji_presek(t_u, v_out_u, 1.35, 'pad', 180)
tf_10_u = nadji_presek(t_u, v_out_u, 0.15, 'pad', 180)

tr_10_m = nadji_presek(t_m, v_out_m, 0.15, 'rast', 80)
tr_90_m = nadji_presek(t_m, v_out_m, 1.35, 'rast', 80)
tf_90_m = nadji_presek(t_m, v_out_m, 1.35, 'pad', 180)
tf_10_m = nadji_presek(t_m, v_out_m, 0.15, 'pad', 180)

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(t_u, v_in, color='#d62728', linewidth=2, linestyle='--', label='Ulaz A (Pobuda)')

boja_u = '#1f77b4'
ax.plot(t_u, v_out_u, color=boja_u, linewidth=2.5, label='Izlaz F (Without Matching)')

boja_m = '#2ca02c'
ax.plot(t_m, v_out_m, color=boja_m, linewidth=2.5, linestyle='-.', label='Izlaz F (With Matching)')

ax.axhline(0.15, color='gray', linestyle='--', linewidth=1.2, alpha=0.7)
ax.axhline(1.35, color='gray', linestyle='--', linewidth=1.2, alpha=0.7)

visina_u = 0.60
visina_m = 0.90


ax.annotate('', xy=(tr_10_u, visina_u), xytext=(tr_90_u, visina_u), arrowprops=dict(arrowstyle='<|-|>', color=boja_u, lw=1.5))
ax.plot([tr_10_u, tr_10_u], [0.15, visina_u], color=boja_u, linestyle=':', lw=1.2, alpha=0.7)
ax.plot([tr_90_u, tr_90_u], [visina_u, 1.35], color=boja_u, linestyle=':', lw=1.2, alpha=0.7)
ax.text((tr_10_u + tr_90_u)/2, visina_u - 0.05, rf'$t_r = {(tr_90_u - tr_10_u):.1f}$ ps', 
        ha='center', va='top', color=boja_u, fontsize=11, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))

ax.annotate('', xy=(tr_10_m, visina_m), xytext=(tr_90_m, visina_m), arrowprops=dict(arrowstyle='<|-|>', color=boja_m, lw=1.5))
ax.plot([tr_10_m, tr_10_m], [0.15, visina_m], color=boja_m, linestyle=':', lw=1.2, alpha=0.7)
ax.plot([tr_90_m, tr_90_m], [visina_m, 1.35], color=boja_m, linestyle=':', lw=1.2, alpha=0.7)
ax.text((tr_10_m + tr_90_m)/2, visina_m + 0.05, rf'$t_r = {(tr_90_m - tr_10_m):.1f}$ ps', 
        ha='center', va='bottom', color=boja_m, fontsize=11, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))

ax.annotate('', xy=(tf_90_u, visina_u), xytext=(tf_10_u, visina_u), arrowprops=dict(arrowstyle='<|-|>', color=boja_u, lw=1.5))
ax.plot([tf_90_u, tf_90_u], [visina_u, 1.35], color=boja_u, linestyle=':', lw=1.2, alpha=0.7)
ax.plot([tf_10_u, tf_10_u], [0.15, visina_u], color=boja_u, linestyle=':', lw=1.2, alpha=0.7)
ax.text((tf_90_u + tf_10_u)/2, visina_u - 0.05, rf'$t_f = {(tf_10_u - tf_90_u):.1f}$ ps', 
        ha='center', va='top', color=boja_u, fontsize=11, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))

ax.annotate('', xy=(tf_90_m, visina_m), xytext=(tf_10_m, visina_m), arrowprops=dict(arrowstyle='<|-|>', color=boja_m, lw=1.5))
ax.plot([tf_90_m, tf_90_m], [visina_m, 1.35], color=boja_m, linestyle=':', lw=1.2, alpha=0.7)
ax.plot([tf_10_m, tf_10_m], [0.15, visina_m], color=boja_m, linestyle=':', lw=1.2, alpha=0.7)
ax.text((tf_90_m + tf_10_m)/2, visina_m + 0.05, rf'$t_f = {(tf_10_m - tf_90_m):.1f}$ ps', 
        ha='center', va='bottom', color=boja_m, fontsize=11, fontweight='bold', bbox=dict(facecolor='white', edgecolor='none', alpha=0.8, pad=1))

ax.set_title(r'Tranzijentna analiza: Poređenje odziva (Odnos $W_p / W_n = 2$)' + '\n' + 'Postlayout-PEX', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Vreme [ps]', fontsize=12)
ax.set_ylabel('Napon [V]', fontsize=12)

ax.set_ylim(-0.2, 1.8)
ax.set_xlim(0, 500)

ax.grid(True, linestyle=':', alpha=0.6)
ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.3))

ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.12), ncol=3, fontsize=11, frameon=True, edgecolor='black', framealpha=0.9)

plt.tight_layout()
plt.savefig('/home/Nikola.Jankovic/projekat/slucaj_2/pex/python/odziv_zajedno.svg', format='svg', bbox_inches='tight')
plt.show()
