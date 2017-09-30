# coding: utf-8
from datetime import date, timedelta
import os, sys
import random

def dategenerator(start, end):
    current = start

    if start > end:
        print("Please input a valid start-end date.")
        yield

    while current <= end:
        yield current
        current += timedelta(days=1)

if __name__ == '__main__':
    (start_date, end_date) = sys.argv[1:]

    (start_y, start_m, start_d) = start_date.split('-')
    (end_y, end_m, end_d)       = end_date.split('-')

    start = date(int(start_y), int(start_m), int(start_d))
    end   = date(int(end_y), int(end_m), int(end_d))

    for date in dategenerator(start, end):
	    number = random.randint(1, 10)
	    datestr = str(date)
	    for num in range(1, number):
	        f = open("cheat.txt", "w")
	        writenumber = random.uniform(0, 100)
	        f.write(str(writenumber))
	        f.close()
	        addfile = "git add cheat.txt"
	        commit  = "git commit --date=%s -m \"%s modify test\"" % (datestr, datestr)

	        os.system(addfile)
	        os.system(commit)

	    print(datestr + "committed " + str(number) + "time(s).")
