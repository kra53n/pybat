class Commands(set):
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.hasattr = super(Commands, self).__new__(self)
        return self.hasattr

    def quit(self):
        self.add('quit')
