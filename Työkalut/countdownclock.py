import time, os, sys

tim = 40
os.system("cowsay -f sodomized-sheep \x1b[41mCountdown started\x1b[0m > hissi.log")
while True:
	time.sleep(1)
	os.system("cowsay -f sodomized-sheep " + "\x1b[41m"+str(tim)+"\x1b[0m" + "> hissi.log")
	if tim == 0:
		os.system("cowsay -f sodomized-sheep \x1b[41mYOU LOSE! THE SYSTEM IS OURS!BWAHAHAHAHAA\x1b[0m > hissi.log")
		break
	else:
		tim -= 1
time.sleep(10)
os.system("sudo shutdown -h now")
