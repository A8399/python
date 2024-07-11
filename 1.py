import time
import subprocess
import psutil

# 检查进程是否在运行
def check_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

# 关闭进程
def stop_process(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            process.kill()

# 启动进程
def start_process(command):
    subprocess.Popen(command, shell=True).wait()

# 配置参数
with open("/root/info.txt", "r") as file:
    info_text = file.read()
output = info_text
f2pool_name = "rukool88" + "."
miner_id = f2pool_name + output
process_name = "aleo-miner"
aleo_miner_path = "/root/aleo/aleo.sh"
miner_code = "stratum+tcp://aleo-asia.f2pool.com:4400 " + miner_id

while True:
    if not check_process_running(process_name):
        print(f"{process_name} 进程未运行，启动进程...")
        start_process(f"cd /root/aleo && nohup {aleo_miner_path} {miner_code} > aleo-miner.log 2>&1 &")
        print(f"{process_name} 进程已启动")
    else:
        print(f"{process_name} 进程正在运行")

    # 等待5秒后进行下一次检测
    time.sleep(5)
