v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
N 530 -250 530 -200 {
lab=ground}
N 730 -200 870 -200 {
lab=ground}
N 870 -250 870 -200 {
lab=ground}
N 700 -250 700 -200 {
lab=ground}
N 560 -200 700 -200 {
lab=ground}
N 530 -280 560 -280 {
lab=ground}
N 560 -280 560 -200 {
lab=ground}
N 530 -200 560 -200 {
lab=ground}
N 700 -280 730 -280 {
lab=ground}
N 730 -280 730 -200 {
lab=ground}
N 700 -200 730 -200 {
lab=ground}
N 860 -280 900 -280 {
lab=ground}
N 900 -280 900 -200 {
lab=ground}
N 870 -200 900 -200 {
lab=ground}
N 870 -340 870 -310 {
lab=#net1}
N 870 -410 930 -410 {
lab=ground}
N 930 -410 930 -200 {
lab=ground}
N 900 -200 930 -200 {
lab=ground}
N 870 -510 870 -440 {
lab=out}
N 870 -620 870 -510 {
lab=out}
N 600 -770 600 -740 {
lab=vdd}
N 740 -770 870 -770 {
lab=vdd}
N 870 -770 870 -680 {
lab=vdd}
N 600 -680 600 -660 {
lab=#net2}
N 600 -600 600 -570 {
lab=#net3}
N 870 -650 910 -650 {
lab=vdd}
N 910 -770 910 -650 {
lab=vdd}
N 870 -770 910 -770 {
lab=vdd}
N 600 -710 640 -710 {
lab=vdd}
N 640 -770 640 -710 {
lab=vdd}
N 600 -770 640 -770 {
lab=vdd}
N 600 -630 670 -630 {
lab=vdd}
N 670 -770 670 -630 {
lab=vdd}
N 640 -770 670 -770 {
lab=vdd}
N 600 -540 710 -540 {
lab=vdd}
N 710 -770 710 -540 {
lab=vdd}
N 670 -770 710 -770 {
lab=vdd}
N 600 -510 870 -510 {
lab=out}
N 870 -510 1020 -510 {
lab=out}
N 530 -340 530 -310 {
lab=#net1}
N 700 -340 870 -340 {
lab=#net1}
N 870 -380 870 -340 {
lab=#net1}
N 700 -340 700 -310 {
lab=#net1}
N 530 -340 700 -340 {
lab=#net1}
N 640 -280 660 -280 {
lab=b}
N 440 -280 490 -280 {
lab=a}
N 820 -280 830 -280 {
lab=c}
N 800 -410 830 -410 {
lab=d}
N 730 -200 730 -180 {
lab=ground}
N 520 -540 560 -540 {
lab=c}
N 530 -630 560 -630 {
lab=b}
N 530 -710 560 -710 {
lab=a}
N 810 -650 830 -650 {
lab=d}
N 740 -800 740 -770 {
lab=vdd}
N 710 -770 740 -770 {
lab=vdd}
C {sg13g2_pr/sg13_lv_nmos.sym} 510 -280 0 0 {name=M1
l=0.13u
w=0.3u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 680 -280 0 0 {name=M2
l=0.13u
w=0.3u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 850 -280 0 0 {name=M3
l=0.13u
w=0.3u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_nmos.sym} 850 -410 0 0 {name=M4
l=0.13u
w=0.3u
ng=1
m=1
model=sg13_lv_nmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 580 -710 0 0 {name=M5
l=0.13u
w=1.125u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 580 -630 0 0 {name=M6
l=0.13u
w=1.125u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 580 -540 0 0 {name=M7
l=0.13u
w=1.125u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {sg13g2_pr/sg13_lv_pmos.sym} 850 -650 0 0 {name=M8
l=0.13u
w=0.375u
ng=1
m=1
model=sg13_lv_pmos
spiceprefix=X
}
C {ipin.sym} 440 -280 0 0 {name=p1 lab=a}
C {ipin.sym} 640 -280 0 0 {name=p2 lab=b}
C {ipin.sym} 820 -280 0 0 {name=p3 lab=c
}
C {ipin.sym} 800 -410 0 0 {name=p4 lab=d
}
C {lab_pin.sym} 520 -540 0 0 {name=p5 sig_type=std_logic lab=c}
C {lab_pin.sym} 530 -630 0 0 {name=p6 sig_type=std_logic lab=b}
C {lab_pin.sym} 530 -710 0 0 {name=p7 sig_type=std_logic lab=a}
C {lab_pin.sym} 810 -650 0 0 {name=p8 sig_type=std_logic lab=d}
C {iopin.sym} 740 -800 3 0 {name=p9 lab=vdd}
C {iopin.sym} 730 -180 1 0 {name=p10 lab=ground}
C {opin.sym} 1020 -510 0 0 {name=p11 lab=out}
