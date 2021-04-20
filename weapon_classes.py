"""Weapon Class main document."""


class Weapon:
    """Class to create a main gunnery weapons for board game Panzer and MBT.

    List of Parameters
    ----------
    
    wpn_name : str, weapon name,
    r_p : int, range point blank,
    r_s : int, range short,
    r_m : int, range medium,
    r_l : int, range long,
    r_e : int, range extreme,
    p_p : int, penetration factor point blank,
    p_s : int, penetration factor short,
    p_m : int, penetration factor medium,
    p_l : int, penetration factor long,
    p_e : int, penetration factor extreme,
    """

    def __init__(self, wpn_name, r_p, r_s, r_m, r_l, r_e, p_p, p_s, p_m, p_l, p_e):
        self.wpn_name = wpn_name
        self.r_p = r_p
        self.r_s = r_s
        self.r_m = r_m
        self.r_l = r_l
        self.r_e = r_e
        self.p_p = p_p
        self.p_s = p_s
        self.p_m = p_m
        self.p_l = p_l
        self.p_e = p_e
