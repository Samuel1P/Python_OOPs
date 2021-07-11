
class room:

    def __init__(self, name, work):
        self.name = name
        self.work = work

    @property
    def email(self):
        return self.name+"@"+self.work+".com"

    @email.setter
    def email(self, email_id):
        name = email_id.split("@")
        self.name = name[0]
        self.work = name[1][:-4]

    @email.deleter
    def email(self):
        self.name = None
        self.work = None
        del self.work

pers1 = room("jim", "oracle")
pers2 = room("jan", "apple")

print (pers1.email)
pers1.name = "Tom"
print (pers1.email)
print(pers2.email)
pers1.email = "samuel@accenture.com"
print (pers1.name)
print (pers1.__dict__)
del pers1.email
print (pers1.__dict__)