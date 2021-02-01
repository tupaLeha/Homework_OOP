class Chlorine(object):
    tFreeze = -100
    tMelt = -100
    tVaporization = -34
    def agg_state(self, unit, t):
        if unit == 'kel':
            t = t - 273.15
        elif unit == 'fa':
            t = (t-32) / 1.8
        elif unit == 'cel':
            pass
        if t < self.tFreeze:
            return print('Твёрдый')
        elif t == self.tMelt:
            return print('Жидкий')
        elif t >= self.tVaporization:
            return print('Газообразный')
chlorine_agg_state = Chlorine()
print(chlorine_agg_state.agg_state('cel', -101))
