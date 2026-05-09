import numpy as np
import matplotlib.pyplot as plt

putanja_do_fajla = '/home/Nikola.Jankovic/projekat/slucaj_2/python/vtc_kriva.txt'
podaci = np.loadtxt(putanja_do_fajla)
Va = podaci[:, 0]
Vout = podaci[:, 1]

izvod = np.gradient(Vout, Va)
indeks_min_izvoda = np.argmin(izvod)

indeks_vil = np.argmin(np.abs(izvod[:indeks_min_izvoda] - (-1)))
Vil = Va[indeks_vil]
Vout_vil = Vout[indeks_vil]

indeks_vih = np.argmin(np.abs(izvod[indeks_min_izvoda:] - (-1))) + indeks_min_izvoda
Vih = Va[indeks_vih]
Vout_vih = Vout[indeks_vih]

Voh = np.max(Vout)
Vol = np.min(Vout)

NM_L = Vil - Vol
NM_H = Voh - Vih
delta_VI = Vih - Vil

V_prava = -Va + Voh + Vol

maska = (Va > Vil) & (Va < Vih)
indeks_vt = np.argmin(np.abs(Vout[maska] - V_prava[maska]))

stvarn_indeks_vt = np.where(maska)[0][indeks_vt] 
Vt = Va[stvarn_indeks_vt]
Vt_out = Vout[stvarn_indeks_vt]

plt.figure(figsize=(12, 8)) 


plt.plot(Va, Vout, color='#0033A0', linewidth=2.5, label='Prenosna karakteristika $V_O(V_I)$')
plt.plot(Va, V_prava, color='gray', linestyle='-.', linewidth=1.5, label='Prava kroz $P_0$ i $P_1$')


plt.fill_between(Va, 0, 1.55, where=((Va >= Vil) & (Va <= Vih)), color='gray', alpha=0.15)


plt.vlines(x=Vil, ymin=0, ymax=Vout_vil, color='black', linestyle='--', alpha=0.7)
plt.vlines(x=Vih, ymin=0, ymax=Vout_vih, color='black', linestyle='--', alpha=0.7)


plt.plot(Vil, Vout_vil, 'ko', markersize=5)
plt.annotate('A ($A_v = -1$)', xy=(Vil, Vout_vil), xytext=(Vil - 0.2, Vout_vil - 0.15),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.2), fontsize=11, fontweight='bold')

plt.plot(Vih, Vout_vih, 'ko', markersize=5)
plt.annotate('B ($A_v = -1$)', xy=(Vih, Vout_vih), xytext=(Vih + 0.05, Vout_vih + 0.15),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.2), fontsize=11, fontweight='bold')

plt.plot(Vt, Vt_out, 'ro', markersize=6, zorder=5) 
plt.annotate(f'T ($V_T$={Vt:.2f}V)', xy=(Vt, Vt_out), xytext=(Vt + 0.08, Vt_out + 0.1),
             arrowprops=dict(color='red', arrowstyle='->', lw=1.2), color='red', fontsize=12, fontweight='bold')


plt.annotate('', xy=(0, 0.05), xytext=(Vil, 0.05), arrowprops=dict(arrowstyle='<->', lw=1.5))
plt.text(Vil/2, 0.07, f'$NM_L$={NM_L:.2f}V\n(Oblast logičke 0)', ha='center', va='bottom', fontsize=10)

plt.annotate('', xy=(Vih, 0.05), xytext=(1.5, 0.05), arrowprops=dict(arrowstyle='<->', lw=1.5))
plt.text((Vih+1.5)/2, 0.07, f'$NM_H$={NM_H:.2f}V\n(Oblast logičke 1)', ha='center', va='bottom', fontsize=10)

plt.annotate('', xy=(Vil, 1.45), xytext=(Vih, 1.45), arrowprops=dict(arrowstyle='<->', lw=1.5))
plt.text((Vil+Vih)/2, 1.47, f'Zabranjena zona\n$\\Delta V_I$={delta_VI:.2f}V', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.axhline(y=Voh, color='black', linestyle=':', alpha=0.3)
plt.text(0.01, Voh - 0.05, '$V_{OH}$', fontsize=11)
plt.axhline(y=0, color='black', linestyle=':', alpha=0.3) # VOL je prakticno nula
plt.text(0.01, 0.02, '$V_{OL}$', fontsize=11)

plt.title('Naponska prenosna karakteristika i statičke margine šuma', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Ulazni napon $V_I$ [V]', fontsize=12)
plt.ylabel('Izlazni napon $V_O$ [V]', fontsize=12)

plt.xlim([0, 1.5])
plt.ylim([-0.05, 1.6]) # Malo lufta gore i dole
plt.grid(True, linestyle='--', alpha=0.5)

plt.legend(loc='upper right', framealpha=0.9, edgecolor='black')

plt.tight_layout()
plt.savefig('/home/Nikola.Jankovic/projekat/slucaj_2/python/vtc_kriva.svg', format='svg')
plt.show()
