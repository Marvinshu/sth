#!/bin/bash

while true
do
    python app.py

    echo 'restarting ...'
    COUNTER=5  
    while [  $COUNTER -gt 0 ]
    do  
        echo  $COUNTER  
        let COUNTER=COUNTER-1   
        sleep 1s
    done  
done
