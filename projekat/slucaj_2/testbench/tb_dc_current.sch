v {xschem version=3.4.5 file_version=1.2
}
G {}
K {}
V {}
S {}
E {}
T {Schematic level testbench
Non matching
DC Current} 190 -670 0 0 0.4 0.4 {}
N 290 -500 520 -500 {
lab=a}
N 290 -500 290 -480 {
lab=a}
N 350 -480 520 -480 {
lab=b}
N 350 -480 350 -460 {
lab=b}
N 410 -460 520 -460 {
lab=c}
N 410 -460 410 -440 {
lab=c}
N 480 -440 520 -440 {
lab=d}
N 480 -440 480 -420 {
lab=d}
N 820 -480 850 -480 {
lab=out}
N 640 -580 650 -580 {
lab=#net1}
N 650 -580 650 -530 {
lab=#net1}
N 550 -580 580 -580 {
lab=GND}
N 550 -580 550 -570 {
lab=GND}
N 480 -360 480 -340 {
lab=GND}
N 410 -380 410 -350 {
lab=GND}
N 350 -400 350 -360 {
lab=GND}
N 290 -420 290 -370 {
lab=GND}
N 690 -410 690 -400 {
lab=GND}
N 680 -410 690 -410 {
lab=GND}
C {vsource.sym} 290 -450 0 0 {name=Va value="PULSE(0 1.5 0 100p 100p 200p 500p)" savecurrent=false}
C {vsource.sym} 350 -430 0 0 {name=Vb value=0 savecurrent=false}
C {vsource.sym} 410 -410 0 0 {name=Vc value=0 savecurrent=false}
C {vsource.sym} 480 -390 0 0 {name=Vd value=1.5 savecurrent=false}
C {vsource.sym} 610 -580 1 0 {name=Vdd value=1.5 savecurrent=false}
C {gnd.sym} 290 -370 0 0 {name=l1 lab=GND}
C {gnd.sym} 350 -360 0 0 {name=l2 lab=GND}
C {gnd.sym} 410 -350 0 0 {name=l3 lab=GND}
C {gnd.sym} 480 -340 0 0 {name=l4 lab=GND}
C {gnd.sym} 550 -570 0 0 {name=l5 lab=GND}
C {simulator_commands_shown.sym} 70 -260 0 0 {
name=Libs_Ngspice
simulator=ngspice
only_toplevel=false
value="
.lib cornerMOSlv.lib mos_tt
.lib cornerMOShv.lib mos_tt
.lib cornerHBT.lib hbt_typ
.lib cornerRES.lib res_typ
"
      }
C {simulator_commands_shown.sym} 430 -220 0 0 {
name=Libs_Xyce
simulator=xyce
only_toplevel=false
value="tcleval(
.lib $::SG13G2_MODELS_XYCE/cornerMOSlv.lib mos_tt
.lib $::SG13G2_MODELS_XYCE/cornerMOShv.lib mos_tt
.lib $::SG13G2_MODELS_XYCE/cornerHBT.lib hbt_typ
.lib $::SG13G2_MODELS_XYCE/cornerRES.lib res_typ
)"
      }
C {gnd.sym} 690 -400 0 0 {name=l7 lab=GND}
C {lab_pin.sym} 850 -480 2 0 {name=p1 sig_type=std_logic lab=out}
C {lab_pin.sym} 290 -500 0 0 {name=p2 sig_type=std_logic lab=a}
C {lab_pin.sym} 350 -480 0 0 {name=p3 sig_type=std_logic lab=b}
C {lab_pin.sym} 410 -460 0 0 {name=p4 sig_type=std_logic lab=c}
C {lab_pin.sym} 480 -440 0 0 {name=p5 sig_type=std_logic lab=d}
C {devices/code.sym} 70 -530 0 0 {name=NGSPICE only_toplevel=false value="
* DC sweep ulaznog napona Va od 0 do 1.5V sa korakom 0.01V

.dc Va 0 1.5 0.01

.control
  run
  
  wrdata /home/Nikola.Jankovic/projekat/slucaj_2/python/struja.txt v(a) i(Vdd)
  
  plot -i(Vdd)
.endc"}
C {/home/Nikola.Jankovic/projekat/slucaj_2/schematic/funkcija.sym} 670 -470 0 0 {name=x1}
