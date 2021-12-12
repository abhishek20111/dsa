# class TreeNodes:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None
#
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level +=1
#             p = p.parent
#         return level
#
#     def print_tree(self):
#         space = ' ' * self.get_level() * 3
#         prefix = space + "|--"if self.parent else ""
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree()
#
#     def add_children(self, child):
#         child.parent = self  # as in input the children adress come to self so child.parent value we give self
#         self.children.append(child)
#
#
# def build_product_tree():
#     root = TreeNodes("Electronic")
#
#     laptop = TreeNodes("laptop")  # it store object as a laptop
#     laptop.add_children(TreeNodes("ideapad"))
#     laptop.add_children(TreeNodes("Lenvo"))
#     laptop.add_children(TreeNodes("i-pad"))
#
#     cellphone = TreeNodes("Cell phone")
#     cellphone.add_children(TreeNodes("iphone"))
#     cellphone.add_children(TreeNodes("Google Pixel"))
#     cellphone.add_children(TreeNodes("Vivo"))
#
#     tv = TreeNodes("TV")
#     tv.add_children(TreeNodes("Samsung"))
#     tv.add_children(TreeNodes("Ml"))
#     tv.add_children(TreeNodes("LG"))
#
#     root.add_children(laptop)
#     root.add_children(cellphone)
#     root.add_children(tv)
#
#     root.print_tree()
#
#
# if __name__ == '__main__':
#     root = build_product_tree()
#  ----------------------------------------------------------------Pratice-----------------------------------------------------------

# class TreeNode:
#     def __init__(self, data):
#         self.data = data
#         self.children = []
#         self.parent = None
#
#     def get_level(self):
#         level = 0
#         p = self.parent
#         while p:
#             level += 1
#             p = p.parent
#         return level
#
#     def print_tree(self):
#         space = ' ' * self.get_level() * 3
#         prefix = space + "|-- "if self.parent else ""
#         print(prefix + self.data)
#         if self.children:
#             for child in self.children:
#                 child.print_tree()
#
#     def add_children(self, child):
#         child.parent = self
#         self.children.append(child)
#
# def build_product_tree():
#     root = TreeNode("Electronic")
#
#     laptop = TreeNode("Laptop")
#     laptop.add_children(TreeNode("Ideapad"))
#     laptop.add_children(TreeNode("IOS"))
#     laptop.add_children(TreeNode("HP"))
#
#     tv = TreeNode("TV")
#     tv.add_children(TreeNode("MI"))
#     tv.add_children(TreeNode("LG"))
#     tv.add_children(TreeNode("Samsung"))
#
#     phone = TreeNode("Phone")
#     phone.add_children(TreeNode("Vivo"))
#     phone.add_children(TreeNode("Oppo"))
#     phone.add_children(TreeNode("KI"))
#
#     root.add_children(laptop)
#     root.add_children(tv)
#     root.add_children(phone)
#
#     root.print_tree()
#
# if __name__ == '__main__':
#     build_product_tree()]


#  --------------------------------------------------------Exrecise---------------------

# class TreeNode:
#     def __init__(self,name, designation):
#         self.name = name
#         self.designation = designation
#         self.children = []
#         self.parent = None
#
#     def get_lenth(self):
#         level = 0
#         p = self.parent
#
#         while p:
#             level +=1
#             p = p.parent
#         return level
#
#     def print_tree(self, propert_name):
#         if propert_name == 'both':
#             value = self.name + " (" + self.designation + ")"
#         elif propert_name == 'name':
#             value = self.name
#         else:
#             value = self.designation
#
#         space = ' ' * self.get_lenth() * 3
#         prefix = space + "|--"if self.parent else""
#         print(prefix + value)
#         if self.children:
#             for child in self.children:
#                 child.print_tree(propert_name)
#
#     def add_child(self, child):
#         child.parent = self
#         self.children.append(child)
#
# def build_management_tree():
#     #  CTO mangment
#     infra_head = TreeNode("Vishua","Infrastructure Head")
#     infra_head.add_child(TreeNode("Dhaval", "Cloud Manager"))
#     infra_head.add_child(TreeNode("Abhijit", "App Manger"))
#
#     cto = TreeNode("Chinmey","CTO")
#     cto.add_child(infra_head)
#     cto.add_child(TreeNode("Amir", "Application Head"))
#
#     #HR hierarcy
#     hr_head = TreeNode("gels", "HR Head")
#
#     hr_head.add_child(TreeNode("Peter", "Recuitment Manger"))
#     hr_head.add_child(TreeNode("Waqas", "Policy Mangeger"))
#
#     ceo = TreeNode("Nilupl","CEO")
#     ceo.add_child(cto)
#     ceo.add_child(hr_head)
#
#     return ceo
#
# if __name__ == '__main__':
#     root_node = build_management_tree()
#     root_node.print_tree("name")
#     print("\n\n")
#     root_node.print_tree("designation")
#     print("\n\n")
#     root_node.print_tree("both")
#---------------------------------------------------Practice----------------------------

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level
    def print_tree(self, level):
        if self.get_level() > level:
            return
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|--"if self.parent else""
        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree(level)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

def build_location_tree():
    root = TreeNode("Global")

    india = TreeNode("India")

    gujarat = TreeNode("Gujarat")
    gujarat.add_child(TreeNode("Ahmedabad"))
    gujarat.add_child(TreeNode("Baroda"))

    karnataka = TreeNode("Karnataka")
    karnataka.add_child(TreeNode("Bangluru"))
    karnataka.add_child(TreeNode("Mysore"))

    india.add_child(gujarat)
    india.add_child(karnataka)

    usa = TreeNode("USA")

    nj = TreeNode("New Jersey")
    nj.add_child(TreeNode("Princeton"))
    nj.add_child(TreeNode("Trenton"))

    california = TreeNode("California")
    california.add_child(TreeNode("San Francisco"))
    california.add_child(TreeNode("Mountain View"))
    california.add_child(TreeNode("Palo Alto"))

    usa.add_child(nj)
    usa.add_child(california)

    root.add_child(india)
    root.add_child(usa)

    return root
if __name__ == '__main__':
    root_mode = build_location_tree()
    root_mode.print_tree(1)
    print("\n")
    root_mode.print_tree(2)
    print("\n")
    root_mode.print_tree(3)