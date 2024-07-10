import time
import subprocess
import getpass
import subprocess

subprocess.run(["python", "1.py"])
username = getpass.getuser()
print(username)

def check_process_running(process_name):
    # 使用 pgrep 命令检查进程是否正在运行
    try:
        subprocess.check_output(f"pgrep {process_name}" , shell=True)
        return True
    except subprocess.CalledProcessError:
        return False


# 要检查的进程名称
process_name = "aleo-miner"
with open("info.txt", "r") as file:
    info_text = file.read()
# aleo-miner程序路径
output = info_text
aleo_miner_path = "/root/aleo/aleo.sh"
f2pool_name = "rukool88"+"."
miner_id = f2pool_name+output
# 指定的代码
miner_code = "stratum+tcp://aleo-asia.f2pool.com:4400 "+miner_id

while True:
    if check_process_running(process_name):
        print(f"进程 {process_name} 正在运行.")
        subprocess.Popen(f"cd /root/aleo/ ; tail -f aleo-miner.log" , shell=True)
    else:
        print(f"进程 {process_name} 未在运行. 启动中...")
        # 切换到aleo-miner程序所在的文件夹并启动aleo-miner
        subprocess.Popen(f"cd /root/aleo && {aleo_miner_path} {miner_code} && tail -f aleo-miner.log" , shell=True)

    # 暂停10分钟
    time.sleep(120)


