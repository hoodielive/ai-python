# the current volue of a water reservoir (in cubic meters) 
reservior_volume = 4.445e8 

# the amount of rainfall form a storm (in cubic meters)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff 
rainfall *= .9 

# add the rainfall variable to the reservior_volume variable 
reservior_volume += rainfall

# increase reservior_volume by 5% to account for stormwater that flows 
# into the reservoir in the days following the storm 
reservior_volume *= 1.05

# decrease reservior_volume by 5% to account for evaporation 
reservior_volume *=0.95

# subtract 2.5e5 cubic meters from reservior_volume to account for water thats piped to agrid regions 
reservior_volume -= 2.5e5

# print the new value of the reservior_volume variable 
print(reservior_volume)
