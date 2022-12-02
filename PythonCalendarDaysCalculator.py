def is_year_leap(year):
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def days_in_month(year, month):
	if year < 1582 or month < 1 or month > 12:
		return None
	days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
	res  = days[month - 1]
	if month == 2 and is_year_leap(year):
		res = 29
	return res

def day_of_year(year, month, day):
    sumdays = day
    if is_year_leap(year):
        days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total_days = 366
    else:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        total_days = 365
    month_days = days[1:month]
    for i in month_days:
        sumdays += i
    return sumdays




print(day_of_year(2000, 12, 31))
