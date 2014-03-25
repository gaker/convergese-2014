
<h1>Crash Course <small>(cont'd)</small></h1>

    class BadMath(object):
        def __init__(self, number):
            self.number = number

        def add_one(self):
            self.number = self.number + 1
            return self.number

        def minus_one(self):
            self.number = self.number - 1
            return self.number
