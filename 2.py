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

# 构建输出字符串
output_str = "{}_{}_{}".format(cpu_name.replace(" ", "-"), "_".join(gpu_names), disk_free)

# 打印输出字符串
print(output_str)

text = output_str

# 提取 CPU 名称
cpu_name = text.split("_")[0].split("-")[3]

# 提取 GPU 名称和硬盘剩余容量
gpu_disk_info = text.split("_")[1:]
gpu_name = gpu_disk_info[0]
disk_free = gpu_disk_info[1]

gpu = gpu_name.split(" ")[-1]
# 构建输出字符串
output_str = "{}_{}_{}".format(cpu_name, gpu, disk_free)

# 打印输出字符串
print(output_str)
