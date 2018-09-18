import shelve
import sys


class Loadshelf:
    def __init__(self, dat_file):
        try:
            self.load = shelve.open(dat_file, 'w')

        except Exception as e:
            print(e)
    # -------------------------------------------------------
    def list_cities(self):
        print('Şehirler')
        print('-----'*3)
        for i, city in enumerate(self.load):
            print(str(i+1)+'.', city)
    # -------------------------------------------------------
    def list_cities_villages(self):
        for i in self.load:
            print('{} - {}'.format(i, ', '.join(self.load[i])))
    # -------------------------------------------------------
    def search_city(self, city):
        try:
            print('{} - {}'.format(city, ', '.join(self.load[city])))

        except Exception:
            print('No such city')
    # -------------------------------------------------------
    def new_city(self, city, *villages):
        if city in self.load:
            print('This city exists in the shelf')
        else:
            self.load[city] = list(villages)

    def delete_city(self, city):
        if not city in self.load:
            print('City doesn\'t exist')
        else:
            del self.load[city]
            print(city, 'deleted!')
    # -------------------------------------------------------
    def exit(self):
        self.load.close()
        sys.exit()
# -------------------------------------------------------
def main():
    x = Loadshelf('city')
    func_dict = {1: x.list_cities, 2: x.list_cities_villages, 3: x.search_city, 4: x.new_city,
                 5: x.exit, 6: x.delete_city}

    while True:
        print('-' * 50)
        print("1) Şehirleri Listele\n2) Şehirleri ve İlçelerini Listele\n3) Şehir Ara\n4) Şehir Ekle\n5) Çıkış\n6) Şehir Sil\n")

        try:
            selection = int(input())
            if not 0 < selection < 7:
                raise ValueError

        except ValueError:
            print('Invalid input')

        except Exception as e:
            print(e.args)

        else:
            if selection == 1 or selection == 2 or selection == 5:
                print('-' * 50)
                func_dict[selection]()

            elif selection == 3:
                city = str(input('Search city: '))
                func_dict[selection](city)

            elif selection == 6:
                city = str(input('Delete city: '))
                func_dict[selection](city)
            else:
                city = input('New city: ')
                villages = input('Villages(Seperate with coma): ')
                func_dict[selection](city, villages)


if __name__ == '__main__':
    main()