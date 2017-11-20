class TalkativeInt(int):
    def __lshift__(self, other):
        print("Shift", self, "by", other)
        return int.__lshift__(self, other)


t = TalkativeInt(8)
x = (t << 3)
print(x)