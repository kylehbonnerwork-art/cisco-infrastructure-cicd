#!/usr/bin/env python3

"""
Basic validation for Cisco IOS XE configuration files.

This script performs preliminary static checks.
It does not connect to or configure a network device.
"""

import sys
from pathlib import Path


CONFIG_FILE = Path("configs/router_config.txt")

REQUIRED_COMMANDS = [
    "hostname",
]

FORBIDDEN_COMMANDS = {
    "write erase",
    "erase startup-config",
    "reload",
}


def validate_config(config_file: Path) -> bool:
    """Validate basic configuration requirements."""

    if not config_file.is_file():
        print(f"ERROR: Configuration file not found: {config_file}")
        return False

    try:
        config = config_file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"ERROR: Cannot read configuration file: {error}")
        return False

    errors = []

    if not config.strip():
        errors.append("Configuration file is empty.")

    commands = []

    for line in config.splitlines():
        line = line.strip()

        # Ignore blank lines and Cisco IOS XE comments.
        if not line or line.startswith("!"):
            continue

        commands.append(line.lower())

    for required in REQUIRED_COMMANDS:
        if not any(
            command == required
            or command.startswith(required + " ")
            for command in commands
        ):
            errors.append(
                f"Required configuration command is missing: {required}"
            )

    for command in commands:
        if command in FORBIDDEN_COMMANDS:
            errors.append(
                f"Potentially destructive command detected: {command}"
            )

    if errors:
        print("Configuration validation FAILED:")

        for error in errors:
            print(f"- {error}")

        return False

    print("Configuration validation PASSED.")
    print(f"Validated file: {config_file}")

    return True


if __name__ == "__main__":
    sys.exit(0 if validate_config(CONFIG_FILE) else 1)
