import subprocess

def dev_install(args):
    subprocess.run(["uv", "pip", "install", "-e", "."], check=True)