import time
import subprocess


def check_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False


# 要检查的进程名称
process_name = "aleo-miner"
# aleo-miner程序路径
aleo_miner_path = "/hive/aleo/aleo.sh"
# 指定的代码
miner_code = "stratum+tcp://aleo-asia.f2pool.com:4400 rukool88.293379"

while True:
    if check_process_running(process_name):
        print(f"进程 {process_name} 正在运行.")
    else:
        print(f"进程 {process_name} 未在运行. 启动中...")
        # 切换到aleo-miner程序所在的文件夹并启动aleo-miner
        subprocess.Popen(f"cd /hive/aleo && {aleo_miner_path} {miner_code}" , shell=True)

    # 暂停10分钟
    time.sleep(600)