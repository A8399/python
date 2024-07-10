import psutil

def check_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

process_name = "aleo-miner"

if check_process_running(process_name):
    print(f"进程 {process_name} 正在运行.")
else:
    print(f"进程 {process_name} 未在运行.")