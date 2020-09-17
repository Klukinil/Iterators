import hashlib

class MD5Generator:

    def __init__(self, file):
        self.file = file

    def __iter__(self):
        pass
        return self

    def md5_generator(self):
        with open(self.file) as f:
            for line in f:
                yield print('Cтрока:', line, 'md5 хэш: ', hashlib.md5(line.encode()).hexdigest())
                print()