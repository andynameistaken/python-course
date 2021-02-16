from lessons.e10_inheritance.fish import Fish


class Trout(Fish):
    def __init__(self, water = "freshwater"):
        self.water = water
        super().__init__(self)


def main():
    terry = Trout("Terry")
    print(terry.first_name + " " + terry.last_name)
    print(terry.skeleton)
    print(terry.eyelids)
    terry.swim()
    terry.swim_backwards()


if __name__ == '__main__':
    main()