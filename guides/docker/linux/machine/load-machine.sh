#!/usr/bin/env bash
# load-machine.sh - load a docker machine and change PS1 prompt to include machine name
# Copyright (C) 2018 Peter Willis <peterwwillis@gmail.com>
# 
# Usage:
#       $ ./load-machine.sh
#   OR 
#       $ ./load-machine.sh machine-name
# 

[ $# -gt 0 ] && DM_NAME="$1"

# The following will evaluate a PROMPT_COMMAND (if it was set),
# then it will replace any '\h' entry in the PS1 variable with
# the DOCKER_MACHINE_NAME environment variable.
function __dockermachine_name () {
    [ -n "$1" ] && eval "$1"
    PS1=${PS1/\\h/(docker-$DOCKER_MACHINE_NAME)}
}

function __load_prompt() {
    # Load the user's bashrc file
    [ -r "$HOME/.bashrc" ] && . $HOME/.bashrc
    if [ -n "$PROMPT_COMMAND" ] ; then
        OLD_PROMPT_COMMAND=$PROMPT_COMMAND
        PROMPT_COMMAND="__dockermachine_name '$OLD_PROMPT_COMMAND'"
    else
        __dockermachine_name
    fi
}

if [ -n ${#BASH_LINENO[0]} -a ${BASH_LINENO[0]} -le 0 -a -n "$HISTFILE" ] ; then
    __load_prompt
else

    [ -n "$DM_NAME" ] || DM_NAME="dev"
    if ! docker-machine ls | tail -n +2 | grep -q "^$DM_NAME" ; then
        echo "Error: $0: Docker-machine named '$DM_NAME' does not exist."
    else
        STATUS=$(docker-machine status $DM_NAME)
        [ "$STATUS" = "Stopped" ] && docker-machine start $DM_NAME
        eval $(docker-machine env $DM_NAME)
        _INCLUDING_AS_RC=1
        exec bash --rcfile ${BASH_SOURCE[0]}
    fi
fi
