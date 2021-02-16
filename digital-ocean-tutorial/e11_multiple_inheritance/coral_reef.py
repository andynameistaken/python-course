
class Coral:
    def __init__(self):
        print("Coral __init__")
    def community(self):
        print("Coral lives in a community.")


class Anemone:
    def __init__(self):
        print("Anemone __init__")

    def protect_clownfish(self):
        print("The anemone is protecting the clownfish.")


class CoralReef(Anemone, Coral):
    pass

great_barrier = CoralReef()
great_barrier.community()
great_barrier.protect_clownfish()