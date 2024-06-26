#!/bin/bash 

#Array concept 

myarray=(1 20 30.5 salam "pakistan")


echo "all vales in array is ${myarray[*]}"

echo "value is 3rd index  ${myarray[3]}"
 
 
 #how to find no. of values in an array 
 
 echo "no. of values , length of an array is ${#myarray[*]} "
 
#how to get specific values 

echo "${myarray[*]:2:2}"

#how to update array 
myarray+=(new 30 40)
echo "values of new array are ${myarray[*]}"
<<comment
#how to store the key values pairs 

declare -A myarray 
myarray=([name]=zee [age]=20)
echo "name is ${myarray[name]}"
comment
