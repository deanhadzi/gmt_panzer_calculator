class VehUnitId:
    """
    Class representing the top row of the Vehicle Data Card.
    :param dc_id: str, data card id number,
    :param veh_name: str, vehicle name,
    :param nat: str, vehicle nationality,
    :param bu: int bool, does a unit have a special brew-up rule,
    :param radio: int bool, does a unit have a radio,
    :param pts: int, victory point amount.
    """

    def __init__(self, dc_id, veh_name, nat, bu, radio, pts):
        self.dc_id = dc_id
        self.veh_name = veh_name
        self.nat = nat
        self.bu = bu
        self.radio = radio
        self.pts = pts

    def __repr__(self):
        return f"{self.dc_id}, {self.veh_name}, {self.nat}, {self.bu}, {self.radio}, {self.pts}"


class VehGenInfo:
    """
    Class representing the second row of the Vehicle Data Card.
    :param mot: str, mode of traction {'T': 'tracked', 'H': 'half-track', 'W': 'wheel'},
    :param ottv: int bool, is a unit open-topped tracked vehicle,
    :param r: int bool, does a unit have a dual-controls,
    :param a: int bool, does a unit have amphibious capabilities,
    :param cc_sp: int, cross-country speed,
    :param p_sp: int, path speed,
    :param r_sp: int, road speed,
    :param b: int, unit's bog modifier,
    :param tr_t: int, transport towed units capacity,
    :param tr_l: int, transport leg units capacity,
    :param uct: int bool, does a unit have under cover transport capabilites,
    :param wt: float, weight in metric tons.
    """

    def __init__(self, mot, ottv, r, a, cc_sp, p_sp, r_sp, b, tr_t, tr_l, uct, wt):
        self.mot = mot
        self.ottv = ottv
        self.r = r
        self.a = a
        self.cc_sp = cc_sp
        self.p_sp = p_sp
        self.r_sp = r_sp
        self.b = b
        self.tr_t = tr_t
        self.tr_l = tr_l
        self.uct = uct
        self.wt = wt

    def __repr__(self):
        return (
            f"{self.mot}, {self.ottv}, {self.r}, {self.a}, {self.cc_sp}, {self.p_sp}, "
            f"{self.r_sp}, {self.b}, {self.tr_t}, {self.tr_l}, {self.uct}, {self.wt}"
        )


class VehWeaponData:
    """
    Class representing the third row of the Vehicle Data Card.
    :param wpn_name: str, gun name/type,
    :param fof: str, field of fire {'A': 'all-round', 'F': 'front only', 'R': 'rear only'},
    :param tt: int, turret turn factor in hexsides,
    :param sb: int, stabilization rating,
    :param st: str, type of gun sight {'O': 'optical'}
    :param rof: str, rate of fire {'N': 'normal', 'Q': 'quick', 'R': 'rapid', 'F': 'fast'},
    :param am: int, ammunition limit and special ammo depletions,
    :param am_a: int, AP special ammo limit,
    :param am_s: int, smoke ammo limit,
    :param am_h: int, HEAT ammo limit,
    :param am_d: int, smoke dischargers limit,
    :param smk: int bool, does a unit have an ability to fire smoke rounds,
    :param il: int bool, does a unit have an ability to fire illumination rounds.
    """

    def __init__(
        self, wpn_name, fof, tt, sb, st, rof, am, am_a, am_s, am_h, am_d, smk, il
    ):
        self.wpn_name = wpn_name
        self.fof = fof
        self.tt = tt
        self.sb = sb
        self.st = st
        self.rof = rof
        self.am = am
        self.am_a = am_a
        self.am_s = am_s
        self.am_h = am_h
        self.am_d = am_d
        self.smk = smk
        self.il = il

    def __repr__(self):
        return (
            f"{self.wpn_name}, {self.fof}, {self.tt}, {self.sb}, {self.st}, {self.rof}, "
            f"{self.am}, {self.am_a}, {self.am_s}, {self.am_h}, {self.am_d}, {self.smk}, {self.il}"
        )


class VehOffInfo:
    """
    Class representing Offensive Information section of the Vehicle Data Card.
    :param r_p: int, range point blank,
    :param r_s: int, range short,
    :param r_m: int, range medium,
    :param r_l: int, range long,
    :param r_e: int, range extreme,
    :param p_p: int, penetration factor point blank,
    :param p_s: int, penetration factor short,
    :param p_m: int, penetration factor medium,
    :param p_l: int, penetration factor long,
    :param p_e: int, penetration factor extreme.
    """

    def __init__(self, r_p, r_s, r_m, r_l, r_e, p_p, p_s, p_m, p_l, p_e):
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

    def __repr__(self):
        return (
            f"{self.r_p}, {self.r_s}, {self.r_m}, {self.r_l}, {self.r_e}, {self.p_p}, "
            f"{self.p_s}, {self.p_m}, {self.p_l}, {self.p_e}"
        )


class VehDefInfo:
    """
    Class representing Defensive Information section of the Vehicle Data Card.
    :param size: int, vehicle size, range -2 to +2.
    """

    def __init__(self, size):
        self.size = size

    def __repr__(self):
        return f"{self.size}"


class VehNotes:
    """
    Class representing Notes section of the Vehicle Data Card.
    :param bgaf: int, basic game armor front,
    :param bgar: int, basic game armor rear.
    """

    def __init__(self, bgaf, bgar):
        self.bgaf = bgaf
        self.bgar = bgar

    def __repr__(self):
        return f"{self.bgaf}, {self.bgar}"


class Tank:
    """
    Class to be used as a main Tank constructor.
    :param unit_id: list, len 6 of params required by VehUnitId class,
    :param gen_info: list, len 12 of params required by VehGenInfo class,
    :param weapon_data: list, len 13 of params required by VehWeaponData class,
    :param off_info: list, len 10 of params required by VehOffInfo class,
    :param def_info: list, len 1 of params required by VehDefInfo class,
    :param notes: list, len 2 of params required by VehNotes class.
    """

    def __init__(self, unit_id, gen_info, weapon_data, off_info, def_info, notes,):
        self.unit_id = VehUnitId(*unit_id)
        self.gen_info = VehGenInfo(*gen_info)
        self.wpn_data = VehWeaponData(*weapon_data)
        self.off_info = VehOffInfo(*off_info)
        self.def_info = VehDefInfo(*def_info)
        self.notes = VehNotes(*notes)
