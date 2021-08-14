import random
mt_list = [1,2,3,4,5,6,7,8,"c","d"]
random.shuffle(mt_list)

class CustomException1(Exception):
    def __init__(self, msg1 = None, num = None):
        self.msg = f"Input is not a number"
        if msg1:
            self.msg = msg1
    
    def __str__(self) -> str:
        return repr(str(self.msg))

try:
    for i in mt_list:
        if not isinstance(i, int):
            raise CustomException1(f"Unexpected value : {i}")
except CustomException1 as exe:
    print (exe)