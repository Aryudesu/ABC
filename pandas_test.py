import datetime as dt

date_str = "2024/08/21 1:00:00"
t_d = dt.datetime.strptime(date_str, "%Y/%m/%d %H:%M:%S")
print(t_d)
