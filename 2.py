import cpuinfo
import pynvml
import psutil

# 获取 CPU 信息
cpu_info = cpuinfo.get_cpu_info()
cpu_name = cpu_info['brand_raw']

# 初始化 NVIDIA 管理库
pynvml.nvmlInit()

# 获取 GPU 数量和名称
gpu_count = pynvml.nvmlDeviceGetCount()
gpu_names = []

for i in range(gpu_count):
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    name = pynvml.nvmlDeviceGetName(handle)
    gpu_names.append(name)

# 清理 NVIDIA 管理库
pynvml.nvmlShutdown()

# 获取硬盘剩余容量
disk_usage = psutil.disk_usage('/')
disk_free = disk_usage.free // (2**30)

# 打印 CPU 名称
print("CPU 名称:", cpu_name)

# 打印 GPU 数量和名称
print("GPU 数量:", gpu_count)
for i, gpu_name in enumerate(gpu_names):
    print("GPU", i, "名称:", gpu_name)

# 打印硬盘剩余容量
print("硬盘剩余容量:", disk_free, "GB")
