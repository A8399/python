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
    subprocess.Popen(command, shell=True)

# 配置参数
with open("/root/info.txt", "r") as file:
    info_text = file.read()
output = info_text
f2pool_name = "rukool88" + "."
miner_id = f2pool_name + output
process_name = "aleo-miner"
aleo_miner_path = "/root/aleo/aleo.sh"
miner_code = "stratum+tcp://aleo-asia.f2pool.com:4400 " + miner_id

# 设定定时关闭和重新打开的时间间隔（单位：秒）
interval = 3600  # 一小时
restart_delay = 30  # 重新启动延迟时间（单位：秒）
startup_delay = 10  # 启动延迟时间（单位：秒）

while True:
    if check_process_running(process_name):
        print(f"{process_name} 正在运行，关闭进程...")
        stop_process(process_name)
        time.sleep(10)  # 等待一段时间确保进程关闭完全
        print(f"{process_name} 进程已关闭")
    else:
        print(f"{process_name} 进程未运行")

        # 等待启动延迟时间
        print(f"等待 {startup_delay} 秒后启动 {process_name} 进程...")
        time.sleep(startup_delay)

        # 启动进程
        print(f"启动 {process_name} 进程...")
        start_process(f"cd /root/aleo && nohup {aleo_miner_path} {miner_code} > aleo-miner.log 2>&1 &")
        print(f"{process_name} 进程已启动")

    # 等待指定的时间间隔
    print(f"等待 {interval} 秒...")
    time.sleep(interval)
