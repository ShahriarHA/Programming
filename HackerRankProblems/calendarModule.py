import calendar
inputDate = list(map(int,input().split(" ")))
mm,dd,yy = inputDate[0],inputDate[1],inputDate[2]
print(mm,dd,yy)
weekday = calendar.weekday(yy,mm,dd)
print(calendar.day_name[weekday].upper())
