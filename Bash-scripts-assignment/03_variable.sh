#!/bin/bash

#script to show how to use variables

a=10
name="zeeshan"
age=15

echo "my name is $name and age is $age"


name="nawaz"

echo "my second name is $name "

#variable to store the output of a command 
hostname=$(hostname)

echo "name of this machine is $hostname"

