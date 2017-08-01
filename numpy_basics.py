#When you importing a python package you can import the whole thing or parts of it
#import packageName will import the whole package and you will have to use its package_Name
#you could also import packaName as pN to shorten the name of how you are going to call it
#you can also import just parts of the package, called sub-packages like so
#import packageName.subPackage

# Import numpy
import numpy as np

# Lists of data
city = ["Tokyo, Japan", "Delhi, India", "Shanghai, China", "Mexico City, Mexico", "Sao Paulo, Brazil"]
population = [38, 25, 23, 21, 21]


# Lists converted to numpy arrays
np_city = np.array(city)
np_population = np.array(population)


# Print out the median population of top 5 biggest cities
print("Median population of world's most populated cities is: " + str(np.median(np_population)))
