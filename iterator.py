import json

class CountryIterator:

    def __init__(self, json_file, out_file):
        self.counter = 1
        self.json_file = json_file
        self.out_file = out_file

    def data_saver(self):
        with open(self.json_file, encoding='utf-8') as f:
            data = json.load(f)
            country_list = [country['name']['common'] for country in data]
        return country_list

    def __iter__(self):
        pass
        return self

    def __next__(self):
        country_list = self.data_saver()
        wiki_list = [f'https://ru.wikipedia.org/wiki/{country}' for country in country_list]

        country_url = {}
        for number in range(len(country_list)):
            country_url[country_list[number]] = wiki_list[number]

        with open(self.out_file, 'w', encoding='utf-8') as f:
            json.dump(country_url, f, ensure_ascii=False, indent=4)
        print('Список стран со ссылками сохранен в файл:', self.out_file)

        self.counter += 1
        if self.counter == len(country_list):
            raise StopIteration

        return wiki_list
