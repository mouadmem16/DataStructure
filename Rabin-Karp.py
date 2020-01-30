"""
    ROLLING HASH ADT.  
"""

# complexity: len(string) * len(key)
def Traditional(string, key):
    result = any(
                key == string[i:i+len(key)]
                for i in range(len(string)-len(key))
            );
    return(result);


# complexity: linear time len(string)
def RabinKarp(string, key):
    hashX = hash(key)
    for i in range(len(string)-len(key)):
        x = hash(string[i:i+len(key)]);
        if(x == hashX):
            if key == string[i:i+len(key)]:
                return True
    else: return False


print(RabinKarp("azazazazaza", "aa"));
print(Traditional("azazazazaza", "aa"));

print(RabinKarp("azazazazaza", "az"));
print(Traditional("azazazazaza", "az"));