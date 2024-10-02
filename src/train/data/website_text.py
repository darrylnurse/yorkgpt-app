from data_helpers import DataHelper

def get_text_data():
    endpoints = DataHelper.read_txt_file("endpoints.txt")

    responses = DataHelper.get_data(endpoints, "https://www.york.cuny.edu/++api++/")

    text_data = []
    for response in responses:
        desc = DataHelper.find_values(response, 'description', 'title')
        plaintext = DataHelper.find_values(response, 'plaintext', 'title')
        title = DataHelper.find_values(response, 'title', 'title')
        text_data.extend(desc)
        text_data.extend(plaintext)
        text_data.extend(title)

    return text_data