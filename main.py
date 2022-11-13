from flask import Flask
import json

f = open("backend-course-data.json")
data = json.load(f)

app = Flask(__name__)
@app.route('/<string:searchString>/')
def hello(searchString):
    searchStrings = searchString.split(" ")
    results = []
    for course in data:
        if searchString == course["course_code"]:
            return course

        relevancy = 0
        for str in searchStrings:
            if course["title"]:
                relevancy += 5 * course["title"].lower().count(str.lower())

            if course["description"]:
                relevancy += course["description"].lower().count(str.lower())

        if relevancy > 0:
            results.append([course, relevancy])

    results = sorted(results, key=lambda x:x[1], reverse=True)
    return results
app.run()
