#!/bin/bash

export title='GC PaaS Demo'

docker run -d --name api-1 --rm -p 5001:5000 \
       --env API_ID="1" \
       --env API_CLOUD="azure" \
       --env API_TITLE="${title}" \
       paas-gc-api \
       api/paas_gc_api_demo.py

docker run -d --name api-2 --rm -p 5002:5000 \
       --env API_ID="2" \
       --env API_CLOUD="azure" \
       --env API_TITLE="${title}" \
       paas-gc-api \
       api/paas_gc_api_demo.py

docker run -d --name api-3 --rm -p 5003:5000 \
       --env API_ID="3" \
       --env API_CLOUD="google" \
       --env API_TITLE="${title}" \
       paas-gc-api \
       api/paas_gc_api_demo.py

docker run -d --name api-4 --rm -p 5004:5000 \
       --env API_ID="4" \
       --env API_CLOUD="google" \
       --env API_TITLE="${title}" \
       paas-gc-api \
       api/paas_gc_api_demo.py