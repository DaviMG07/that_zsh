from . import omz, ubuntu, p10k
import os

def take_config(home: str, assets: str) -> None:
    os.rename(home + "/.zshrc", home + "/.zshrc.old")
    os.symlink(assets: "/zshrc", home + "/.zshrc")
    return