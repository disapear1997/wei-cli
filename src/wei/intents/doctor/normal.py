import subprocess

def doctor(args):
    try:
        result = subprocess.run(
            ["git", "--version"],
            capture_output=True,
            text=True,
            check=True,
        )

        print(f"[✓] {result.stdout.strip()}")

    except FileNotFoundError:
        print("[✗] Git is not installed.")

    except subprocess.CalledProcessError:
        print("[✗] Git is installed but cannot be executed.")