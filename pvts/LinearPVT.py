
class LinearPVT:
    k   = 10 * 9.8692326671601e-16
    B   = 1
    ct  = 8.8087848201176633e-08
    rho = 1000 
    phi = 0.1 
    mu = 1e-3
    
    def __init__(self) -> None:
        pass
    
    @property
    def get_k(self):
        return self.k
    
    @property
    def get_B(self):
        return self.B
    
    @property
    def get_ct(self):
        return self.ct
    
    @property
    def get_rho(self):
        return self.rho
    
    @property
    def get_phi(self):
        return self.phi
    
    @property
    def get_mu(self):
        return self.mu
    