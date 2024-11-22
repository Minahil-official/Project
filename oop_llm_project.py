class student:
    def __init__(self,name):
        self.name = name
        self.score = {}
    def add_score(self,subject,score):
        self.score[subject] = score
        
    def calculate_average(self):
        return sum(self.score.values())/len(self.score)
        
    def is_passing(self):
        for sub,num in self.score.items():
            if num <40:
                return (f'fail in {sub}')
            return 'pass'
        
class Performance_tracker:
    def __init__(self):
        self.student = {}
        
    def add_student(self,name):
        if not name.isalpha():
            raise ValueError("please enter valid name")
        self.student[name] = student(name)
        
    def calculate_class_average(self):
        total = 0
        for x in self.student.values():
            total += x.calculate_average()
            return total/len(self.student.values())
        
    def display_student_performance(self):
        for x,y in self.student.items():
            average = y.calculate_average()
            status = y.is_passing()
            print(f"student: {x} average: {average} and pass_fail status: {status}")
            
performace = Performance_tracker()
while True:
    name = input("enter student name or type exit to finish:")
    if name.lower() == "exit":
        break
    try:
        performace.add_student(name)
        for x in ['eng','math','urdu']:
            while True:
                try:
                    score= float(input("enter student score for{x} 0 to 100:"))
                    if 0<= score <=100:
                        performace.student[name].add_score(x,score)
                        break
                    else:
                        print("please enter valid input")
                except ValueError as e:
                    print(e)
    except Exception as e:
        print(e)
        
performace.display_student_performance()
print(f"This is class average {performace.calculate_class_average()}")