def status(housing_status):
    if housing_status == "BA":
        result = 0
    elif housing_status == "BB":
        result = 1
    elif housing_status == "BC":
        result = 2
    elif housing_status == "BD":
        result = 3
    elif housing_status == "BE":
        result = 4
    elif housing_status == "BF":
        result = 5
    elif housing_status == "BG":
        result = 6
    return result


def os_system(device_os):
    if device_os == "windows":
        result = 0
    elif device_os == "other":
        result = 1
    elif device_os == "linux":
        result = 2
    elif device_os == "macintosh":
        result = 3
    elif device_os == "x11":
        result = 4
    return result
