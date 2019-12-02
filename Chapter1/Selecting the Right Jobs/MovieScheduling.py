from datetime import datetime

class Movie:

    def __init__(self, name, startDate, finishDate):
        self.name = name
        self.startDate = startDate
        self.finishDate = finishDate

class MovieScheduler:

    def __init__(self, movies):
        self.movies = list(movies)
        self.scheduledJobs = list()


    def OptimalScheduling(self):
        while(len(self.movies) != 0):
            """Accept the job "j" from "I" with the earliest completion date."""
            movie = self.GetJobEarliestCompletionDate()
            self.scheduledJobs.append(movie)
            """Delete j, and any interval which intersects j from I."""
            self.movies.remove(movie)

            intersectMovies = self.GetIntersectJobs(movie)
            if(len(intersectMovies) > 0):
                self.movies = [m for m in self.movies if m not in intersectMovies]
            return self.OptimalScheduling()

    def GetJobEarliestCompletionDate(self):
        sortedMovies = sorted(self.movies,key=lambda x: x.finishDate, reverse=False)
        movie = sortedMovies[0]
        return movie

    def GetIntersectJobs(self, movie):
        intersectMovies = list()
        for _movie in self.movies:
            if(_movie.startDate < movie.startDate < _movie.finishDate):
                # Add intersect movie which is _movie
                intersectMovies.append(_movie)
                continue
            elif(_movie.startDate < movie.finishDate < _movie.finishDate):
                # Add intersect movie which is _movie
                intersectMovies.append(_movie)
        return intersectMovies



if __name__ == '__main__':

    movies = [Movie("The President's Algorist", datetime(2019, 1, 5), datetime(2019, 2, 28)),
              Movie("Discrete Mathematics", datetime(2019, 1, 15), datetime(2019, 2, 10)),
              Movie("Tarjan of the Jungle", datetime(2019,1, 30), datetime(2019, 3, 20)),
              Movie("Halting State", datetime(2019, 2, 20), datetime(2019, 4, 10)),
              Movie("Steiner's Tree", datetime(2019, 3, 10), datetime(2019, 5, 8)),
              Movie("The Four Volume Problem", datetime(2019, 4, 20), datetime(2019, 8, 11)),
              Movie("Programming Challenges", datetime(2019, 6, 14), datetime(2019, 9, 1)),
              Movie("Process Terminated", datetime(2019, 7, 20), datetime(2019, 11, 10)),
              Movie("Calculated Bets", datetime(2019, 9, 29), datetime(2019, 12, 1))]

    movieScheduler = MovieScheduler(movies)
    movieScheduler.OptimalScheduling()
    for _x in movieScheduler.scheduledJobs:
        print("Job : " + _x.name)
