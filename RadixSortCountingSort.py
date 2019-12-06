class SortIntegers:

    def __init__(self, t, b):
        self.tab = t;
        self.base = b;

    def Radix(self):
        def radix2simple(offs):
            if (self.tab[0]//offs == 0): return;
            self.Counting(offs);
            radix2simple(offs*10);
        radix2simple(1);

    def Counting(self, offset):
        baseTab = []
        result = [];
        for i in range(self.base):
            baseTab.append(list());
        for var in self.tab:
            baseTab[var//offset%10].append(var);
        for i in range(self.base):
            for var in baseTab[i]:
                result.append(var);
        self.tab = result;
        print(result)



integers = [7731,662,1570,3365,4564,3675,2232,1363,4130];
base = 8;

sort = SortIntegers(integers, base);
sort.Radix()
print(sort.tab);