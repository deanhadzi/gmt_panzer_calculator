from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.orm import relationship
from db import Base


class Weapon(Base):
    """Weapon Catalog."""

    cd = Column(String(50), primary_key=True)
    name = Column(String(100), nullable=False)


class Ammo(Base):
    """Ammo Catalog."""

    cd = Column(String(50), primary_key=True)
    name = Column(String(100), nullable=False)


class Armor(Base):
    """Armor Catalog."""

    cd = Column(String(50), primary_key=True)
    name = Column(String(100), nullable=False)


class UnitType(Base):
    """Unit Type lookup."""

    cd = Column(String(50), primary_key=True)
    name = Column(String(100), nullable=False)


class Unit(Base):
    """Unit Catalog."""

    cd = Column(String(50), primary_key=True)
    name = Column(String(100), nullable=False)
    unittype_cd = Column(String(50), ForeignKey("unittype.cd"), nullable=False)

    unittype = relationship("UnitType", backref="units")


class Actor(Base):
    """Acting Unit."""

    id = Column(Integer, primary_key=True)
    unit_cd = Column(String(50), ForeignKey("unit.cd"), nullable=False)
    armor_cd = Column(String(50), ForeignKey("armor.cd"))
    health = Column(Integer, nullable=False)

    unit = relationship("Unit", backref="actors")
    armor = relationship("Armor", backref="actors")


class ActorWeapon(Base):
    """Actor Weapon association."""

    id = Column(Integer, primary_key=True)
    actor_id = Column(Integer, ForeignKey("actor.id"), nullable=False)
    weapon_cd = Column(String(50), ForeignKey("weapon.cd"), nullable=False)

    actor = relationship("Actor", backref="weapons")
    weapon = relationship("Weapon", backref="actors")


class ActorAmmo(Base):
    """Actor Ammo association."""

    id = Column(Integer, primary_key=True)
    actor_id = Column(Integer, ForeignKey("actor.id"), nullable=False)
    ammo_cd = Column(String(50), ForeignKey("ammo.cd"), nullable=False)
    rounds = Column(Integer, nullable=False)

    actor = relationship("Actor", backref="ammos")
    ammo = relationship("Ammo", backref="actors")

