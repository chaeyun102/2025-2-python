class Student:
  def __init__(self, name, score=0):
    self.name = name
    self.score = score
    self.score_list =[]


  def add_score(self,score):
    self.score = score
    self.score_list.append(score)
    print(f'{self.name}의 성적 {score}이 추가되었습니다.')

  def cal_avg(self):
      avg = sum(self.score_list)/len(self.score_list)
      return avg


student = Student('Kim')

student.add_score(90)
student.add_score(85)
student.add_score(78)

avg = student.cal_avg()
print(f'{student.name}의 평균 성적: {avg:.2f}')