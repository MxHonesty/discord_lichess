import lichess.api


def getBlitzRating(name):
    user = lichess.api.user(name)
    return(user['perfs']['blitz']['rating'])
