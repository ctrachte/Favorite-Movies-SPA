import webbrowser
import time

break_count=0
breaks_needed=3

print ("Timer started on " + time.ctime())
while break_count<breaks_needed:
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=_4VCpTZye10")
	break_count+=1