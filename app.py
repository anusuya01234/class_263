from flask import Flask, render_template, request #From the flask library we are importing some functions such as Flask, render_template, and request.

app = Flask(__name__) # initializing Flask using the Flask function. __name__ is to define how you want to run your program.
#  @app. route is a decorator which is directing our web page to perform a function.
@app.route("/")
def visitors(): #visitors() function will keep a track of visitors who visited the website,

    # Load current count
    counter_read_file = open("count.txt", "r") #open the file in read mode
    visitors_count = int(counter_read_file.read())
    counter_read_file.close() #close() function to close the file

    # Increment the count
    visitors_count = visitors_count + 1

    # Overwrite the count
    counter_write_file = open("count.txt", "w")
    counter_write_file.write(str(visitors_count))
    counter_write_file.close()

    # Render HTML with count variable.convert console based output into a GUI based output that will come on the HTML page using flask’s render_template() method.
    return render_template("index.html", count=visitors_count) #Here count is the attribute name which we have mentioned in the p tag of the HTML file.
# define one more decorator using @app.route(‘/’) because we need to run another function on the index.html file. 
@app.route('/', methods=['POST']) #passed the method parameter from which we need to get the user input. so use the HTTP method as POST
def covid_stats():
    # Load current count
    counter_read_file = open("count.txt", "r")
    visitors_count = int(counter_read_file.read())
    counter_read_file.close()

    text = request.form['text'] #requesting text from the HTML page for the country name.in the input field we had added the name as ‘text’. Hence, we need to mention the same name then only we can refer to that input field and get the user entered value.
#appending country code(which is entered by the user and stored in a text variable) to the API URL.
    corona_data = 'https://covidstats-sdbd.onrender.com/?country='+text
    print(corona_data) # print the link of the covid stats image.
    return render_template("index.html", image=corona_data, count=visitors_count) #return corona_data as image and visitors count data at HTML page
#check if still, we are under flask code. if the condition satisfies then we will run our flask application by using run() function.This will result in running URL 127.0.0.1:5000.
if __name__ == "__main__":
    app.run()
