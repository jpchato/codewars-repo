'''
https://www.codewars.com/kata/568d0dd208ee69389d000016/train/python
After a hard quarter in the office you decide to get some rest on a vacation. So you will book a flight for you and your girlfriend and try to leave all the mess behind you.

You will need a rental car in order for you to get around in your vacation. The manager of the car rental makes you some good offers.

Every day you rent the car costs $40. If you rent the car for 7 or more days, you get $50 off your total. Alternatively, if you rent the car for 3 or more days, you get $20 off your total.

Write a code that gives out the total amount for different days(d).
'''
def rental_car_cost(d):
    total = d*40
    if d >= 3 and d < 7:
        total -= 20
    elif d >= 7:
        total -= 50
    print(total)
    return total

if __name__ == '__main__':
    rental_car_cost(1)
    rental_car_cost(4)
    rental_car_cost(7)
    rental_car_cost(8)
