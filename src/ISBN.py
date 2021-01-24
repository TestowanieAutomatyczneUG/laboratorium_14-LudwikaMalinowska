class ISBN:
    def check_number(self, nr):
        nr = nr.split('-')
        nr = ''.join(nr)

        if len(nr) != 13:
            return False
        suma = 0
        for i in range(len(nr)):
            if not isinstance(int(nr[i]), int):
                return False
            elif i % 2 == 0:
                suma += 1 * int(nr[i])
            elif i % 2 != 0:
                suma += 3 * int(nr[i])

        reszta = suma % 10
        if reszta == 0:
            reszta = 10
        if 10 - reszta == 0:
            return True
        else:
            return False


