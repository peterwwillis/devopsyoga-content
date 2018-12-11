#!/bin/bash
set -e
MYDIR=$(readlink -f $(dirname ${BASH_SOURCE[0]}))
MDBN=`basename $MYDIR`
source $MYDIR/$MDBN.venv/bin/activate
BN=`basename $0 .sh`
./$BN.py $*
