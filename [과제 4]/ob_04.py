class Course:
    def __init__(self, name, scores=[]):
        self.name = name 
        self.scores = scores
        self.avge =0
    def add_score(self, s):
        self.scores.append(s)

    def avg(self):
        self.avge = sum(self.scores) /len(self.scores)
        return self.avge
    
    def info(self):
        self.avge = sum(self.scores) /len(self.scores)
        result = '과목:'+self.name+', 평균: '+str(self.avge)
        return result

c = Course('파이썬')
c.add_score(80)
c.add_score(90)
print(c.info())
