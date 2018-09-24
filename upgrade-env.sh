#!/bin/bash

helm upgrade $1 jupyterhub/jupyterhub \
  --version 0.7.0 \
  -f deployments/config-$1.yaml

