info = {'name':'Karan', 'age':19, 'eligible':True}
print(info)
info.update({'age':20})
info.update({'DOB':2001})
print(info)
# info.clear()
# info.pop('eligible')
# info.popitem()
del info['ag']
print(info)