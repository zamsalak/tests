import shelve


def open_file(file):
    try:
        with open(file, 'r', encoding='utf-8') as f:
            data = f.readlines()
            for each in data:
                yield each.strip()

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(e.args)
#-------------------------------------------------------
def parse(text):
    d = {}
    t = text.replace(' =>', ',')
    t = t.split(', ')
    d[t[0]] = t[1:]
    return d
#-------------------------------------------------------
def shelve_it(dic):
    try:
        with shelve.open('city', 'c') as sh:
            for i in dic:
                sh[i] = dic[i]

    except Exception as e:
        print(e)
#-------------------------------------------------------
def main():
    f = 'city-village.txt'
    for i in open_file(f):
        shelve_it(parse(i))
main()
