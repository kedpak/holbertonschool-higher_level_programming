#!/bin/bash
# request url and return size of body in bytes
curl -sI "$@" | grep "Content-Length" | cut -d " " -f 2
