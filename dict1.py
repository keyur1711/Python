d ={"one":2,"two":3}


d["no"] = 56

print(d)



print(dir(d))

print(d.get("one"))
print(d.items())
print(d.keys())
print(d.values())
d.pop("one")
print(d)
print(d.popitem())
print(d)