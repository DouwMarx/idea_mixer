import json

idea = "that"
with open("knowledge_base.json", "r+") as file:
    data = json.load(file)
    newlist = data["generated_ideas"]
    newlist.append(idea)
    print(newlist)
    dict = {"generated_ideas": newlist}

    data.update(dict)
    file.seek(0)
    json.dump(data, file)

    # Return idea as string to be displayed
    # string = idea
    # return newlist[-1]
