#!/bin/bash
eval $(docker-machine env dev)
exec bash --rcfile docker-machine-prompt.rc
