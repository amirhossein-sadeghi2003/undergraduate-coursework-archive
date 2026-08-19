#!/bin/bash

sudo rmmod speaker
sudo rm /dev/speakernode
make clean

echo "Your module(speaker) removed successfully."

