#!/usr/bin/bash
echo `ps -e | grep $1 | grep -Eo "[0-9]{4}"`