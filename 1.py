import time
import subprocess


def check_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False


process_name = "aleo-miner"
aleo_miner_path = "/hive/aleo/aleo.sh"
miner_code = "stratum+tcp://aleo-asia.f2pool.com:4400 rukool88.293379"

while True:
    if check_process_running(process_name):
        print("runing")
    else:
        print("runing")
        subprocess.Popen(f"cd /hive/aleo && {aleo_miner_path} {miner_code}" , shell=True)

    time.sleep(600)