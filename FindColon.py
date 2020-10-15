str = 'X-Dspam-Confidence: 0.8475'
#Find colon
cpos=str.find(':')
print(cpos)
#Find value
piece=str[cpos+2:]
print(piece)
#Convert to float from str
value=float(piece)
print(value)
