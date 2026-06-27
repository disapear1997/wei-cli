import argparse


def main():
    parser = argparse.ArgumentParser(
        prog="wei",
        description="Wei CLI"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="wei-cli 0.0.1"
    )

    parser.parse_args()