def format_time(time):
        seconds = time // 1000 
        minutes = seconds // 60
        seconds -=  minutes * 60
        return "{0:02}:{1:02}".format(minutes, seconds)

print(format_time(150000))