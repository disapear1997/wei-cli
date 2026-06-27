# Wei CLI

Wei is a cross-platform command-line interface designed to simplify development workflows through intent-driven commands.

The core of **wei** is intentionally lightweight and depends only on the Python standard library. Platform-specific capabilities are provided by external tools or plugins.

> **Status:** Early development (v0.x)

---

# Installation

## Requirements

* Python 3.10 or later
* Recommended: Python 3.12
* pipx

---

## Ubuntu

Install `pipx` if it is not already available.

```bash
sudo apt update
sudo apt install pipx
pipx ensurepath
```

Install Wei from GitHub:

```bash
pipx install git+https://github.com/strongco223/wei-cli.git
```

Verify the installation:

```bash
wei --version
```

---

## Windows

Install Python (3.10 or later, 3.12 recommended).

Install pipx:

```powershell
python -m pip install --user pipx
python -m pipx ensurepath
```

Restart your terminal.

Install Wei:

```powershell
pipx install git+https://github.com/strongco223/wei-cli.git
```

Verify the installation:

```powershell
wei --version
```

---

# Upgrade

Update Wei to the latest version:

```bash
pipx upgrade wei-cli
```

If Wei was installed directly from the GitHub repository, reinstall it:

```bash
pipx reinstall git+https://github.com/strongco223/wei-cli.git
```

---

# Getting Help

Display the current version:

```bash
wei --version
```

More commands and documentation will be added in future releases.
