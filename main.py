from iterator import CountryIterator
from generator import MD5Generator

if __name__ == '__main__':
    countryURL = CountryIterator("countries.json", 'countries_url.json')
    countryURL.data_saver()
    countryURL.__next__()
    FILE = "countries.json"
    file = input('Введите путь и имя файла для генерации md5 hash (ппо умолчанию используется файл - country_links.json): ')
    file = file or FILE
    md5_generator = MD5Generator(file)
    hash_gen = md5_generator.md5_generator()
    while True:
        print(next(hash_gen))