import numpy as np

class Well:
    def __init__(
        self,
        well_position: float,
        rad_well: float,
        skin: float,
        q_rate: float,
        well_h: float
    ):
        self.well_position = well_position
        self.r_w = rad_well
        self.skin = skin
        self.q_rate = q_rate * 1.157 * 10e-5
        self.well_h = well_h
        
        self.pwf = []
        
    
    def get_well_index(
        self, 
        cell_radius: float,
        lam: float,
        h: float = 10
    ):
        if(self.r_w >= cell_radius):
            raise ValueError("r_w is too small")
    
        return 2 * np.pi * h * lam / (np.log(2 * cell_radius / self.r_w) + self.skin)
    
    
    def write_pwf(self, pwf: float):
        self.pwf.append(pwf)
    
    @property
    def get_rw(self):
        return self.r_w
    
    @property
    def get_skin(self):
        return self.skin
    
    @property
    def get_q(self):
        return self.q_rate
    
    @property
    def get_well_position(self):
        return self.well_position
    
    @property
    def get_pwf(self):
        return self.pwf
    
        