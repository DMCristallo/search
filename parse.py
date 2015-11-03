import datetime

def size(stat_result):
    size = stat_result[6]
    if size <= 10240:
        print "%s B" % size
    elif size <= 10240000:
        print "%s KB" % (size/1024)
    else: #size <= 10240000000:
        print "%s MB" % (size/1024000)

def time(time_field):
    pass
    print datetime.datetime.fromtimestamp(time_field)
