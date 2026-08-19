#!/bin/bash
prefix=$2 
dir=$1
shift 2
input_numbers=("$@")
if [ -d "$dir" ]; then
	echo "Directory found."
else
	mkdir -p "$dir"
fi

my_random_number=$((RANDOM % 30)+ 1)
echo "your random number is $my_random_number."
for((j=1; j<=my_random_number;j++));do
	file="$dir/${prefix}${j}.txt"
	touch "$file"
	echo "$file is created"
done
for k in "${input_numbers[@]}";do
	file="$dir/${prefix}${k}.txt"
	rm "$file"
	echo "$file is removed."
done
