"""SSH Config List — List Host entries from ~/.ssh/config with HostName and User, hiding IdentityFile contents."""
from __future__ import annotations

import argparse


def main() -> int:
    parser = argparse.ArgumentParser(
        prog='ssh_config_list',
        description='List Host entries from ~/.ssh/config with HostName and User, hiding IdentityFile contents.',
    )
    parser.add_argument('path', nargs='?', help='Input file or folder')
    parser.add_argument('--out', help='Output folder')
    parser.add_argument('--preview', help='Show the plan and do not write')
    args = parser.parse_args()
    print('SSH Config List')
    print('Which SSH aliases you actually have.')
    print('Local CLI preview.')
    if vars(args):
        print(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
