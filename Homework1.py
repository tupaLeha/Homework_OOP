class Element():
    def convertation(self, unit, t):
        if unit == 'kel':
            return t - 273.15
        elif unit == 'fa':
            return (t-32) / 1.8
        elif unit == 'cel':
            return t
    def agg_state(self, unit, t):
        t = self.convertation(unit, t)
        if t <= self.tFreeze:
            return print('Твёрдый')
        elif t < self.tVaporization:
            return print('Жидкий')
        elif t >= self.tVaporization:
            return print('Газообразный')
class Chlorine(Element):
    tFreeze = -100
    tMelt = -100
    tVaporization = -34
chlorine_agg_state = Chlorine()
chlorine_agg_state.agg_state('cel', -101)
