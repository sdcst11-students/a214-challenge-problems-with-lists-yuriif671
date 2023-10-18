#!python3

"""
The list represents the list price of an item.
Use a for loop to iterate through the list to:
Calculate 5% GST rounded to 2 decimal places
Calculate 7% PST rounded to 2 decimal places
add the price to a subtotal
add the GST to a GST total
add the PST to a PST total
Find the total price for the entire list

Uncomment lines 16,17 and 18 for different test data
"""

#prices = [92.18, 72.74, 89.57, 44.89, 97.12, 91.97]         # subtotal:488.47 gst:24.43 pst:34.19 total:547.09
#prices = [19.36, 73.35, 58.72, 15.63, 28.54, 61.94, 27.58, 69.55, 16.67] #subtotal:371.34 gst:18.58 pst:26.0 total:415.92
#prices = [38.0, 83.18, 66.35, 82.27, 59.13, 17.17, 51.13, 10.97, 25.18, 89.79, 85.41] # subtotal:608.58 gst:30.44 pst:42.6 total:681.62
total = 0
gst = 0
pst = 0

    