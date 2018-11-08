#Write a function invert_dict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.



nvert_dict = {'x':1,'y':2,'z':3,'w':4,'t':5}
def invert(d):
    return dict([(v,k) for k, v  in d.items()])

print(invert_dict)
print(invert(invert_dict))
