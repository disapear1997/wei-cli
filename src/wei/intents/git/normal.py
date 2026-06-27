import subprocess

def git_sync(args):
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", args.message], check=True)
    subprocess.run(["git", "push"], check=True)