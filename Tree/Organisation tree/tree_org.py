# tree structute of organisation

class Node:
  def __init__(self,data):
    self.data = data
    self.children = []
    self.parent = None

  def get_level(self):
    level = 0
    p = self.parent
    while p:
      level+=1
      p = p.parent

    return level
      
    
  def add_child(self,child):
    child.parent = self
    self.children.append(child)

  def print_tree(self):
    spaces = ' '* self.get_level()*3
    prefix = spaces + "|__" if self.parent else ""
    print(prefix+self.data)
    if self.children:
      for child in self.children:
        child.print_tree()

def build_tree():
  root = Node('CEO')

  #Finance
  fi = Node('VP_Finance')
  ca1 = Node('Chief Accountant 1')
  ca1.add_child(Node('Junior Accountant'))
  ca2 = Node('Chief Accountant 2')
  
  fi.add_child(ca1)
  fi.add_child(ca2)

  #manufacture
  manu = Node('VP_Manufacture')
  
  pm1 = Node('Plant Manager 1')
  pm2 = Node('Plant Manager 2')
  pm2.add_child(Node('Maintenance Supervisor'))
  
  manu.add_child(pm1)
  manu.add_child(pm2)

  #Marketing 
  mar = Node('VP_Marketing')
  
  sm = Node('Sales Manager')
  am = Node('Advertising Manager')
  am.add_child(Node('Account Executive'))
  
  mar.add_child(sm)
  mar.add_child(am)
  
  #HR

  hr = Node('VP_HR')

  hrm = Node('HR Manager')
  re = Node('Recruit Executive')
  ben = Node('Benifits')
  ben.add_child(Node('Recruiters 1'))
  ben.add_child(Node('Recruiters 2'))

  hr.add_child(hrm)
  hr.add_child(re)
  hr.add_child(ben)

  
  root.add_child(fi)
  root.add_child(manu)
  root.add_child(mar)
  root.add_child(hr)
  
  root.print_tree()

if __name__ == "__main__":
  build_tree()
  pass