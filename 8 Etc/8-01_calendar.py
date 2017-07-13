# Given a Calendar class (there are three fields, year, month, day) and a number of N, 
# Implement a function that returns the calendar after N days, 
# For example, if the input is {2017, 3,20} and 12, then the return is {2017,4, 1}

class Calendar(object):
	def __init__(self, year, month, day):
		self.year = year
		self.month = month
		self.day = day

	def m_days(self, year, month):
		mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		if month != 2:
			return mdays[month]
		else:
			if year % 4 == 0:
				return mdays[2]+1
			else:
				return mdays[2]

	def y_days(self, year):
		if year % 4 == 0:
			return 366
		else:
			return 365

	def date_to_days(self, year, month, day):
		days = 0
        for i in range(year):
            days += self.y_days(i)
		for i in range(1, month):
			days += self.m_days(year, i)
		days += day
		return days

	def days_to_date(self, days):
		year = 0
		while days > 0:
			days -= self.y_days(year)
			year += 1
		year -= 1
		days += self.y_days(year)

		month = 1
		while days > 0 and month <=12 :
			days -= self.m_days(year, month)
			month += 1

		if month == 12:
			return (year, month, days)
		else:
			month -= 1
			days += self.m_days(year, month)
			return (year, month, days)

	def add_days(self, date, n):
		date_days = self.date_to_days(*date)
		date_days += n
		return self.days_to_date(date_days)
	

if __name__ == '__main__':
	c = Calendar(2017, 3, 6)
	#days = c.date_to_days(2017,3,20)
	#print(days)
	#print(c.days_to_date(days))
	print(c.add_days((2017,3,20), 12))

	# print(c.days_to_date(367))



	
