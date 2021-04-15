# Source common kernel config
from device.xiaomi.sm8250 import *

# Device info
CODENAME = "citrus"
DEFCONFIG = f"vendor/{CODENAME}_defconfig"

# Kernel sources folder name
KERNEL_PATH = "kernel/xiaomi/citrus"

# I don't build DTBO as of now
BUILD_ARTIFACTS = ["Image", "dtb.img"]
