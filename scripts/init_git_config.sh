#!/usr/bin/env bash
set -euo pipefail

USER_EMAIL="khb9gd@virginia.edu"
USER_NAME="CodeStriker10"

git config --global user.email "$USER_EMAIL"
git config --global user.name "$USER_NAME"
git config --global init.defaultBranch "main"
git config --global core.editor "nano"

git config --global --list
