with open('file.xml', 'r', encoding='UTF-8') as file:
    strings = file.readlines()

    count = 0

    for string in strings:
        if 'http' in string:
            links_end = 0
            while string.find('http', links_end) != -1:
                links_start = string.find('http', links_end)
                if string[links_start - 1] == '"':
                    links_end = string.find('"', links_start)
                elif string[links_start - 1] == ' ':
                    links_end = string.find(' ', links_start)
                else:
                    links_end = string.rfind('<')
                count += 1
                print(string[links_start:links_end])
    print("Всего ссылок:", count)