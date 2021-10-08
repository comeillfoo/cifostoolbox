#!/usr/bin/bash
ps -e | grep "3c627d" | grep -oE "([0-9]+)?" | head -n 1