class TraceMemory:
    def __init__(self, short_term_size=100, long_term_size=1000):
        self.short_term = []
        self.long_term = []
        self.short_term_size = short_term_size
        self.long_term_size = long_term_size

    def store(self, trace):
        self.short_term.append(trace)
        if len(self.short_term) > self.short_term_size:
            self.short_term.pop(0)

    def consolidate(self):
        if len(self.long_term) < self.long_term_size:
            self.long_term.extend(self.short_term)
        else:
            self.long_term = self.long_term[len(self.short_term):] + self.short_term
        self.short_term = []

    def get_recent(self, n=10):
        return self.short_term[-n:]

    def get_long_term(self):
        return self.long_term