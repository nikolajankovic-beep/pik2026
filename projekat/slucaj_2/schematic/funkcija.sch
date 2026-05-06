v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 750 -460 750 -410 {
lab=ground}
N 950 -410 1090 -410 {
lab=ground}
N 1090 -460 1090 -410 {
lab=ground}
N 920 -460 920 -410 {
lab=ground}
N 780 -410 920 -410 {
lab=ground}
N 750 -490 780 -490 {
lab=ground}
N 780 -490 780 -410 {
lab=ground}
N 750 -410 780 -410 {
lab=ground}
N 920 -490 950 -490 {
lab=ground}
N 950 -490 950 -410 {
lab=ground}
N 920 -410 950 -410 {
lab=ground}
N 1080 -490 1120 -490 {
lab=ground}
N 1120 -490 1120 -410 {
lab=ground}
N 1090 -410 1120 -410 {
lab=ground}
N 1090 -550 1090 -520 {
lab=#net1}
N 1090 -620 1150 -620 {
lab=ground}
N 1150 -620 1150 -410 {
lab=ground}
N 1120 -410 1150 -410 {
lab=ground}
N 1090 -830 1090 -720 {
lab=out}
N 820 -980 820 -950 {
lab=vdd}
N 960 -980 1090 -980 {
lab=vdd}
N 1090 -980 1090 -890 {
lab=vdd}
N 820 -890 820 -870 {
lab=#net2}
N 820 -810 820 -780 {
lab=#net3}
N 1090 -860 1130 -860 {
lab=vdd}
N 1130 -980 1130 -860 {
lab=vdd}
N 1090 -980 1130 -980 {
lab=vdd}
N 820 -920 860 -920 {
lab=vdd}
N 860 -980 860 -920 {
lab=vdd}
N 820 -980 860 -980 {
lab=vdd}
N 820 -840 890 -840 {
lab=vdd}
N 890 -980 890 -840 {
lab=vdd}
N 860 -980 890 -980 {
lab=vdd}
N 820 -750 930 -750 {
lab=vdd}
N 930 -980 930 -750 {
lab=vdd}
N 890 -980 930 -980 {
lab=vdd}
N 750 -550 750 -520 {
lab=#net1}
N 920 -550 1090 -550 {
lab=#net1}
N 1090 -590 1090 -550 {
lab=#net1}
N 920 -550 920 -520 {
lab=#net1}
N 750 -550 920 -550 {
lab=#net1}
N 860 -490 880 -490 {
lab=b}
N 660 -490 710 -490 {
lab=a}
N 1040 -490 1050 -490 {
lab=c}
N 1020 -620 1050 -620 {
lab=d}
N 950 -410 950 -390 {
lab=ground}
N 740 -750 780 -750 {
lab=c}
N 750 -840 780 -840 {
lab=b}
N 750 -920 780 -920 {
lab=a}
N 1030 -860 1050 -860 {
lab=d}
N 960 -1010 960 -980 {
lab=vdd}
N 930 -980 960 -980 {
lab=vdd}
N 820 -720 1090 -720 {
lab=out}
N 1090 -720 1090 -650 {
lab=out}
N 1090 -720 1240 -720 {
lab=out}
C {sg13g2_pr/sg13_lv_nmos.sym} 730 -490 0 0 {name=M1
l=0.13u
w=0.3u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 900 -490 0 0 {name=M2
l=0.13u
w=0.3u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 1070 -490 0 0 {name=M3
l=0.13u
w=0.3u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 1070 -620 0 0 {name=M4
l=0.13u
w=0.3u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 800 -920 0 0 {name=M5
l=0.13u
w=0.9u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 800 -840 0 0 {name=M6
l=0.13u
w=0.9u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 800 -750 0 0 {name=M7
l=0.13u
w=0.9u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 1070 -860 0 0 {name=M8
l=0.13u
w=0.3u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {ipin.sym} 660 -490 0 0 {name=p1 lab=a}
C {ipin.sym} 860 -490 0 0 {name=p2 lab=b}
C {ipin.sym} 1040 -490 0 0 {name=p3 lab=c
}
C {ipin.sym} 1020 -620 0 0 {name=p4 lab=d
}
C {lab_pin.sym} 740 -750 0 0 {name=p5 sig_type=std_logic lab=c}
C {lab_pin.sym} 750 -840 0 0 {name=p6 sig_type=std_logic lab=b}
C {lab_pin.sym} 750 -920 0 0 {name=p7 sig_type=std_logic lab=a}
C {lab_pin.sym} 1030 -860 0 0 {name=p8 sig_type=std_logic lab=d}
C {iopin.sym} 960 -1010 3 0 {name=p9 lab=vdd}
C {iopin.sym} 950 -390 1 0 {name=p10 lab=ground}
C {opin.sym} 1240 -720 0 0 {name=p11 lab=out}
