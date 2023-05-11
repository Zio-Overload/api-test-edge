#!/bin/bash

cd "$(dirname "$0")"
source fastapi-iotedge-test/bin/activate
uvicorn main:app --host=0.0.0.0 --workers=3
