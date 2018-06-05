from affine import Affine

class Atbash(Affine):
    def __init__(self):
        super().__init__(25, 25)