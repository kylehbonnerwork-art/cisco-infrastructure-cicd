#!/usr/bin/env python3

"""
Basic validation for Cisco IOS XE configuration files.

This script performs preliminary checks on configuration inputs.
It does not connect to or configure a network device.
"""

import sys
from pathlib import Path


CONFIG_FILE = Path("configs/router_config.txt")

REQUIRED_COMMANDS = [
    "hostname",
]

FORBIDDEN_PATTERNS = [
    "write erase",
    "erase startup-config",
    "reload",
]


def validate_config(config_file: Path) -> bool:
    """Validate basic configuration requirements."""

    if not config_file.is_file():
        print(f"ERROR: Configuration file not found: {config_file}")
        return False

    config = config_file.read_text(encoding="utf-8")
    normalized_config = config.lower()

    errors = []

    if not config.strip():
        errors.append("Configuration file is empty.")

    for command in REQUIRED_COMMANDS:
        if not any(
            line.strip().lower().startswith(command + " ")
            or line.strip().lower() == command
            for line in config.splitlines()
        ):
            errors.append(
                f"Required configuration command is missing: {command}"
            )

    for pattern in FORBIDDEN_PATTERNS:
        if pattern in normalized_config:
            errors.append(
                f"Potentially destructive command detected: {pattern}"
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
