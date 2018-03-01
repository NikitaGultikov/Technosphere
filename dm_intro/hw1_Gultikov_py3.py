# № 2
import os
path = r'D:\10 semestr\Техносфера\Новая папка\мент.txt'

def print_file_tree(path, file_filter, s_start = '', s_plus = '   '):
    tree = os.listdir(path)
    roots = []
    print(s_start + os.path.basename(path) + ':')
    for i in tree:
        if os.path.isdir(path + "\\" + i):
            roots.append(path + "\\" + i)
        else:
            if i.rfind(file_filter + '.') != -1:
                print(s_start + s_plus + i)
    for i in roots:
        print_file_tree(i, file_filter, s_start = s_start + s_plus)
        
def file_tree(path, file_filter = None):
    s = ' '*4
    if os.path.isfile(path):
        if file_filter == None:
            print(os.path.basename(path))
        else:
            print_file_tree(os.path.dirname(path), file_filter)
    elif os.path.isdir(path):
        if file_filter == None:
            print('Такой путь к папке корректен. Введите "file_filter"!')
        else:
            print_file_tree(path, file_filter)
    else:
        print('Ваш путь к папке или к файлу введен некорректно')

file_tree(path, 'т')

# № 1
import csv
import random
import json

class SuperDict(dict):
    
    """
    
    Инициализация
    
    """
    
    def __init__(self, arg, field_names=['key', 'value']):
        
        if isinstance(arg, dict):
            for key in arg:
                self[key] = arg[key]
        elif isinstance(arg, str):
            if arg.endswith('.json'):
                with open(arg, 'r') as input:
                    data = json.load(input)
                    for key in data:
                        self[key] = data[key]
            elif arg.endswith('.csv'):
                with open(arg, newline='') as input:
                    reader = csv.DictReader(input)
                    for row in reader:
                        if len(row) > 2:
                            print('wrong .csv file!')
                        else:
                            self[row[field_names[0]]] = row[field_names[1]]


    def to_json(self, file_name='data.json'):
        with open(file_name, 'w') as File:
            json.dump(self, File)


    def to_csv(self, file_name='data.csv', field_names=['key', 'value']):
        with open(file_name, 'w') as File:
            writer = csv.DictWriter(File, delimiter=',', fieldnames=field_names)
            writer.writeheader()
            for key in self:
                writer.writerow({field_names[0]: key, field_names[1]: self[key]})
    
    """
    
    Переопределение методов: __getitem__, clear, items, keys, values, iteritems, iterkeys, itervalues, __iter__, __eq__, __len__
    
    """
    
    #def __init__(self, *args, **kwargs):      #удалить
        #dict.__init__(self, *args, **kwargs) 
    
    def __getitem__(self, var):
        return dict.__getitem__(self, var)
    
    def clear(self):
        return dict.clear(self)
    
    def items(self):
        return [(k, self.__getitem__(k)) for k in self]
    
    def keys(self):
        return [k for k in self]
    
    def values(self):
        return [self.__getitem__(k) for k in self]
    
    def iteritems(self):
        return super(SuperDict, self).items()

    def iterkeys(self):
        return super(SuperDict, self).keys()

    def itervalues(self):
        return super(SuperDict, self).values()
    
    def __len__(self):
        return dict.__len__(self)
    
    def __eq__(self, value):
        return dict.__eq__(self, value)
    
    def __iter__(self):
        return dict.__iter__(self)
        
    """
    
    Метод случайного поиска ключа: SuperDict.get_random_key()
    
    """
    
    def get_random_key(self):
        return self.keys()[random.randrange(len(self))]
    
    """
    
    Метод, возвращающий длину максимального ключа
    
    """
    
    def len_of_max_key(self):
        return len(max(self.keys()))
    
    """
    
    Метод, возвращающий ключи, которые начинаются с переданного аргумента: SuperDict.get_key_starts_from('abc')
    
    """
    
    def get_key_starts_from(self, begin):
        return [key for key in self.keys() if key.startswith(begin)]
    
    """
    
    Метод, позволяющий складывать словари: SuperDict('data.json') + SuperDict('new_data.json')
    
    """
    
    def __add__(self, other):
        x = dict(self)
        x.update(other)
        return x
      
    def __iadd__(self, other):
        x = dict(self)
        x.update(other)
        return x