import time
import subprocess
import getpass
import subprocess

subprocess.run(["python", "1.py"])
username = getpass.getuser()
print(username)

def check_process_running(process_name):
    try:
        subprocess.check_output(f"pgrep {process_name}" , shell=True)
        return True
    except subprocess.CalledProcessError:
        return False


process_name = "aleo-miner"
with open("/root/info.txt", "r") as file:
    info_text = file.read()
output = info_text
aleo_miner_path = "/root/aleo/aleo.sh"
f2pool_name = "rukool88"+"."
miner_id = f2pool_name+output
miner_code = "stratum+tcp://aleo-asia.f2pool.com:4400 "+miner_id

while True:
    if check_process_running(process_name):
        print(f" {process_name} runing")
        subprocess.Popen(f"cd /root/aleo/ ; tail -f aleo-miner.log" , shell=True)
    else:
        print(f"The process {process_name} is not running. Starting...")
        subprocess.Popen(f"cd /root/aleo && {aleo_miner_path} {miner_code} && tail -f aleo-miner.log" , shell=True)


    time.sleep(120)


