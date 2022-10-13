print('sw assignment')
class PB:
    def __init__(self):
      self.names = ('kim', 'lee', 'pack')
      self.phones = ('11111', '22222', '33333')

    def search(self, name):
      if name in self.names:
        idx = self.names.index(name)
        return idx
	
      else:
        return None

    def print_one(self, idx):
      name = self. names[idx]
      print("{0}{1}'s phone number is {2}".format(name[0],\
        name[1:].lower(), self.phones[idx]))

    def print_all(self):
      n = len(self.names)
      for i in range(n):
        self.print_one(i)

name = input('input your name: ')		
name = name.strip().upper()

PB = PB()

idx = search(name)
if idx != None:
    PB.print_one(idx)
else:
    print('not registered name')

PB.print_all()
 