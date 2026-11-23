set shell := ["bash", "-euo", "pipefail", "-c"]
set windows-shell := ["powershell.exe", "-NoLogo", "-Command"]

# List the recipes (default).
help:
    @just --list --unsorted

# Install the Python dependencies (uv sync).
setup:
    uv sync

# Convert the questions to all formats.
build:
    uv run scripts/build.py --format all

# Convert to Moodle XML only.
moodle:
    uv run scripts/build.py --format moodle

# Build the self-check page only.
selfcheck:
    uv run scripts/build.py --format selfcheck

# Check that the committed exports match the sources (what CI runs).
check:
    uv run scripts/build.py --check
