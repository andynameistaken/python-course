class Fish:
    def __init__(self, first_name, last_name="Fish",
                 skeleton="bone", eyelids=False):
        self.first_name = first_name
        self.last_name = last_name
        self.skeleton = skeleton
        self.eyelids = eyelids

    def swim(self):
        print("The fish is swimming.")

    def swim_backwards(self):
        print("The fish can swim backwards.")


class Clownfish(Fish):
    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.")


class Trout(Fish):
    def __init__(self, water="freshwater"):
        self.water = water
        super().__init__(self)


def main():
    terry = Trout()
    terry.first_name = "Terry"
    # Use parent __init__() through super()
    print(str(terry.first_name) + " ---- " + str(terry.last_name))
    print(terry.eyelids)

    # Use child __init__() override
    print(terry.water)

    # Use parent swim() method
    terry.swim()




if __name__ == '__main__':
    main()
