import os
import subprocess

result: str = subprocess.run(['dpkg', '--get-selections'], stdout=subprocess.PIPE, text=True).stdout.replace("\tinstall\n", "")

for _ in range(4):
    result = result.replace("\t\t", "\t")

INSTALLED: list[str] = result.split("\t")

def install(package: str) -> None:
    os.system(f"sudo apt install {package} -y")
    return

def upgrade() -> None:
    os.system("sudo apt update && sudo apt upgrade -y")
    return

def installed(package: str) -> bool:
    return (package in INSTALLED)