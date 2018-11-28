from datetime import datetime
s1 = '20:45:00'
s2 = '11:03:11' 
format = '%H:%M:%S'
time = datetime.strptime(s2, format) - datetime.strptime(s1, format)
print time
