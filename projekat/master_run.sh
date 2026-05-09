#!/bin/bash

echo "=========================================================="
echo " FAZA 1: POKRETANJE NGSPICE SIMULACIJA (Fajl po fajl)     "
echo "=========================================================="

echo "Simuliram odziv_1_8..."
ngspice -b /home/Nikola.Jankovic/projekat/slucaj_1_8/simulation/tb_tran.spice > /dev/null 2>&1
echo "Simuliram odziv_2..."
ngspice -b /home/Nikola.Jankovic/projekat/slucaj_2/simulation/tb_tran.spice > /dev/null 2>&1
ngspice -b /home/Nikola.Jankovic/projekat/slucaj_2/simulation/tb_tran_matching.spice > /dev/null 2>&1

echo "Sve simulacije završene. Izlazne datoteke su kreirane."
echo ""

echo "=========================================================="
echo " FAZA 2: POKRETANJE PYTHON SKRIPTI (Fajl po fajl)         "
echo "=========================================================="

echo "Crtam odziv_2..."
python /home/Nikola.Jankovic/projekat/slucaj_1_8/python/odziv_1_8.py
echo "Crtam odziv_2..."
python /home/Nikola.Jankovic/projekat/slucaj_2/python/odziv_2.py
python /home/Nikola.Jankovic/projekat/slucaj_2/python/odziv_2_matching.py
echo "=========================================================="
echo " GOTOVO! Svi grafici su iscrtani i sačuvani.             "
echo "=========================================================="
