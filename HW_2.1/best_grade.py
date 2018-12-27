current_max = 0
max_grade = None


with open("grades.txt", encoding="utf-8") as text:
    for line in text:
        grade = line
        marks = text.readline()
        marks = marks.split()
        # print(marks)
        int_marks = list()
        # for i in marks:
        #     int_marks.append(int(i))
        # есть и другая конструкция вместо цикла for: (ЭТО НУЖНО ЗАПОМНИТЬ!)
        int_marks = [int(i) for i in marks]
        avg_marks = sum(int_marks) / len(int_marks)
        if avg_marks > current_max:
            current_max = avg_marks
            max_grade = line.strip()
        # print("Название класса: {}".format(line))
        # print("средняя оценка {}".format(avg_marks))
        text.readline()

print("Наилучший класс {} со средней оценкой {}".format(max_grade, current_max))