import subprocess

def docker_enter(args):
    """Enter the project's development container."""

    # Start containers
    subprocess.run(
        ["docker", "compose", "up", "-d"],
        check=True,
    )

    # Enter dev service
    subprocess.run(
        ["docker", "compose", "exec", "dev", "bash"],
        check=True,
    )