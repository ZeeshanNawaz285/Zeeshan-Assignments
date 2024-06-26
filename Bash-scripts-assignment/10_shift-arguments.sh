#!/bin/bash 


#to create a user , provide username and description 

echo "Creating user"

echo "username is $1"

#shift is liyah use kia ha jb 1 argument k bd baki jo rakh jay ga wo sb 2nd argument ma jay ga 
shift 
echo "description is  $@"

