#!/usr/bin/env bash
# Reset demo state to a known baseline.

set -e

echo "Removing local SQLite databases and caches..."

rm -rf data/*.db data/*.sqlite

# Optional: clear Python caches
find . -type d -name __pycache__ -prune -exec rm -rf {} + || true

echo "Demo state reset complete. Restart the app or containers."
