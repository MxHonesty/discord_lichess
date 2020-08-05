import lichess.api
import sys


def getBlitzRating(name):
    user = lichess.api.user(name)
    return(user['perfs']['blitz']['rating'])

def getClassicRating(name):
    user = lichess.api.user(name)
    return(user['perfs']['classical']['rating'])


if __name__ == '__main__':
    if(len(sys.argv) > 1 ):
        if(sys.argv[1] == "blitz"):
            try:
                print(sys.argv[2])
                print(getBlitzRating(sys.argv[2]))
            except:
                print("User not found")

        if(sys.argv[1] == "classic"):
            try:
                print(sys.argv[2])
                print(getClassicRating(sys.argv[2]))
            except:
                print("User not found")
