txt = "We are the so-called \"Vikings\" from the north."
print(txt) # Use backslash '\' so we can have two double quotes inside one string

# Code	    Result
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value1

txt = "Choose YES \\ NO"
print(txt)

# A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157\n\n"
print(txt) 

print("Hello \nWorld! \n\tThis is Mandy") # Other escape characters example


