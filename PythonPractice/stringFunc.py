
#str = "Arpan is a good boy"

#a = str.capitalize()  # The capitalize() method returns a string where the first character is upper case.
#print(str)
#print(a)

"""
str1 ="ARPAN IS A GOOD BOY"
b = str1.casefold()             #The casefold() method returns a string where all the characters are lower case.
print(b)
"""

"""
str1 ="ARPAN"
b = str1.center(20)             #The center() method will center align the string, using a specified character (space is default) as the fill character.
print(b)

C = str1.center(20,"0")
print(C)

"""
"""
str2 ="Ram is good boy, Ram play footbal daily, Ram also a very good student."
D = str2.count("Ram")  	#The count() method returns the number of times a specified value appears in the string.
print(D)

E = str2.count("Ram",0,20)  	#The count() method returns the number of times a specified value appears in the string.
print(E)
"""
"""
str3 ="Name of the boy is ÃÖRPA℉THU℃IKH"    #The encode() method encodes the string, using the specified encoding. If no encoding is specified, UTF-8 will be used.

print(str3.encode(encoding="ascii",errors="backslashreplace"))   #'backslashreplace'	- uses a backslash instead of the character that could not be encoded
print(str3.encode(encoding="ascii",errors="ignore"))             #'ignore'	- ignores the characters that cannot be encoded
print(str3.encode(encoding="ascii",errors="namereplace"))        #'namereplace'	- replaces the character with a text explaining the character
print(str3.encode(encoding="ascii",errors="replace"))            #'replace'	- replaces the character with a questionmark
print(str3.encode(encoding="ascii",errors="xmlcharrefreplace"))  #'xmlcharrefreplace'	- replaces the character with an xml character
"""

Str4 ="Hi, How are you"     #The endswith() method returns True if the string ends with the specified value, otherwise False.
F= Str4.endswith("you")
F1= Str4.endswith("are")
F2= Str4.endswith("you",4,13)
F3= Str4.endswith("you",4,15)
print(F)
print(F1)
print(F2)
print(F3)











