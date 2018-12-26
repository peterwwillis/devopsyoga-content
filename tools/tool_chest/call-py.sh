#!/bin/bash
set -e
MYFILE=$(readlink -f ${BASH_SOURCE[0]})
MYDIR=$(dirname ${MYFILE})
MDBN=`basename $MYDIR`
ACT="$MYDIR/$MDBN.venv/bin/activate"
if [ ! -r "$ACT" ] ; then
    echo "Error: could not load '$ACT'" ; exit 1
fi
source $ACT
BN=`basename $0 .sh`
./$BN.py $*
