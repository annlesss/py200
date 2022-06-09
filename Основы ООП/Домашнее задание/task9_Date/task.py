class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        if not isinstance(day, int):
            raise TypeError
        if not isinstance(month, int):
            raise TypeError
        if not isinstance(year, int):
            raise TypeError

    def __repr__(self) -> str:
        return f"Date({self.day}, {self.month}, {self.year})"

    def __str__(self)-> str:
        return f"({self.day}, / , {self.month}, / , {self.year})"

    def linked_date(self)-> str:
        return self.day

if __name__ == "__main__":
    day = 13
    month = 11
    year = 2002
    liked_data = (day, month, year)
    print(Date)
