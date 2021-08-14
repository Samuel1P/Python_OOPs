class File:
    ext = "jpeg"
    name = "image"

    def say_file():
        print(f"Hello There")


File.say_file()


print (File.__dict__)

print (File.say_file)
