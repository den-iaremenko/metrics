#!/bin/bash

echo "####Create Container####"
docker build -t metrics .

echo "####Start Python Container####"
###docker run --rm --name metrics --detach -d metrics


