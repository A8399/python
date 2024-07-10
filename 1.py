import cpuinfo
import pynvml
import psutil

# Get CPU information
cpu_info = cpuinfo.get_cpu_info()
cpu_name = "_".join(cpu_info['brand_raw'].replace(" ", "_").split("_")[2:4])

# Initialize NVIDIA management library
pynvml.nvmlInit()

# Get GPU count and names
gpu_count = pynvml.nvmlDeviceGetCount()
gpu_names = []

for i in range(gpu_count):
    handle = pynvml.nvmlDeviceGetHandleByIndex(i)
    name = pynvml.nvmlDeviceGetName(handle)
    gpu_name = "_".join(name.replace(" ", "_").split("_")[-2:])
    gpu_names.append(gpu_name)

# Clean up NVIDIA management library
pynvml.nvmlShutdown()

# Get available disk space
disk_usage = psutil.disk_usage('/')
disk_free = disk_usage.free // (2 ** 30)

# Combine CPU, GPU, and disk information
output = "_".join([*gpu_names, str(disk_free)])

# Save the output to a file
with open("info.txt", "w") as file:
    file.write(output)

# Print the output
print(output)
