import psutil

def check_process_running(process_name):
    for process in psutil.process_iter(['name']):
        if process.info['name'] == process_name:
            return True
    return False

process_name = "aleo-miner"

if check_process_running(process_name):
    print("runing")
else:
    print("no")