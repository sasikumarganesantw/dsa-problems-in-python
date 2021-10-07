class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data;
        self.left = left;
        self.right = right;

    def insert(self, data):
        if data <= self.data:
            if self.left is None:
                self.left = Tree(data);
            else:
                self.left.insert(data);
        else:
            if data > self.data:
                if self.right is None:
                    self.right = Tree(data);
                else:
                    self.right.insert(data);
        return True;

    def print_tree_inorder(self):
        if self.left is not None:
            self.left.print_tree_inorder();
        print(self.data);
        if self.right is not None:
            self.right.print_tree_inorder();

    def print_tree_preorder(self):
        print(self.data);
        if self.left is not None:
            self.left.print_tree_preorder();
        if self.right is not None:
            self.right.print_tree_preorder();

    def print_tree_postorder(self):
        if self.left is not None:
            self.left.print_tree_postorder();

        if self.right is not None:
            self.right.print_tree_postorder();
        print(self.data);

    def find_val(self, data):
        if data < self.data:
            if self.left is None:
                print("%d not found" % data);
            else:
                self.left.find_val(data);
        elif data > self.data:
            if self.right is None:
                print("%d not found" % data);
            else:
                self.right.find_val(data);
        else:
            print("%d found" % data)

if __name__ == "__main__":
    tree = Tree(6);
    tree.insert(5);
    tree.insert(7);
    tree.insert(8);
    tree.insert(3);
    tree.insert(3);
    print('inorder');
    tree.print_tree_inorder();
    print('--------------');
    print('preorder');
    tree.print_tree_preorder();
    print('--------------');
    print('postorder');
    tree.print_tree_postorder();
    print('--------------');
    tree.find_val(7);
    tree.find_val(9);