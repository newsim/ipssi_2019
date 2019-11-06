#!/bin/bash


# if running bash
    # include .bashrc if it exists
    touch efface_moi
    if [ -f "/Users/simon/Desktop/rendu/ex04/efface_moi" ]; then
	    echo "il existe";
    else 
        echo "il n'existe pas"
    fi

# set PATH so it includes user's private bin directories
PATH="$HOME/bin:$HOME/.local/bin:$PATH"