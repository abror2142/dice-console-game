class ProbabilityCalculation:

    def __init__(self, dice_a, dice_b):
        self.dice_a = dice_a
        self.dice_b = dice_b

    def calculate(self):
        n = 0
        for x in self.dice_a:
            for y in self.dice_b:
                if x > y: n+=1
        return round(n/36, 4)