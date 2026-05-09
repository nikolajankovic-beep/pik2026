#!/bin/bash

echo "=========================================================="
echo " FAZA 1: POKRETANJE NGSPICE SIMULACIJA"
echo "=========================================================="

echo "Simuliram odziv_1_8..."
ngspice -b /home/Nikola.Jankovic/projekat/slucaj_1_8/simulation/tb_tran.spice > /dev/null 2>&1
echo "Simuliram odziv_2..."
ngspice -b /home/Nikola.Jankovic/projekat/slucaj_2/simulation/tb_tran.spice > /dev/null 2>&1
#ngspice -b /home/Nikola.Jankovic/projekat/slucaj_2/simulation/tb_tran_matching.spice > /dev/null 2>&1
echo "Simuliram odziv_2_5..."
ngspice -b /home/Nikola.Jankovic/projekat/slucaj_2_5/simulation/tb_tran.spice > /dev/null 2>&1
echo "Simuliram odziv_3..."
ngspice -b /home/Nikola.Jankovic/projekat/slucaj_3/simulation/tb_tran.spice > /dev/null 2>&1
echo "Simuliram naponsku prenosnu karakterisitku..."
ngspice -b /home/Nikola.Jankovic/projekat/slucaj_2/simulation/vtc_kriva.spice  > /dev/null 2>&1
echo "Simuliram strujnu prenosnu karakterisitku..."
ngspice -b /home/Nikola.Jankovic/projekat/slucaj_2/simulation/struja.spice  > /dev/null 2>&1
echo "Simuliram postlayout - PEX - without matching..."
ngspice -b /home/Nikola.Jankovic/projekat/slucaj_2/pex/simulation/tb_tran.spice  > /dev/null 2>&1
echo "Simuliram postlayout - PEX - with matching..."
ngspice -b /home/Nikola.Jankovic/projekat/slucaj_2/pex/simulation/tb_tran_matching.spice  > /dev/null 2>&1


echo "Sve simulacije završene. Izlazne datoteke su kreirane."
echo ""

echo "=========================================================="
echo " FAZA 2: POKRETANJE PYTHON SKRIPTI "
echo "=========================================================="



echo "Crtam odziv_2..."
python /home/Nikola.Jankovic/projekat/slucaj_1_8/python/odziv_1_8.py
echo "Crtam odziv_2..."
python /home/Nikola.Jankovic/projekat/slucaj_2/python/odziv_2.py
#python /home/Nikola.Jankovic/projekat/slucaj_2/python/odziv_2_matching.py
echo "Crtam odziv_2_5..."
python /home/Nikola.Jankovic/projekat/slucaj_2_5/python/odziv_2_5.py
echo "Crtam odziv_3..."
python /home/Nikola.Jankovic/projekat/slucaj_3/python/odziv_3.py
echo "Crtam naponsku prenosnu karakteristiku..."
python /home/Nikola.Jankovic/projekat/slucaj_2/python/vtc_kriva.py
echo "Crtam strujnu prenosnu karakteristiku..."
python /home/Nikola.Jankovic/projekat/slucaj_2/python/struja.py
echo "Crtam odziv postlayout without matching"
python /home/Nikola.Jankovic/projekat/slucaj_2/pex/python/odziv_nonmatch.py
echo "Crtam odziv postlayout with matching"
python /home/Nikola.Jankovic/projekat/slucaj_2/pex/python/odziv_match.py

echo "Crtam zajedno odzive za razlicite odnose sirina pmos i nmos tranzistora"
python /home/Nikola.Jankovic/projekat/python/odziv_zajedno.py
echo "Crtam zajedno postlayout sa matchingom i bez matchinga "
python /home/Nikola.Jankovic/projekat/slucaj_2/pex/python/odziv_zajedno.py



echo "=========================================================="
echo " GOTOVO! Svi grafici su iscrtani i sačuvani.             "
echo "=========================================================="
