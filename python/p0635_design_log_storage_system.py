class LogSystem:
    _prefix_lengths = {'Year': 4, 'Month': 7, 'Day': 10,
                       'Hour': 13, 'Minute': 16, 'Second': 19}

    def __init__(self):
        self._logs = []

    def put(self, id, timestamp):
        self._logs.append((id, timestamp))

    def retrieve(self, start, end, granularity):
        length = self._prefix_lengths[granularity]
        lower, upper = start[:length], end[:length]
        return [id for id, timestamp in self._logs
                if lower <= timestamp[:length] <= upper]
