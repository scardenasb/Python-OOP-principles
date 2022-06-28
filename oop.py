# NOTE: Class1, parent and grandparent class
class TheFreePeoplesOfTheWorld:
    common_final_mission = (
        "To destroy The Ring"
    )  # NOTE: Class attributes shall apply to every member of the class (is declared before constructor)

    def __init__(
        self, name, mission: None, weapon
    ):  # NOTE: Instance constructor with its instance attributes (values may differ from object to object)
        self.name = name
        self.mission = mission
        self.weapon = weapon

    def description(self):  # NOTE: Method 1
        print(
            "\n｢{0} Profile｣\nName: {0}\nMission: {1}\nWeapon: {2}".format(
                self.name, self.mission, self.weapon
            )
        )

    def attack(
        self
    ):  # NOTE: Method 2, every member of TheFreePeoplesOfTheWorld can attack (child classes included)
        if self.weapon is not None:
            print("\n｢{0}｣\n-Attacks with his {1}-\n".format(self.name, self.weapon))
        else:
            print("\n｢{0}｣\nYou do not have any weapon to use 😰\n".format(self.name))


# NOTE: Class2 and child1 of class1 with no new attributes
class Hobbits(
    TheFreePeoplesOfTheWorld
):  # NOTE: If a child doesn't have new attributes and its parent has a constructor,it is not necessary to create a new one
    def cook(self):
        print("｢{0}｣\n-is cooking-".format(self.name))


# NOTE: Class3 and child2 of class1 with a protected method (single '_foo', use double to make a protected one '__foo')
class Elves(TheFreePeoplesOfTheWorld):
    def __init__(
        self, name, mission, weapon, supplies
    ):  # NOTE: New instance constructor because this class add supplies
        super().__init__(
            name, mission, weapon
        )  # NOTE: Super() function to call parent constructor, not 'self' argument needed just attributes inside
        self.supplies = supplies
        self._give_item = None  # NOTE: Protected instance attribute

    @property  # NOTE: @property decorator acts as a getter and sets the given Docstring to the method so you can read important info before use it
    def give_item(self):
        """This is a protected method to give the right object to the right person"""
        return self._give_item

    @give_item.setter  # NOTE: A @property object has a built in getter, setter and a deleter method usable as decorators
    def give_item(self, obj):
        print("｢{0} got a new item: {1}｣".format(self.name, obj))
        self._give_item = obj

    @give_item.deleter
    def give_item(self):
        print("｢{0} has not his/her {1} anymore｣".format(self.name, self._give_item))
        del self._give_item


# NOTE: Class3, child1 of class2, child1 of class3 so is grandchild of class1 (multiple inheritance)
class TheFellowshipOfTheRing(
    Hobbits, Elves
):  # NOTE: Python prioritize the first argument's constructor, in this case Hobbits
    def __init__(
        self, name, mission, weapon, supplies, ring: str
    ):  # NOTE: New attribute, 'ring' (string type, to check if the ring is The Ring)
        Hobbits.__init__(
            self, name, mission, weapon
        )  # NOTE: Multiple inheritance calls the specific parent constructor and 'self' argument (instead of super() function)
        Elves.__init__(self, name, mission, weapon, supplies)
        self.ring = ring

    def put_ring(self):  # NOTE: Method 1 with an attribute's condition
        if self.ring == "The Ring":
            print(
                "\n｢{0}｣\n-Is hiding- Beware of Nazgûl Riders! 🏇🏇\n".format(self.name)
            )
        else:
            print(
                "\n｢{0}｣\nYou do not have the right ring, you can not hide!\n".format(
                    self.name
                )
            )

    def attack(
        self
    ):  # NOTE: This attack method override the one inherited from TheFreePeoplesOfTheWorld, and add special 'attacks' (Polymorphism)
        if self.name == "Gandalf":
            print("\n｢{0}｣\nYou shall not pass!! 🧙\n".format(self.name))
        elif self.weapon is not None:
            print("\n｢{0}｣\n-Attacks with his {1}-\n".format(self.name, self.weapon))
        else:
            print("\n｢{0}｣\nYou do not have any weapon to use 😰\n".format(self.name))

    def description(self):  # NOTE: Method 3
        TheFreePeoplesOfTheWorld.description(
            self
        )  # NOTE: Inheritance of the 'description' grandparent's method
        print(
            "Supplies: {0}\nItem: {1}\nRing: {2}".format(
                self.supplies, self.give_item, self.ring
            )
        )


frodo = TheFellowshipOfTheRing(
    "Frodo", "Destroy The Ring", "Sword", None, "The Ring"
)  # NOTE: TheFellowshipOfTheRing have 5 attributes but there is a 6th protected one 'item'
sam = TheFellowshipOfTheRing(
    "Sam", "Protect The Ring bearer", None, "Elven bread", None
)
gandalf = TheFellowshipOfTheRing(
    "Gandalf", "Protect The Ring bearer", "Staff", "Pipe", None
)
bilbo = Hobbits("Bilbo Baggins", "Wrote a book", None)
frodo.give_item = (
    "Phial of Galadriel"
)  # NOTE: Set a value thanks to the setter decorator.
frodo.description()  # NOTE: This description is related to the Hobbits's one (Ln 70), which will display its parent description first (Ln 72)
# frodo.put_ring()
# frodo.attack()   # NOTE: Attack is a method of TheFreePeoplesOfTheWorld, Hobbits inherit this method through the Hobbits class
# del frodo.give_item   # NOTE: Can delete items calling the deleter decorator
# sam.give_item = 'Rope'
# sam.description()
# del sam.give_item
# gandalf.description()
# gandalf.attack()
# bilbo.description()
# bilbo.cook()
# print(frodo.common_final_mission)
