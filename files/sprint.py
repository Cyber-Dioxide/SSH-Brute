import sys,time
from files import colors
c = colors
def sprint(str):
	for i in str +c.C + "\n":
		sys.stdout.write(i)
		sys.stdout.flush()

		time.sleep(3/90)


