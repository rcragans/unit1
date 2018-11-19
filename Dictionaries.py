# greg = {"name": "Greg","gender": "Male", "Height": "Tall", "Job": "Developer"}

# zombie = {}
# zombie['weapon'] = 'fist'
# zombie['health'] = 100
# zombie['speed'] = 10

# print zombie

# for key,value in zombie.items():
#     print "Zombie has a key of %s with a value of %s." %(key,value)
    

# del zombie['weapon']
# print zombie

# is_nighttime = True
# if(is_nighttime):
#     zombie['health']+= 50

zombies = []
zombies.append({'name':'Hank','weapon': 'baseball bat','speed': 10})
zombies.append({'name':'Willy','weapon':'axe','speed':3, 'victims':['squirrel','rabbit','racoon']})

print zombies[0]['weapon']
print zombies[1]['victims'][1]
