#!/bin/bash
# sends a POST request to the passed URL, and displays body
curl -X POST -sd "email=hr@holbertonschool.com&subject=I+will+always+be+here+for+PLD" "$1"
