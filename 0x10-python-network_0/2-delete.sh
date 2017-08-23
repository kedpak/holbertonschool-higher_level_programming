#!/bin/bash
# send DELETE request to URL passed
curl -sLX "$1" -X DELETE -H "$1"
