import os

#DIR_MADGRAPH = "/home/matheus/Documents/MG5_aMC_v2_8_3/"
DIR_MADGRAPH = "/media/matheus/789617339616F17C/Eventos/MG5_aMC_v2_8_3/"
DIR_PROC = "/home/matheus/Documents/repositorio/pdpd2020/proc.dat"
DIR_EVENTS = DIR_MADGRAPH + "bin/teste/"

def change_proc(lhs, mdm, nevents, ptj, reset=False, higgs=False):
    dir_events = "MDM" + str(mdm)
    if reset:
        with open("proc.dat", "r") as file_proc:
            lines = file_proc.readlines()
        with open("proc.dat", "w") as file_proc:
            for line in lines[:-8]:
                file_proc.write(line)
        return

    if higgs:
        with open("proc.dat", "a") as file_proc: 
            file_proc.write(f"generate p p > h j, h > sdm sdm\n")
    else:
        with open("proc.dat", "a") as file_proc: 
            file_proc.write(f"generate p p > sdm sdm j\n")

    with open("proc.dat", "a") as file_proc: 
        file_proc.write(f"output {DIR_MADGRAPH}bin/{dir_events}\n")
        file_proc.write(f"launch\n")
        file_proc.write(f"set lhs {lhs}\n")
        file_proc.write(f"set mdm {mdm}\n") 
        file_proc.write(f"set wh auto\n") 
        file_proc.write(f"set nevents {nevents}\n")
        file_proc.write(f"set ptj {ptj}")


def run_madgraph(lhs: float, mdmValues: list, nevents: int, ptj: float, higgs=False):
    # Generate proc.dat file
    for mass in mdmValues:
        change_proc(lhs, mass, nevents, ptj, higgs=higgs)
        os.system(DIR_MADGRAPH + "bin/mg5_aMC " + DIR_PROC)
        change_proc(lhs, mass, nevents, ptj, reset=True)

def main():
    is_higgs = input("on-shell higgs? (y,n): ")
    is_higgs = True if (is_higgs=='y') else False
    lhs = float(input("LHS: "))
    qt_m = int(input("Number of DM masses: "))
    dm_masses = []
    for q in range(qt_m):
        m = float(input("mdm" + str(q+1) + ": "))
        dm_masses.append(m)

    n_ev = int(input("Number of events: "))
    cut = float(input("Cut for jets (ptj): "))
    run_madgraph(lhs, dm_masses, n_ev, cut, higgs=is_higgs)
    

if __name__ == '__main__':
    main()