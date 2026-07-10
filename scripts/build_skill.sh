#!/usr/bin/env bash
#
# build_skill.sh — package the skill into a distributable .skill archive.
#
# A .skill file is a zip archive with the skill folder at its root. This script
# produces dist/human-copywrite.skill from the source folder, excluding
# build cruft so the package stays clean.

set -euo pipefail

SKILL_DIR="human-copywrite"
DIST_DIR="dist"
OUTPUT="${DIST_DIR}/${SKILL_DIR}.skill"

# Run from the repository root regardless of where the script is invoked.
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "${ROOT}"

if [[ ! -f "${SKILL_DIR}/SKILL.md" ]]; then
  echo "error: ${SKILL_DIR}/SKILL.md not found. Run from the repository root." >&2
  exit 1
fi

mkdir -p "${DIST_DIR}"
rm -f "${OUTPUT}"

zip -r -X "${OUTPUT}" "${SKILL_DIR}" \
  -x '*.DS_Store' \
  -x '*__pycache__*' \
  -x '*.py[cod]'

echo
echo "Built ${OUTPUT}"
unzip -l "${OUTPUT}"
