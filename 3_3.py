'''На основании результатов соревнований по прыжкам в длину
(фамилии и результаты трех попыток) составить итоговый протокол
соревнований, считая, что в зачет идет лучший результат.'''
class Athlete:
    def __init__(self, surname):
        self.surname = surname
        self.jumps = []
    
    def add_jump(self, jump_length):
        self.jumps.append(jump_length)
    
    def get_best_jump(self):
        return max(self.jumps) if self.jumps else 0
    
    def __str__(self):
        return f"{self.surname}: {self.jumps} (Лучший: {self.get_best_jump()})"

class Competition:
    def __init__(self):
        self.athletes = []
    
    def add_athlete(self, athlete):
        self.athletes.append(athlete)
    
    def get_sorted_results(self):
        return sorted(
            self.athletes, 
            key=lambda x: x.get_best_jump(), 
            reverse=True
        )
    
    def print_protocol(self):
        print("Итоговый протокол соревнований:")
        for place, athlete in enumerate(self.get_sorted_results(), 1):
            print(f"{place} место: {athlete.surname} - {athlete.get_best_jump()} м")
#Здесь можно менять данные которые идут на вход об участниках
def main():
    competition = Competition()

    athlete1 = Athlete("Иванов")
    athlete1.add_jump(6.5)
    athlete1.add_jump(6.2)
    athlete1.add_jump(6.7)
    competition.add_athlete(athlete1)

    athlete2 = Athlete("Петров")
    athlete2.add_jump(6.3)
    athlete2.add_jump(6.8)
    athlete2.add_jump(6.4)
    competition.add_athlete(athlete2)

    athlete3 = Athlete("Смирнов")
    athlete3.add_jump(6.6)
    athlete3.add_jump(6.1)
    athlete3.add_jump(6.9)
    competition.add_athlete(athlete3)

    print("Результаты участников:")
    for athlete in competition.athletes:
        print(athlete)
    print()

    competition.print_protocol()

if __name__ == "__main__":
    main()