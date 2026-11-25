def check_alarm(value: float, limit: float) -> str:
    """alarming function that checks if the value exceeds the limit and returns an appropriate message."""
    if value >= limit :
        return "Alarm"
    return "Normal"



print (check_alarm(30,  28))
print (check_alarm(20,  28))

Pressure = 4.5
Pressure_limit = 4

print ("Pressure:", check_alarm(Pressure, Pressure_limit))
print ("Temperature:", check_alarm(23.5, 2.0))