class Playlist:
    def __init__(self, name, tracks = []):
        self.name = name
        self.tracks = tracks

    def add(self, track):
        self.tracks.append(track)

    def count(self):
        return len(self.tracks)

    def show(self):
        return '플리명: ' +str(self.name)+', 곡 수: '+str(self.count())+', 곡들: '+str(self.tracks)
    
pl = Playlist('MyList')
pl.add('Dynamite')
pl.add('Butter')
print(pl.show())