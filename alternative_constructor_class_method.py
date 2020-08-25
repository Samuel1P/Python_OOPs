# program  converts input in  bytes to appropriate readable file unit.
# sometimes the value may not be sent in bytes
# some user may send MB, we need an alternative constructor for those users
# init constructor - takes care of bytes inputs
# mb_converter is an alternative constructor - takes input from MB passing users

class bytes_converter:
    avail_unit = ["B","KB","MB","G","T"]
    def __init__(self, inp):
        self.value = inp

    def converted_value(self):
        for unit in self.avail_unit:
            if self.value < 1024:
                break
            self.value = self.value / 1024
        return round(self.value, 2), unit

    @classmethod
    def mb_converter(cls, mb_value):
        x = mb_value * 1024 *1024
        # x = x * 1024
        print (x)
        return cls(x)

normal_ins = bytes_converter(10222)
print (normal_ins.converted_value())

alt_ins = bytes_converter.mb_converter(1024323)
print (alt_ins.converted_value())
