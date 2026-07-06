letter = ''' Dear <|Name|>,
You are selected !
<|Date|>'''

print(letter.replace("<|Name|>", "vinay") .replace("<|Date|>","10 june 2005"))



name = "virat kohli is my      idol"
# strings are immutable
print(name.find("idol"))