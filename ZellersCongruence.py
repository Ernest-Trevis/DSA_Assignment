class DateCalculator:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

        if self.month < 3:
         self.adjust_month = month + 12
         self.adjust_year = year - 1
        else:
         self.adjust_month = month
         self.adjust_year  = year


    def calculate_day(self):
        q = self.day
        m = self.adjust_month
        Y = self.adjust_year

        J = Y // 100
        K = Y % 100

        h = (q + ((13 * (m + 1)) // 5) + K + (K // 4) + (J // 4) + 5*J) % 7
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return days[h]

calculator = DateCalculator(1589, 9, 15)
day_of_the_week = calculator.calculate_day()
print(f"September 15, 1589 was a {day_of_the_week}")