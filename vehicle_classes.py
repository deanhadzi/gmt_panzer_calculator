"""Vehicle Class main document."""
from weapon_classes import Weapon


class ArmorFightingVehicle:
    """Class to create a main fighting vehicle for board game Panzer and MBT.

    List of Parameters
    ----------
    Id params:
    dc_id : str, data card id number,
    name : str, unit name,

    Point params:
    pts : int, victory points amount,

    Movement params:
    cc_sp : int, cross-country speed,
    p_sp : int, path speed,
    r_sp : int, road speed,

    Transport capacity params:
    tr_t : int, transport towed units capacity,
    tr_l : int, transport leg units capacity,

    Weight and size params:
    wt : float, weight in metric tons,
    size : int, vehicle size, range -2 to +2,

    Defensive params:
    bgaf : int, basic game armor front,
    bgar : int, basic game armor rear,

    Offensive params:
    main_wpn : str, gun name/type,
    tt : int, turret turn factor,
    sb : int, stabilization rating,
    ammo : list len 5 - default 'None'
        am : int, ammo limit,
        am_a : int, AP special ammo limit,
        am_s : int, smoke ammo limit,
        am_h : int, HEAT ammo limit,
        am_d : int, smoke dischargers limit,

    Special abilities and features params:
    bu : int as bool, default 0, does a unit have a special brew-up rule,
    radio : int as bool, default 1, does a unit have a radio,
    ottv : int bool, default 0, does a unit have an open top,
    r : int bool, default 0, does a unit have a dual control,
    a : int bool, default 0, does a unit have amphibious capabilities,
    b : int, default 0, unit's bog modifier,
    smk : int bool, default 0, does a unit have an ability to fire smoke rounds,
    il : int bool, default 0, does a unit have an ability to fire illumination rounds,

    Kwargs params:
    mot : str, mode of traction {'T': 'tracked', 'H': 'half-track', 'W': 'wheel'},
    fof : str, field of fire {'A': 'all-round', 'F': 'front only', 'R': 'rear only'},
    st : str, type of gun sight {'O': 'optical'}
    rof : str, rate of fire {'N': 'normal', 'Q': 'quick', 'R': 'rapid', 'F': 'fast'},
    """

    def __init__(
        self,
        dc_id,
        name,
        pts,
        cc_sp,
        p_sp,
        r_sp,
        tr_t,
        tr_l,
        wt,
        size,
        bgaf,
        bgar,
        main_wpn,
        tt,
        sb,
        ammo=[],
        bu=0,
        radio=1,
        ottv=0,
        r=0,
        a=0,
        b=0,
        smk=0,
        il=0,
        **kwargs
    ):
        self.dc_id = dc_id
        self.name = name
        self.pts = pts
        self.cc_sp = cc_sp
        self.p_sp = p_sp
        self.r_sp = r_sp
        self.tr_t = tr_t
        self.tr_l = tr_l
        self.wt = wt
        self.size = size
        self.bgaf = bgaf
        self.bgar = bgar
        self.main_wpn = Weapon(main_wpn)
        self.tt = tt
        self.sb = sb
        self.am = ammo[0]
        self.am_a = ammo[1]
        self.am_s = ammo[2]
        self.am_h = ammo[3]
        self.am_d = ammo[4]
        self.mot = kwargs["mot"]
        self.fof = kwargs["fof"]
        self.st = kwargs["st"]
        self.rof = kwargs["rof"]
