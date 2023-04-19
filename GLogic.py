#This is Breaker GLogic, for Gate Logic, this will allow quick access to AND OR NOR NOT and XOR gates (More Gates will be added if needed)

# AND GATE

@_('INPUT AND INPUT')
def statement(self, t):
  if t.INPUT1 == True:
    if t.INPUT2 == True:
      blockPrint()
      return '1'
    else:
      blockPrint()
      return '0'
  else:
    blockPrint()
    return '0'

# OR GATE

# NOR GATE

# XOR GATE

# NOT GATE
