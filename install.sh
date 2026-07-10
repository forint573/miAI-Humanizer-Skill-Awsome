#!/usr/bin/env bash
#
# install.sh — install the HumanCopywrite skill into a Claude skills folder.
#
# Fastest path:
#   curl -fsSL https://raw.githubusercontent.com/forint573/human-copywrite/main/install.sh | bash
#
# Options (env vars):
#   SCOPE=user      install to ~/.claude/skills           (default)
#   SCOPE=project   install to ./.claude/skills           (current repo)
#   DEST=/path      install into a specific skills folder  (overrides SCOPE)
#   REF=main        git ref to install from                (default: main)
#
# Or run it from a clone:
#   ./install.sh            # user scope
#   SCOPE=project ./install.sh

set -euo pipefail

REPO_URL="https://github.com/forint573/human-copywrite.git"
SKILL_NAME="human-copywrite"
REF="${REF:-main}"
SCOPE="${SCOPE:-user}"

if [[ -n "${DEST:-}" ]]; then
  TARGET="${DEST}"
elif [[ "${SCOPE}" == "project" ]]; then
  TARGET="$(pwd)/.claude/skills"
else
  TARGET="${HOME}/.claude/skills"
fi

echo "HumanCopywrite installer"
echo "  source : ${REPO_URL} (ref: ${REF})"
echo "  target : ${TARGET}/${SKILL_NAME}"
echo

command -v git >/dev/null 2>&1 || { echo "error: git is required." >&2; exit 1; }

# If we're already inside a clone, copy locally; otherwise fetch a shallow copy.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if [[ -d "${SCRIPT_DIR}/${SKILL_NAME}" ]]; then
  SRC="${SCRIPT_DIR}/${SKILL_NAME}"
  CLEANUP=""
else
  TMP="$(mktemp -d)"
  CLEANUP="${TMP}"
  git clone --depth 1 --branch "${REF}" "${REPO_URL}" "${TMP}/repo" >/dev/null 2>&1 \
    || git clone --depth 1 "${REPO_URL}" "${TMP}/repo" >/dev/null 2>&1
  SRC="${TMP}/repo/${SKILL_NAME}"
fi

if [[ ! -f "${SRC}/SKILL.md" ]]; then
  echo "error: could not locate ${SKILL_NAME}/SKILL.md in the source." >&2
  [[ -n "${CLEANUP}" ]] && rm -rf "${CLEANUP}"
  exit 1
fi

mkdir -p "${TARGET}"
rm -rf "${TARGET:?}/${SKILL_NAME}"
cp -r "${SRC}" "${TARGET}/${SKILL_NAME}"
[[ -n "${CLEANUP}" ]] && rm -rf "${CLEANUP}"

echo "Installed to ${TARGET}/${SKILL_NAME}"
echo
echo "Next: open Claude in this context and ask it to"
echo "  \"humanize this copy\"  or  \"finalize this draft and remove planning notes\"."
