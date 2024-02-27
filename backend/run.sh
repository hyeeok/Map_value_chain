#!/bin/bash

redis-server --bind 0.0.0.0 --port 6379 &

sleep 10

uvicorn main:app --host 0.0.0.0 --port 8000
