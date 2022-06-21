import requests
import json

from Tkinter import *

window = Tk()

# Window Config
window.title("COVID19 Info")
window.geometry("400x100")


def get_country_info():
    url = "https://api.covid19api.com/summary"
    response = requests.request("GET", url)

    # Get Data from API and store in json
    data = json.loads(response.text)

    # Get Index for Country
    searchcountry = txt.get()

    def get_country_index(country):
        for index, item in enumerate(data["Countries"]):
            if item["Country"] == country:
                return index

    countryid = get_country_index(searchcountry)

    # Get New New Confirmed & Total Confirmed
    newconfirmed = data["Countries"][countryid]["NewConfirmed"]
    totalconfirmed = data["Countries"][countryid]["TotalConfirmed"]

    covid_msg = f"Last number of new confirmed cases in {searchcountry}: {newconfirmed}.\nThe total cases are: {totalconfirmed}"

    # Return covid msg to gui
    output_text.set(covid_msg)


# Create Label
lbl = Label(window, text="Enter Country:")
lbl.grid(column=0, row=0, sticky=E)

# Create Entry Field
txt = Entry(window, width=30)
txt.grid(column=1, row=0, sticky=W)

# Create Button
btn = Button(window, text="Get Information", command=get_country_info)
btn.grid(column=2, row=0, sticky=W)

# Display Output
output_text = StringVar()
lbl_output = Label(window, textvariable=output_text)
lbl_output.grid(column=0, columnspan=2, row=1, sticky=W)

window.mainloop()