from __future__ import annotations


class Knight:
    def __init__(self, parameters: dict) -> None:
        self.name = parameters["name"]
        self.hp = parameters["hp"]

        self.protection = 0
        for armour in parameters["armour"]:
            self.protection += armour["protection"]

        self.power = parameters["power"] + parameters["weapon"]["power"]

        if parameters["potion"] is not None:
            if "power" in parameters["potion"]["effect"]:
                self.power += parameters["potion"]["effect"]["power"]

            if "protection" in parameters["potion"]["effect"]:
                self.protection += parameters["potion"]["effect"]["protection"]

            if "hp" in parameters["potion"]["effect"]:
                self.hp += parameters["potion"]["effect"]["hp"]

    def knights_buttle(self, other: Knight) -> None:
        self.hp -= other.power - self.protection
        other.hp -= self.power - other.protection
        if self.hp <= 0:
            self.hp = 0
        if other.hp <= 0:
            other.hp = 0
