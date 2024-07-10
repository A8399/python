import time
import subprocess
import cpuinfo
import pynvml
import psutil

# 获取 CPU 信息
cpu_info = cpuinfo.get_cpu_info()
cpu_name = "_".join(cpu_info['brand_raw'].replace(" ", "_").split("_")[2:4])

# 初始化 NVIDIA 管理库
pynvml.nvmlInit()

# 获取 GPU 数量和名称
gpu_count = pynvml.nvmlDeviceGetCount()
gpu_names = []


for i in range(gpu_count):
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    name = pynvml.nvmlDeviceGetName(handle)
    gpu_name = "_".join(name.replace(" ", "_").split("_")[-2:])
    gpu_names.append(gpu_name)

# 清理 NVIDIA 管理库
pynvml.nvmlShutdown()

# 获取硬盘剩余容量
disk_usage = psutil.disk_usage('/')
disk_free = disk_usage.free // (2 ** 30)

# 连接 CPU、GPU 和硬盘信息
output = "_".join([cpu_name, *gpu_names, str(disk_free)])
f2pool_name = "rukool88"+"."
miner_id = f2pool_name+output

def check_process_running(process_name):
    # 使用 pgrep 命令检查进程是否正在运行
    try:
        subprocess.check_output(f"pgrep {process_name}" , shell=True)
        return True
    except subprocess.CalledProcessError:
        return False


# 要检查的进程名称
process_name = "aleo-miner"
# aleo-miner程序路径
aleo_miner_path = "/root/aleo/aleo.sh"
# 指定的代码
pool_address = "stratum+tcp://aleo-asia.f2pool.com:4400"
connection_string = f"{pool_address} {miner_id}"
miner_code = connection_string

while True:
    if check_process_running(process_name):
        print(f"进程 {process_name} 正在运行.")
        subprocess.Popen(f"cd /root/aleo/ ; tail -f aleo-miner.log" , shell=True)
    else:
        print(f"进程 {process_name} 未在运行. 启动中...")
        # 切换到aleo-miner程序所在的文件夹并启动aleo-miner
        subprocess.Popen(f"cd /root/aleo && {aleo_miner_path} {miner_code} && tail -f aleo-miner.log", shell=True)

    # 暂停10分钟
    time.sleep(600)


