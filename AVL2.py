class Avl:
    def __init__(self, val, r = None, l = None, p = None):
        self.val = val;
        self.right = r;
        self.left = l;
        self.parent = p;
        self.height = 0;

    def add(self, node):
        if node.val < self.val:
            if self.left == None: self.left = node; self.left.parent = self;
            else: self.left.add(node);
        else:
            if self.right == None: self.right = node; self.right.parent = self;
            else: self.right.add(node);
        self.height = self.getHeight();
        selfBalance = self.getBalance(); leftBalance=0; rightBalance=0;
        if self.left != None: leftBalance = self.left.getBalance();
        if self.right != None: rightBalance = self.right.getBalance();

        if selfBalance == -2:
            if leftBalance == -1:
               return self.RightRotate();
            elif  leftBalance == 1:
                return self.LeftrightRotate();
        elif selfBalance == 2:
            if rightBalance == 1:
                return self.leftRotate();
            elif  leftBalance == -1:
                return self.RightleftRotate();
        else:
            return self;

    def LeftrightRotate(self):
        self.left = self.left.leftRotate();
        return self.RightRotate();

    def RightleftRotate(self):
        self.right = self.right.RightRotate();
        return self.leftRotate();

    def RightRotate(self):
        self.left.parent = self.parent;
        if self.parent != None: 
            if self.parent.left == self: self.parent.left = self.left;
            else:  self.parent.right = self.left;
        self.parent = self.left;
        self.left = self.parent.right;
        if self.left != None: 
            self.left.parent = self;
        self.parent.right = self;
        return self.parent;

    def leftRotate(self):
        self.right.parent = self.parent;
        if self.parent != None: 
            if self.parent.left == self: self.parent.left = self.right;
            else:  self.parent.right = self.right;
        self.parent = self.right;
        self.right = self.parent.left;
        if self.right != None: 
            self.right.parent = self;
        self.parent.left = self;
        return self.parent;

    def __str__(self):
        def Infixe(AVLs):
            if AVLs == None: return '';
            return Infixe(AVLs.left) + ' ' + str(AVLs.val) + ' ' + Infixe(AVLs.right);
        # return Infixe(self);        
        def prefixe(AVLs):
            if AVLs == None: return '';
            return str(AVLs.val) + ' ' + prefixe(AVLs.left) + ' ' + prefixe(AVLs.right);
        return "Infixe: "+Infixe(self) + ", prefixe: "+prefixe(self);
    
    def getBalance(self):
        if self.right == None and self.left == None: return 0;
        if self.right == None: return -self.left.height-1;
        if self.left == None: return self.right.height+1;
        return self.right.height - self.left.height;

    def getHeight(self):
        if self.right == None and self.left == None: return 0;
        if self.right == None: return self.left.height+1;
        if self.left == None: return self.right.height+1;
        return max(self.right.height, self.left.height)+1;

avl = Avl(9);
avl = avl.add(Avl(10));
avl = avl.add(Avl(4));
avl = avl.add(Avl(3));
avl = avl.add(Avl(7));
avl = avl.add(Avl(5));
avl = avl.add(Avl(8));

print(avl)
            

