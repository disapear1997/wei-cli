from pathlib import Path
import re


class VersionManager:
    def __init__(self, pyproject_path: Path = Path("pyproject.toml")):
        self.pyproject_path = pyproject_path

    def patch(self) -> str:
        text = self.pyproject_path.read_text(encoding="utf-8")

        match = re.search(r'^version\s*=\s*"(\d+)\.(\d+)\.(\d+)"',
                          text,
                          re.MULTILINE)

        if match is None:
            raise RuntimeError("Version not found in pyproject.toml")

        major, minor, patch = map(int, match.groups())

        old_version = f"{major}.{minor}.{patch}"
        new_version = f"{major}.{minor}.{patch + 1}"

        text = text.replace(
            f'version = "{old_version}"',
            f'version = "{new_version}"',
            1,
        )

        self.pyproject_path.write_text(text, encoding="utf-8")

        print(f"{old_version} -> {new_version}")

        return new_version