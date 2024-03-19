def calculate_health(health, damage, armor):
    health = armor * damage - health
    print(health)
    return health

calculate_health(100, 10, .5)

def average_of_five(one,two,three,four,five):
    five = one+two+three+four+five/5
    print(five)
    
average_of_five(10,20,30,40,50)
