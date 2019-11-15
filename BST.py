class BST:
    def __init__(self, info, parent=None, right=None, left=None):
        self.info = info;
        self.right = right;
        self.left = left;
        self.parent = parent;
    
    def add(self, info):
        def adding(this):
            if this.info >= info:
                if this.left == None: 
                    this.left = BST(info, this);
                    return;
                else: adding(this.left);
            else:
                if this.right == None: 
                    this.right = BST(info, this);
                    return;
                else: adding(this.right);
        adding(self);

    def addNode(self, info):
        def adding(this):
            if this.info >= info.info:
                if this.left == None: 
                    this.left = info;
                    info.parent = this;
                    return;
                else: adding(this.left);
            else:
                if this.right == None: 
                    this.right = info;
                    info.parent = this;
                    return;
                else: adding(this.right);
        adding(self);
    
    def __str__(self):
        def Infixe(BSTs):
            if BSTs == None: return '';
            return Infixe(BSTs.left) + ' ' + str(BSTs.info) + ' ' + Infixe(BSTs.right);
        return Infixe(self);        

    def remove(self, info):
        def removing(this):
            if this.info == info:
                parent = this.parent;
                leftchild = this.left;
                rightchild = this.right;
                if(this.info == parent.left.info):
                    parent.left = None;
                else:
                    parent.right = None;
                if leftchild != None: parent.addNode(leftchild)
                if rightchild != None: parent.addNode(rightchild)
            else:
                if this.info >= info: removing(this.left);
                else: removing(this.right);
        removing(self);

    """
        l'arbre doit étre Arbre Binaire de Recherche;
        parce que ma methode propage just vers le droit, et retourne le dernier element du droit.
        la compléxité c'est O(log(n)) parce que a chaque fois je parcour just la moitié de la branche.
    """
    def MaxNodeRecurs(self): 
        if(self.right == None):
            return self.info;
        return self.right.MaxNode();
   
    """
        l'arbre doit étre Arbre Binaire de Recherche;
        ici j'utilise les references pour retourne le dernier element du droit.
        la compléxité c'est O(log(n)) parce que a chaque fois je parcour just la moitié de la branche.
    """
    def MaxNodeIter(self):
        bstree = self;
        while bstree.right != None:
            bstree = bstree.right;
        return bstree.info;

BSTree = BST(5);
BSTree.add(3);
BSTree.add(2);
BSTree.add(1);
BSTree.add(6);
BSTree.add(4);
BSTree.add(8);
BSTree.add(7);
BSTree.add(9);
print(BSTree)
BSTree.remove(1);
print(BSTree)
print("le maximum est : "+str(BSTree.MaxNodeIter()));