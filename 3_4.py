'''4. Соревнования по прыжкам в воду оценивают 7 судей. Каждый спортсмен выполняет 4 прыжка.
Каждый прыжок имеет одну из шести категорий сложности, оцениваемую коэффициентом (от 2,5 до 3,5).
Качество прыжка оценивается судьями по 6-балльной шкале. Далее лучшая и худшая оценки отбрасываются,
остальные складываются, и сумма умножается на коэффициент сложности.
Получить итоговую таблицу, содержащую фамилии спортсменов, и итоговую оцену
 (сумму оценок по 4 прыжкам) в порядке занятых мест.'''

class Dive:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.judge_scores = []

    def add_judge_scores(self, scores):
        self.judge_scores = scores

    def calculate_dive_score(self):
        sorted_scores = sorted(self.judge_scores)
        middle_scores = sorted_scores[1:-1]

        return sum(middle_scores) * self.difficulty

class Athlete:
    def __init__(self, surname):
        self.surname = surname
        self.dives = []

    def add_dive(self, dive):
        self.dives.append(dive)

    def total_score(self):
        return sum(dive.calculate_dive_score() for dive in self.dives)

class Competition:
    def __init__(self):
        self.athletes = []

    def add_athlete(self, athlete):

        self.athletes.append(athlete)

    def get_final_standings(self):
        return sorted(
            self.athletes,
            key=lambda x: x.total_score(),
            reverse=True
        )

    def print_results(self):

        print("Итоговая таблица результатов:")
        for place, athlete in enumerate(self.get_final_standings(), 1):
            print(f"{place} место: {athlete.surname} - {athlete.total_score():.2f} баллов")

def main():
    #Задаем соревнование, участников и их прыжки
    competition = Competition()


    athlete1 = Athlete("Иванов")

    dive1 = Dive(3.0)
    dive1.add_judge_scores([5.5, 5.0, 5.5, 5.5, 5.0, 5.5, 5.0])
    dive2 = Dive(2.8)
    dive2.add_judge_scores([5.0, 5.5, 5.0, 5.5, 5.5, 5.0, 5.5])
    dive3 = Dive(3.2)
    dive3.add_judge_scores([5.5, 5.5, 5.0, 5.5, 5.0, 5.5, 5.0])
    dive4 = Dive(2.9)
    dive4.add_judge_scores([5.0, 5.5, 5.5, 5.0, 5.5, 5.0, 5.5])

    athlete1.add_dive(dive1)
    athlete1.add_dive(dive2)
    athlete1.add_dive(dive3)
    athlete1.add_dive(dive4)
    competition.add_athlete(athlete1)

    athlete2 = Athlete("Петров")
    dive1 = Dive(3.1)
    dive1.add_judge_scores([5.5, 5.0, 5.5, 5.0, 5.5, 5.0, 5.5])
    dive2 = Dive(2.7)
    dive2.add_judge_scores([5.0, 5.5, 5.0, 5.5, 5.0, 5.5, 5.0])
    dive3 = Dive(3.3)
    dive3.add_judge_scores([5.5, 5.0, 5.5, 5.0, 5.5, 5.0, 5.5])
    dive4 = Dive(3.0)
    dive4.add_judge_scores([5.0, 5.5, 5.0, 5.5, 5.0, 5.5, 5.0])

    athlete2.add_dive(dive1)
    athlete2.add_dive(dive2)
    athlete2.add_dive(dive3)
    athlete2.add_dive(dive4)
    competition.add_athlete(athlete2)

    print("Подробные результаты:")
    for athlete in competition.athletes:
        print(f"{athlete.surname}: Итоговый балл = {athlete.total_score():.2f}")
    print()

    competition.print_results()

if __name__ == "__main__":
    main()