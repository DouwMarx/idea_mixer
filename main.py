from flask import Flask
from flask import request, escape
import json
import random

# Created from tutorial on https://realpython.com/python-web-applications/

app = Flask(__name__)

def add_new_idea(idea):
    """
    Add a new idea to the knowledgebase .json

    :param idea:  A string of the idea
    :return:
    """

    # with open("knowledge_base.json", "r+") as file:
    #     data = json.load(file)
    #     newlist = data["generated_ideas"]
    #     newlist.append(idea)
    #     dict = {"generated_ideas": newlist}
    #
    #     data.update(dict)
    #     file.seek(0)
    #     json.dump(data, file)

    # Return idea as string to be displayed
    string = idea
    return string

def sample_from_concepts():
    """
    Randomly presents concepts to generate ideas from
    :return:
    """
    # with open("knowledge_base.json", "r+") as file:
    #     data = json.load(file)
    #     concepts = data["familiar_concepts"]
    concepts = ["heat transfer", "object orientated programming", "vibration", "cellular automata", "stepper motors", "inverse kinematics", "DADGAD guitar tuning", "CFD", "knife liner lock"]

    return random.sample(concepts, 3)


def concept_string_generator():
    
    """
     <ul>
      <li>Coffee</li>
      <li>Tea</li>
      <li>Milk</li>
    </ul>
    """

    concepts = sample_from_concepts()
    
    str = "<ul>"
    for c in concepts:
        str += "<li>"
        str += c
        str += "</li>"
    str +=  "</ul>"

    return str

@app.route("/")
def index():

    string = concept_string_generator()

    idea = str(request.args.get("idea", "")) # initally "" when first loading the page

    if idea: # Check if this is availbe in the dictionary of variables
        added_idea = add_new_idea(idea)
    else:
        added_idea = ''

    return (
        "Generate an idea that incorporates the following concepts:"
        + string
        + """<form action="" method="get"> 
                <input type="text" name="idea">
                <input type="submit" value="Add idea">
              </form>"""
        + "the idea entered was: "
        + added_idea
    )
# Action is where the data goes
# Method: HTTP get request that can be seen in the url
# Type: Text, could be drop down or check boxes as well
# Name is like te key to a dictionary


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
