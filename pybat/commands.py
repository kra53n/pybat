class Commands(set):
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.hasattr = super(Commands, self).__new__(self)
        return self.hasattr

    def quit(self):
        self.add('quit')
    
    def start_playing(self):
        self.add('start_playing')
    
    def quit_play_menu(self):
        self.add('quit_play_menu')
