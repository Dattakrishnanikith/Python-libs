Pk_movies = {'OG':'11:00am', 'Jalsa':'1:00pm', 'Panja': '3:00pm', 'AD':'6:00pm' , 'CMGR':'11:00am', 'GabbarSingh' : '11:30pm' }

print("We are showing the following PawanKalyan's movies:")

for key in Pk_movies:
    print(key)

movie = input('What movie would you like the showtime for?\n')

showtime = Pk_movies.get(movie)

if showtime == None:
    print("Requested movie isn't playing")

else:
    print(movie, 'is playing at' , showtime)

