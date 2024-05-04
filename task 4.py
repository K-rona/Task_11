class Faculty:

    def __init__(self, name):
        self.__name = name
        self.departments = {}

        with open(f'{self.__name}.txt', 'r', encoding='utf8') as f:
            data = f.readlines()
        for line in data:
            department, groups = line.rstrip().split(':')
            new_department = Departments(department)
            if new_department not in self.departments:
                self.departments[new_department] = []
            for group in groups.split(','):
                new_group = Groups(group)
                self.departments[new_department] += [new_group]


class Departments:

    def __init__(self, name):
        self.name = name
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)

    def __repr__(self):
        return self.name


class Groups:

    def __init__(self, number):
        self.number = number
        self.schedule = {
            'Понедельник': [],
            'Вторник': [],
            'Среда': [],
            'Четверг': [],
            'Пятница': [],
            'Суббота': []
        }
        self.plan = self.semester_plan()
        self.fill_schedule()

    def semester_plan(self):
        schedule_lst = []
        try:
            with open(f'{self.number}_disciplines.txt', 'r', encoding='utf8') as f:
                data = f.readlines()
            for discipline in data:
                subject, pair_num = discipline.rstrip().split(":")
                schedule_lst += [[subject, int(pair_num)]]

        except FileNotFoundError:
            pass
        return schedule_lst

    def fill_schedule(self):
        plan = self.semester_plan().copy()
        while len(plan) > 0:
            for day in self.schedule.keys():
                for discipline in plan:
                    if discipline[0] not in self.schedule[day] and discipline[1] > 0 \
                            and len(self.schedule[day]) < 4:
                        self.schedule[day] += [discipline[0]]
                        discipline[1] -= 1
                    if discipline[1] == 0:
                        plan.remove(discipline)

    def look_schedule(self):
        for day in self.schedule.keys():
            print(f'{day}:')
            for subject in self.schedule[day]:
                print(subject)
            print()

    def __repr__(self):
        return self.number


Economics = Faculty('Faculty of Economics')
for department, groups in Economics.departments.items():
    for group in groups:
        if group.number == '22704.1':
            print(f'{department.name}, {group.number}:')
            group.look_schedule()

