#!/bin/bash
# display all HTTP methods the server will accept
curl -sI OPTIONS "$1" | grep "Allow:" | cut -b8-
