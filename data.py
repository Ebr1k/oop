
class data:
    def __init__(self, arch=None, inp="", out=""):
        self.setArch(arch)
        self.setInp(inp)
        self.setOut(out)

    def setArch(self, value): self.__arch = value
    def setInp(self, value): self.__inp = value
    def setOut(self, value): self.__out = value

    def getArch(self): return self.__arch
    def getInp(self): return self.__inp
    def getOut(self): return self.__out

    def readFile(self, filename):
        self.setInp(filename)
        self.read()
    def writeFile(self, filename):
        self.setOut(filename)
        self.write()
    def read(self): pass
    def write(self): pass