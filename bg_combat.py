"""Basic Game Combat Logic."""

from vehicle_classes import ArmorFightingVehicle


def basic_game_ap_combat(shooter, target):
    t_range = input("Enter range in hexes: ")
    t_moving = input("Is target moving (y/n)? ")
    # t_size = target.size
    t_cover = input("What is target cover (light/medium/heavy)? ")
    s_damaged = input("Is shooter damaged (y/n)? ")
    bu_smoke = input("Enter total amount of intervening brew up smoke hexes: ")
    s_order = input("What is shooter's order type (fire/short-halt/overwatch)? ")
    if s_order == "overwatch":
        s_over_adj = input("Is this shot overwatch adjust (y/n)? ")
        return t_range, t_moving, t_cover, s_damaged, bu_smoke, s_order, s_over_adj
    else:
        return t_range, t_moving, t_cover, s_damaged, bu_smoke, s_order
