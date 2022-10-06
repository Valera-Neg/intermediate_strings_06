#Take the following Pythone code that stores a string: 
# str = "X-DSPAM-Confidence: 0.8475 "  
# Use <find> and string slicing to extract the portion of the 
# string after the colon character and then use the <float> function 
# to convert the extracted string into a floating point number.

str = "X-DSPAM-Confidence: 0.8475"
start = str.find(":")
res = str[start + 2 :]
fl = float(res)
print(fl)