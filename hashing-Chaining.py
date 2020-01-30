class HashTable(object):
    
    def __init__(self, taille):
        self.table = [None]*taille;
    
    # transform the data to numbers countable (in N) non negative.
    def preshash(self, index):
        return index % 3;

    # collision resolved by chaining methode
    def add(self, value):
        key = self.preshash(value);
        if self.table[key] != None:
            if type(self.table[key]) == list:
                value = [value] + self.table[key]
            else:
                value = [value] + [self.table[key]]

        self.table[key] = value;

Universe = [9,8,7,6,5,4,3,2,1,0]
hashtable =  HashTable(len(Universe))
for x in Universe:
    hashtable.add(x);
print(hashtable.table)
