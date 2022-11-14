# CourseSearchAPI

Run main.py to start the program. Then go to http://localhost:5000/query in order to use the API, where "query" can be replaced by any arbitrary query, consisting of space-separated strings.

The search algorithm that I used essentially counts how many times each string in the query appears in the title and description of a course.
For a given query, a relevancy score is calculated for each course. When a string in the query appears in the title, it is weighted more towards
the relevancy score than when it appears in the description. Finally, the courses will be sorted by their relevancy score and returned to the user.
If a course has a relevancy score of 0, it will not be included in the returned result. For the special case where the query is itself a course code,
I simply return that course by itself.

The above algorithm is quite simple and therefore quick and easy to implement. I applied a greater weight to when a search string appears in the title 
because it typically indicates more direct relevancy. Another reason for the weight is that titles tend to be a lot shorter than descriptions, and therefore
I think it would make less sense if I simply count the number of occurence of the search string in the title and description and add them up.

However, there are also shortfalls to a simple algorithm. For instance, sometimes a search query will include strings that are highly related to
a particular course, but those strings do not show up directly in the title or description. In those cases, the API will not be able to detect those
relevant courses.
