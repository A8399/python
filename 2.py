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
    gpu_info = pynvml.nvmlDeviceGetFullName(handle)
    gpu_name = gpu_info.decode().replace(" ", "-")
    gpu_names.append(gpu_name)

# 清理 NVIDIA 管理库
pynvml.nvmlShutdown()

# 获取硬盘剩余容量
disk_usage = psutil.disk_usage('/')
disk_free = disk_usage.free // (2**30)

# 构建输出字符串
cpu_model = cpu_name.split()[2].replace("-", "")
output_str = "{}_{}_{}".format(cpu_model, "_".join(gpu_names), disk_free)

# 打印输出字符串
print(output_str)
