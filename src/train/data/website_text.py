from data_helpers import DataHelper

def get_text_data():
    endpoints = DataHelper.read_txt_file("endpoints.txt")

    responses = DataHelper.get_data(endpoints, "https://www.york.cuny.edu/++api++/")

    text_data = []
    unique_text = set() 

    for response in responses:
        all_values = DataHelper.find_values(response, 'description', 'define_division', 'text')
        for text in all_values:
            if text not in unique_text and DataHelper.is_valid_text(text):
                unique_text.add(text)
                text_data.append({
                    'text': DataHelper.format_space(text),
                    #'context': str(response) # lets try changing it from json to maybe a paragraph of all string values in response
                })

    return text_data
