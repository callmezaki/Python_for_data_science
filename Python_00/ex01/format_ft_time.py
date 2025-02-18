import time as t

# create function to print seconds with a space after every three digits

def print_seconds(seconds):
    seconds = str(seconds)
    if len(seconds) < 4:
        return seconds
    else:
        return print_seconds(seconds[:-3]) + "," + seconds[-3:]

print("seconds since January 1, 1970 are ", print_seconds(int(t.time())) , "or with scientific notaion:", "{:e}".format(t.time()))
print("current time:", t.ctime())
