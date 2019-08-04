from sys import argv
script, user_name, movie_name = argv

print(f"My name is {user_name}, and the script name is {script}")
prompt="#"
print(f"I would like to ask you few questions")
print(f"Do you like me ?")
likes = input(prompt)
print(f"where do you live {user_name}")
lives = input(prompt)
print(f"what type of computer you are ?")
computer = input(prompt)
print(f"do you like the movie {movie_name}")
movie = input(prompt)
print(f""" 
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
reg the movie {movie_name} i {movie} it
"""
)