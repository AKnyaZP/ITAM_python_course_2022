def hello(name, surname):
    return f'Доброго времени суток, {name} "Человек" {surname}!'

a = str(input())
a = a.split(' ')
name = a[0]
surname = a[1]
print (hello(name, surname))
