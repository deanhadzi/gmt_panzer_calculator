from tank_factory import create_tank
from dice import Die

d100 = Die(100)

target_range = {"P": 90, "S": 70, "M": 50, "L": 30, "E": 10}

# TODO
# Input attacker, defender.
# Input angle of attack.
# Input target range.
# Check if the target range is greater than attackers extreme range. If it does return to previous step.
# Find appropriate target roll in target range dict.
# Roll dice. If the roll is equal or less than the target roll check if attackers gun penetrates defender's armor.
# Implement hit logic.

def bg_direct_fire_step(shooter, defender):

    # Create both tanks.
    attk = create_tank(shooter)
    dfnd = create_tank(defender)

    # Input shot relevant data.
    aoa = input('Input angle of attack (front/rear): ')
    rng = int(input("Input range to defender unit: "))

    # Check if the target is out of range.
    if rng > attk.off_info.r_e:
        print(f"Incorrect range, input value between 1 and {attk.off_info.r_e}.")
        rng = int(input("Input range to defender unit: "))

    # Determine target roll based on range.
    target_roll = 0
    pen_factor = 0

    if rng <= attk.off_info.r_p:
        target_roll = target_range["P"]
        pen_factor = attk.off_info.p_p
    elif rng <= attk.off_info.r_s:
        target_roll = target_range["S"]
        pen_factor = attk.off_info.p_s
    elif rng <= attk.off_info.r_m:
        target_roll = target_range["M"]
        pen_factor = attk.off_info.p_m
    elif rng <= attk.off_info.r_l:
        target_roll = target_range["L"]
        pen_factor = attk.off_info.p_l
    else:
        target_roll = target_range["E"]
        pen_factor = attk.off_info.p_e

    # Execute attack.
    die_roll = d100.roll_dice()
    dmg_amt = 0

    if die_roll > target_roll:
        print('Shot was ineffective.')
    else:
        if aoa == 'front':
            dmg_amt = pen_factor - dfnd.notes.bgaf
        elif aoa == 'rear':
            dmg_amt = pen_factor - dfnd.notes.bgar

    # Determine damage.
    if dmg_amt <= 0:
        print("Shot connected, but has no effect.")
    elif dmg_amt <= 3:
        print("Target is damaged.")
    elif dmg_amt <= 9:
        print("Target is knocked out.")
    elif dmg_amt >= 10:
        print("Target brews-up.")

    # Print values.
    print(f"Target roll: {target_roll}")
    print(f"Die roll: {die_roll}")
    print(f"Penetration factor: {pen_factor}")
    print(f"Damage amount: {dmg_amt}")

if __name__ == '__main__':
    bg_direct_fire_step('T34/85 M44', 'T34/76 M43')