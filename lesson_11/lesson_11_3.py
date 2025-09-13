# def add_str(*args):
#     print(type(args))
#     return "".join(args)
#
# res = add_str('1asdas', '2gtbyg', '3dsgfweg')
#
# print(type(res))
# print(res)

def add_str(f, *args, sep=' ', **kwargs):
    print(type(args))
    print(args)
    print(type(kwargs))
    print(kwargs)
    if kwargs.get('sep'):
        sep = kwargs['sep']
    res = sep.join(args)
    if kwargs.get('upper'):
        res = res.upper()
    return res


res = add_str('1asdas', '2gtbyg', '3dsgfweg', sep='-', upper=False, asfqe='dwqdq')
print(res)
