class LeastSquaresFitting:
    @staticmethod
    def lsf(series: list[tuple[float, float]], round_by: int = 2) -> list[tuple[float, float]]:
        '''
        input: series (list of tuples (x, y) axis, being y the value to calculate on)

        Least Squares Fitting calculation: 
        A line equation y = mx + b
        m is the slope of the function, given by 
            m = (N * sum(xy) - sum(x)sum(y))/(N * sum(x^2) - sum(x)^2)
        b is the intercept, given by
            b = (sum(y) - m * sum(x))/N
        N is the number of data points
        '''
        if not series: return []

        sum_x, sum_y, sum_x_sq, sum_xy = map(sum, zip(*[(x, y, x*x, x*y) for x, y in series]))

        N = len(series)
        m = (N * sum_xy - sum_x * sum_y) / ((N * sum_x_sq) - sum_x ** 2)
        b = (sum_y - m * sum_x) / N

        return [(x, round(m*x + b, round_by)) for x, _ in series]
