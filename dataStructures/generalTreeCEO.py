class TreeNodes:
    def __init__(self, data, position):
        self.data = data
        self.position = position
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + self.data + ' (' + self.position + ')')
        if self.children:
            for child in self.children:
                child.print_tree()
    

def build_product_tree():
    CEO = TreeNodes('Nilupul', 'CEO')

    CTO = TreeNodes('Chinmay', 'CTO')

    IH = TreeNodes('Vishwa', 'IH')
    AH = TreeNodes('Aamir', 'Application Head')

    CM = TreeNodes('Dhaval', 'Cloud Manager')
    AM = TreeNodes('Abdi', 'App Manager')

    HR = TreeNodes('Gels', 'HR head')

    RM = TreeNodes('Peter', 'Recruitment Manager')
    PM = TreeNodes('Waqas', 'Policy Manager')

    IH.add_child(CM)
    IH.add_child(AM)
    HR.add_child(RM)
    HR.add_child(PM)
    CTO.add_child(IH)
    CTO.add_child(AH)
    CEO.add_child(HR)
    CEO.add_child(CTO)

    CEO.print_tree()

if __name__ == '__main__':
    build_product_tree()