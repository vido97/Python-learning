def add_new_movie_and_rating(dictionary, movie, rating):
    if movie not in dictionary:
        dictionary[movie] = rating
        return True
    else:
        return False
    pass

def change_rating(dictionary, movie, rating):
    if movie in dictionary:
        dictionary[movie] = rating
        return True
    else:
        return False
    pass


def print_all_movies(dictionary):
    movielist=dictionary.keys()
    movielist =sorted(movielist)

    for movie in movielist:
        print(f"{movie:s} {dictionary[movie]:d}")
    pass


def find_movies_with_rating(dictionary, rating):
    movielist = dictionary.keys()
    find = []
    for movie in movielist:
        if dictionary[movie] == rating:
            find.append(movie)
    return find
    pass

def ask_user_input():
    print("Choose 1-5.")
    print("1: Add a new movie and rating.")
    print("2: Change the rating of the movie.")
    print("3: Print all movies and their ratings.")
    print("4: Find all movies with a specific rating.")
    print("5: Exit.")
    user_input = int(input())

    return user_input


def main():
    print("Welcome to the database of the movie ratings.\n")
    dictionary = {}
    action = ask_user_input()
    while action != 5:
        if action == 1:
            print("")
            movie = input("Enter the movie.\n")
            rating = int(input("Enter the rating (4-10).\n"))
            new_movie=add_new_movie_and_rating(dictionary, movie, rating)
            if new_movie == True:
                print(f"{movie:s} has been added into the database.")
            else:
                print(f"{movie:s} is already in the database. Choose 2 if you want to change the rating of the movie.")

        elif action == 2:
            print("")
            movie = input("Enter the movie.\n")
            rating = int(input("Enter the new rating (4-10).\n"))
            change=change_rating(dictionary, movie, rating)
            if change == True:
                print(f"The rating of {movie:s} has been changed.")
            else:
                print(f"{movie:s} is not in the database. Choose 1 if you want to add the movie.")

        elif action == 3:
            print("")
            print("The movies in the database:")
            print_all_movies(dictionary)

        elif action == 4:
            print("")
            rating = int(input("Enter the rating.\n"))
            find=find_movies_with_rating(dictionary, rating)
            for movie in find:
                print(movie)
            if len(find) == 0:
                print(f"There are no movies with rating {rating:d} in the database.")

        else:
            print("")
            print("You chose an invalid number.")

        print("")
        action = ask_user_input()
main()