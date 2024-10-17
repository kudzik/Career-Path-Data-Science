from datetime import datetime


birthday = datetime(1983, 2, 7, 0, 0, 0)
diff = datetime.today() - birthday


print(diff.days)
