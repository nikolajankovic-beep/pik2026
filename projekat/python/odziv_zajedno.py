import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

podaci_20 = np.loadtxt('/home/Nikola.Jankovic/projekat/slucaj_2/python/odziv_2.txt') 
podaci_25 = np.loadtxt('/home/Nikola.Jankovic/projekat/slucaj_2_5/python/odziv_2_5.txt') 
podaci_30 = np.loadtxt('/home/Nikola.Jankovic/projekat/slucaj_3/python/odziv_3.txt') 

t_20 = podaci_20[:, 0] * 1e12  
v_in = podaci_20[:, 1]          
v_out_20 = podaci_20[:, 3]        

t_25 = podaci_25[:, 0] * 1e12  
v_out_25 = podaci_25[:, 3]

t_30 = podaci_30[:, 0] * 1e12  
v_out_30 = podaci_30[:, 3]

boja_20 = 'blue'   
boja_25 = 'red'     
boja_30 = 'green'   

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(t_20, v_in, color='black', linewidth=1.5, linestyle='--', label='Ulaz A (Zajednički)')

ax.plot(t_20, v_out_20, color=boja_20, linewidth=2.5, label='Izlaz F ($W_p/W_n = 2.0$)') 
ax.plot(t_25, v_out_25, color=boja_25, linewidth=2.5, label='Izlaz F ($W_p/W_n = 2.5$)') 
ax.plot(t_30, v_out_30, color=boja_30, linewidth=2.5, label='Izlaz F ($W_p/W_n = 3.0$)') 

ax.axhline(0.15, color='gray', linestyle=':', linewidth=1.5, alpha=0.7)
ax.axhline(1.35, color='gray', linestyle=':', linewidth=1.5, alpha=0.7)
ax.text(5, 0.17, '10% $V_{DD}$', fontsize=10, color='gray', fontweight='bold')
ax.text(5, 1.37, '90% $V_{DD}$', fontsize=10, color='gray', fontweight='bold')


pocetak_rasta = np.argmax(t_20 > 80)

idx_20 = pocetak_rasta + np.argmax(v_out_20[pocetak_rasta:] > 1.1)   
idx_25 = pocetak_rasta + np.argmax(v_out_25[pocetak_rasta:] > 0.75) 
idx_30 = pocetak_rasta + np.argmax(v_out_30[pocetak_rasta:] > 0.4)   

x_tekst = 20
ax.annotate('$W_p/W_n = 2.0$', 
            xy=(t_20[idx_20], v_out_20[idx_20]), 
            xytext=(x_tekst, 1.25),
            arrowprops=dict(arrowstyle="-|>", color=boja_20, lw=2),
            fontsize=12, color='white', fontweight='bold', 
            bbox=dict(facecolor=boja_20, edgecolor='none', boxstyle='round,pad=0.4', alpha=0.9))

ax.annotate('$W_p/W_n = 2.5$', 
            xy=(t_25[idx_25], v_out_25[idx_25]), 
            xytext=(x_tekst, 0.75),
            arrowprops=dict(arrowstyle="-|>", color=boja_25, lw=2),
            fontsize=12, color='white', fontweight='bold', 
            bbox=dict(facecolor=boja_25, edgecolor='none', boxstyle='round,pad=0.4', alpha=0.9))

ax.annotate('$W_p/W_n = 3.0$', 
            xy=(t_30[idx_30], v_out_30[idx_30]), 
            xytext=(x_tekst, 0.25),
            arrowprops=dict(arrowstyle="-|>", color=boja_30, lw=2),
            fontsize=12, color='white', fontweight='bold', 
            bbox=dict(facecolor=boja_30, edgecolor='none', boxstyle='round,pad=0.4', alpha=0.9))

ax.set_title('Uporedni tranzijentni odziv za različite odnose $W_p / W_n$', fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel('Vreme [ps]', fontsize=14)
ax.set_ylabel('Napon [V]', fontsize=14)

ax.set_ylim(-0.1, 1.8)
ax.set_xlim(0, 450)

ax.grid(True, linestyle='--', alpha=0.5)
ax.xaxis.set_major_locator(ticker.MultipleLocator(100))
ax.yaxis.set_major_locator(ticker.MultipleLocator(0.3))

ax.legend(loc='lower right', fontsize=11, frameon=True, edgecolor='black', framealpha=0.9)

plt.tight_layout()
plt.savefig('/home/Nikola.Jankovic/projekat/python/odziv_zajedno.svg', format='svg', bbox_inches='tight')
plt.show()
