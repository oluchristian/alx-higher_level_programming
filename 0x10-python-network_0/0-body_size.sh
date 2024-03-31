#!/bin/bash
# a bash script that prints body size of a http header response
curl -sI $1 | grep -i 'Content-Length' | cut -d " " -f2