from data_helpers import DataHelper

def get_text_data():
    endpoints = DataHelper.read_txt_file("endpoints.txt")

    responses = DataHelper.get_data(endpoints, "https://www.york.cuny.edu/++api++/")

    text_data = []
    for response in responses:
        all_values = DataHelper.find_values(response, 'description', 'plaintext', 'title')
        text_data.extend([text for text in all_values if DataHelper.is_valid_string(text)])

    filtered_data = [text for text in text_data if DataHelper.is_valid_string(text)]

    return filtered_data
