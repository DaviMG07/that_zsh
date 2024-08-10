from src import *
import os

HOME: str = os.path.expanduser("~")
WORKDIR: str = HOME + "/that_zsh"
ASSETS: str = WORKDIR + "/assets"

with open(WORKDIR + "/dependencies.txt", "r") as file:
    DEPENDENCIES: list[str] = file.read().split("\n")

def clear() -> None:
    os.system("clear")
    return

def run() -> None:
    for index, pkg in enumerate(DEPENDENCIES):
        print(f"[{index}/{len(DEPENDENCIES)}] - {pkg}")
        if (ubuntu.installed(pkg)): continue
        ubuntu.install(pkg)
        continue

    if (omz.installed()):
        os.system(f"remove -r {HOME + "/.oh-my-zsh"}")
        pass

    if (p10k.installed()):
        os.system(f"remove -r {HOME + "/powerlevel10k"}")
    return

if __name__ == "__main__":
    run()