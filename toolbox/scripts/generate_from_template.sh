#!/bin/bash

cp ~/Code/competitive-programming/toolbox/templates/python_solution.py ./$1_sol.py
touch ./$1_test.txt

sed -i '' -e "s/{{test_file}}/$1_test/g" $1_sol.py