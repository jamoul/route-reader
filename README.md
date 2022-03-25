# About this project

This is a personal project to help me crunch air traffic data. To use the script with the provided "21pax.csv" dataset:
* Run the script.
* Input the IATA airport code of the desired origin airport (must be a US airport). 
* Call 'set_up(21)' to set up the reader with the 2021 data in 21pax.csv.
This will provide the passenger air traffic (seats and passengers flown) between the origin airport and all domestic destination airports in a dictionary 'segments', indexed by month, destination, and airline. Calling the 'collate()' function will remove the differentiation between airlines (so traffic between two given airports in a given month constitutes one entry in the dictionary).

Recommended: After setting up, try using the mon_total() function to display the seats and passengers flown to each destination in a given month. (As an argument, the function takes the month as an integer, so 1 = Jan, 2 = Feb, etc.)

I'm currently planning to overhaul this project to make it easier and more intuitive to work with!
