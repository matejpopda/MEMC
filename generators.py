



class congruent_period:
    def __init__(self, seed, prime, root) -> None:
        self.x=seed
        self.prime=prime
        self.root=root

    def get(self):
        self.x = self.x*self.root % self.prime
        return self.x
    
    def get_float(self):
        self.x = self.x*self.root % self.prime
        return self.x/self.prime