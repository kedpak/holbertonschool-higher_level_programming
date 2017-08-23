#!/bin/bash
# send DELETE request to URL passed
curl -sL "$1" -X DELETE "$1"
