#!/usr/bin/bash
ps -e | grep "$1" | grep -oE "([0-9]+)?" | head -n 1