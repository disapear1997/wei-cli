import subprocess


def check_command(name: str, command: list[str]) -> bool:
    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        print(f"[✓] {name}: {result.stdout.strip()}")
        return True

    except FileNotFoundError:
        print(f"[✗] {name} is not installed.")
        return False

    except subprocess.CalledProcessError:
        print(f"[✗] {name} is installed but cannot be executed.")
        return False

def doctor(args):
    check_command("Git",["git","--version"])
    check_command("Docker",["docker","--version"])
    check_command("Docker Compose", ["docker", "compose", "version"])
    check_command("GitHub CLI", ["gh", "--version"])
    