rabbit_pop = 190
year = 0
print('In year ' + str(year) + ' the rabbit population is: ' + \
      str(rabbit_pop) + '.')
while year < 10:
    year += 1
    if rabbit_pop > 150:
        rabbit_pop -= 100
    rabbit_pop *= 2
    print('In year ' + str(year) + ' the rabbit population is: ' + \
          str(rabbit_pop) + '.')

    
