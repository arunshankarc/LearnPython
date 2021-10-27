# DON'T TOUCH THIS PLEASE!
people = ["Hanna","Louisa","Claudia", "Angela","Geoffrey", "aparna"]
# DON'T TOUCH THIS PLEASE!

#Change "Hanna" to "Hannah"
for pep in people:
    if pep == "Hanna":
        people[len(pep)] = 'h'
    elif pep == "Geoffrey":
        pep = "Jeffrey"
    elif pep == "aparna":
        pep[0] = 'A'
