# Decision making with conditionals
"""
Variations of conditionals:
1. if
2. if - elif(s)
3. if - elif(s) - else
4. if - else
"""

score = 4

# 1 if_entity gives only 1 input
# Executes the first condition that is elevated to True
# and disregard the rest
"""
if score > 20:
    print("#_#")
    
elif score > 50:
    print("*_*")
    
elif score > 8:
    print("^_^")
    
elif score > 2:
    print("&_&")
    
if score > 1:
    print("$_$")
    
elif score > 0:
    print("@_@")
"""

if score > 12:
    print("^_^")
elif score > 15:
    print("*_*")
elif score > 5:
    print("%_%")
else:
    print("#_#")
