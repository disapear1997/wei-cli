import argparse
from importlib.metadata import version

from wei.intents.dev.register import register_dev
from wei.intents.git.register import register_git
from wei.intents.docker.register import register_docker




def main():

    parser = argparse.ArgumentParser(
        prog="wei",
        description="Wei CLI"
    )

    parser.add_argument(
        "--version",
        action="version",
        version=f"wei-cli {version('wei-cli')}"
    )

    # Root command
    subparsers = parser.add_subparsers(
        dest="command"
    )

    # Register first-level intents
    register_dev(subparsers)
    register_git(subparsers)
    register_docker(subparsers)

    args = parser.parse_args()

    # ------------------------------------------------------------------
    # Dispatch (暫時保留)
    # ------------------------------------------------------------------

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()