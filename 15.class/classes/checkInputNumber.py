class CheckInputNumber:
    @staticmethod
    def is_integer(n):
        if isinstance(n, int):
            return True
        elif isinstance(n, float):
            return n.is_integer()
        else:
            return False

    @staticmethod
    def is_float(n):
        if isinstance(n, float):
            return True
        else:
            return False
