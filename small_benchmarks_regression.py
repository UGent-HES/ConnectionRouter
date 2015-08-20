import subprocess
def ppr_blif_6(ciruit):
	ppr("vtr_flow/benchmarks/blif/6/"+ciruit)

def ppr(circuitpath):
        print("circuit:"+circuitpath)
        outputfile = "small_benchmarks_regression.txt"
        f = open(outputfile,"a")
        f.write("circuit:"+circuitpath+"\n")
        f.close
        vpr = "vpr/vpr "
        archfile = " vtr_flow/arch/timing/k6_N10_40nm.xml "
        options = " -router_algorithm timing_driven_conr -first_iter_pres_fac 0.5 -initial_pres_fac 0.5 "
#        subprocess.call(vpr+archfile+circuitpath+options+" 2>&1 ", shell=True)
#        print(vpr+archfile+circuitpath+options)
        subprocess.call(vpr+archfile+circuitpath+options+" >> "+outputfile, shell=True)

ppr_blif_6("b1")
ppr_blif_6("majority")
ppr_blif_6("con1")
ppr_blif_6("shiftreg")
ppr_blif_6("xor5")
ppr_blif_6("cm152a")
ppr_blif_6("C17")
ppr_blif_6("cm151a")
ppr_blif_6("daio")
ppr_blif_6("cm82a")
ppr_blif_6("lion")
ppr_blif_6("dk27")
ppr_blif_6("mux")
ppr_blif_6("cm85a")
ppr_blif_6("cm150a")
ppr_blif_6("parity")
ppr_blif_6("mc")
ppr_blif_6("rd53")
ppr_blif_6("tcon")
ppr_blif_6("z4ml")
ppr_blif_6("cm163a")
ppr_blif_6("cm42a")
ppr_blif_6("cmb")
ppr_blif_6("bbtas")
ppr_blif_6("tav")
ppr_blif_6("squar5")
ppr_blif_6("s27")
ppr_blif_6("decod")
ppr_blif_6("cu")
ppr_blif_6("dk512")
ppr_blif_6("dk17")
ppr_blif_6("x2")
ppr_blif_6("cm138a")
ppr_blif_6("pm1")
ppr_blif_6("cm162a")
ppr_blif_6("dk15")
ppr_blif_6("misex1")
ppr_blif_6("pcle")
ppr_blif_6("beecount")
ppr_blif_6("i1")
ppr_blif_6("cc")
ppr_blif_6("s208")
ppr_blif_6("sqrt8")
ppr_blif_6("unreg")
ppr_blif_6("sqrt8ml")
ppr_blif_6("misex2")
ppr_blif_6("sct")
ppr_blif_6("f51m")
ppr_blif_6("s208")
ppr_blif_6("dk14")
ppr_blif_6("comp")
ppr_blif_6("ldd")
ppr_blif_6("pcler8")
ppr_blif_6("s420")
ppr_blif_6("lal")
ppr_blif_6("5xp1")
ppr_blif_6("frg1")
ppr_blif_6("ex4")
ppr_blif_6("c8")
ppr_blif_6("bbara")
ppr_blif_6("cht")
ppr_blif_6("b9")
ppr_blif_6("b12")
ppr_blif_6("mark1")
ppr_blif_6("inc")
ppr_blif_6("traffic")
ppr_blif_6("count")
ppr_blif_6("vg2")
ppr_blif_6("opus")
ppr_blif_6("ex6")
ppr_blif_6("ttt2")
ppr_blif_6("9symml")
ppr_blif_6("s526n")
ppr_blif_6("bw")
ppr_blif_6("s420")
ppr_blif_6("s526")
ppr_blif_6("mult16b")
ppr_blif_6("sse")
ppr_blif_6("s444")
ppr_blif_6("s349")
ppr_blif_6("s344")
ppr_blif_6("s386")
ppr_blif_6("bbsse")
ppr_blif_6("o64")
ppr_blif_6("my-adder")
ppr_blif_6("s382")
ppr_blif_6("s400")
ppr_blif_6("dk16")
ppr_blif_6("rd73")
ppr_blif_6("mm4a")
ppr_blif_6("term1")
ppr_blif_6("cse")
ppr_blif_6("sao2")
ppr_blif_6("mult16a")
ppr_blif_6("i3")
ppr_blif_6("pma")
ppr_blif_6("9sym")
ppr_blif_6("s510")
ppr_blif_6("x1")
ppr_blif_6("s641")
ppr_blif_6("s713")
ppr_blif_6("apex7")
ppr_blif_6("keyb")
ppr_blif_6("i4")
ppr_blif_6("tbk")
ppr_blif_6("example2")
ppr_blif_6("clip")
ppr_blif_6("s838")
ppr_blif_6("s838")
ppr_blif_6("s820")
ppr_blif_6("ex1")
ppr_blif_6("x4")
ppr_blif_6("s832")
ppr_blif_6("i2")
ppr_blif_6("mm9a")
ppr_blif_6("too-lrg")
ppr_blif_6("i6")
ppr_blif_6("i5")
ppr_blif_6("C432")
ppr_blif_6("alu2")
ppr_blif_6("C499")
ppr_blif_6("rd84")
ppr_blif_6("mult32a")
ppr_blif_6("t481")
ppr_blif_6("C1355")
ppr_blif_6("mm9b")
ppr_blif_6("i7")
ppr_blif_6("s1")
ppr_blif_6("s1196")
ppr_blif_6("s1238")
ppr_blif_6("duke2")
ppr_blif_6("i9")
ppr_blif_6("styr")
ppr_blif_6("C1908")
ppr_blif_6("e64")
ppr_blif_6("sand")
ppr_blif_6("C880")
ppr_blif_6("s953")
ppr_blif_6("vda")
ppr_blif_6("rot")
ppr_blif_6("planet")
ppr_blif_6("planet1")
ppr_blif_6("ph-decod")
ppr_blif_6("s1488")
ppr_blif_6("s1423")
ppr_blif_6("s1494")
ppr_blif_6("x3")
ppr_blif_6("gcd")
ppr_blif_6("apex6")
ppr_blif_6("ex4p")
ppr_blif_6("frg2")
ppr_blif_6("ecc")
ppr_blif_6("C2670")
ppr_blif_6("daio-rec")
ppr_blif_6("scf")
ppr_blif_6("cordic")
ppr_blif_6("k2")
ppr_blif_6("misex3c")
ppr_blif_6("table3")
ppr_blif_6("table5")
ppr_blif_6("bbrtas")
ppr_blif_6("apex5")
ppr_blif_6("dalu")
ppr_blif_6("s9234")
ppr_blif_6("sbc")
ppr_blif_6("mm30a")
ppr_blif_6("pair")
ppr_blif_6("i8")
ppr_blif_6("C3540")
ppr_blif_6("apex1")
ppr_blif_6("cps")
ppr_blif_6("s5378")
ppr_blif_6("apex3")
ppr_blif_6("C5315")
ppr_blif_6("parker1986")
ppr_blif_6("misex3")
ppr_blif_6("C7552")
ppr_blif_6("apex4")
ppr_blif_6("des")
ppr_blif_6("ex5p")
ppr_blif_6("i10")
ppr_blif_6("alu4")
ppr_blif_6("bigkey")
ppr_blif_6("dsip")
ppr_blif_6("tseng")
ppr_blif_6("C6288")
ppr_blif_6("seq")
ppr_blif_6("diffeq")
ppr_blif_6("apex2")
ppr_blif_6("s298")
ppr_blif_6("elliptic")
ppr_blif_6("ex1010")
ppr_blif_6("spla")
ppr_blif_6("frisc")
ppr_blif_6("s38417")
ppr_blif_6("pdc")
ppr_blif_6("s38584")
ppr_blif_6("clma")
