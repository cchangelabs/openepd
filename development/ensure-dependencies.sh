#!/bin/bash

DEPS=("python3.11" "sed")

echo "Verifying required dependencies"
echo ""

for d in "${DEPS[@]}"; do
  if [ -n "$(which "$d")" ]; then
    printf "   %-25s: installed\n" $d
  else
    printf "   %-25s: %b\n" $d "${COLOR_RED}NOT INSTALLED${COLOR_NC}"
    exit 1
  fi
done

echo ""
echo "All dependencies installed"
