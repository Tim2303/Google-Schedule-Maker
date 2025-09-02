from datetime import datetime, timedelta

class Discipline:
    """
    Class for discipline storage
    """
    start_time: str = ""
    end_time: str = ""
    weeks = []
    name: str = ""
    address: str = ""
    teacher: str = ""
    day: int = 0 # 0 - sunday, 1 - monday, etc
    desc: str = ""

    def __init__(self, start_time, end_time, weeks, name, address, teacher, day, desc):
        self.start_time = start_time
        self.end_time = end_time
        self.weeks = weeks
        self.name = name
        self.address = address
        self.teacher = teacher
        self.day = day
        self.desc = desc


id_counter = 0
def parse_discipline(w_file, disp: Discipline):
    global id_counter

    for d_week in disp.weeks:
        w_file.write("BEGIN:VEVENT\n")
        w_file.write(f"UID:{id_counter}@default\n")
        id_counter += 1
        w_file.write("CLASS:PUBLIC\n")
        w_file.write(f"DESCRIPTION:{disp.desc}\\nГруппа: {disp.name}\\nПреподаватель: {disp.teacher}\n")

        # Time
        date = (datetime.fromisoformat('2025-09-01') +
                timedelta(weeks=d_week-1, days=int(disp.day)-1)).strftime("%Y%m%d")
        w_file.write(f"DTSTAMP;VALUE=DATE-TIME:20250902T141919\n")
        w_file.write(f"DTSTART;VALUE=DATE-TIME:{date}T{disp.start_time}\n")
        w_file.write(f"DTEND;VALUE=DATE-TIME:{date}T{disp.end_time}\n")

        w_file.write(f"LOCATION:{disp.address}\n")
        w_file.write(f"SUMMARY;LANGUAGE=en-us:{disp.name}\n")
        w_file.write("TRANSP:TRANSPARENT\n")
        w_file.write("END:VEVENT\n")

DisciplinesArr = [
    Discipline(
        start_time="113000", # 11:30::00
        end_time="130000",   # 13:00::00
        weeks=[1, 3, 6, 7],
        name="Уроки труда",
        address="ул.Пушкина, д.Колотушкина 69",
        teacher="Иванов Иван Иванович",
        day="6", # Saturday
        desc="Лекция, Аудитория 1404",
    )
]

# Main part
sch_file = open("schedule.ics", "w", encoding="utf-8")
sch_file.write("BEGIN:VCALENDAR\nPRODID:Calendar\nVERSION:2.0\n")
for d in DisciplinesArr:
    parse_discipline(sch_file, d)
sch_file.write("END:VCALENDAR")
sch_file.close()
