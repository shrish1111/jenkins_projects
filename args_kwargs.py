def multiple_args(*args,**kwargs):
    if 'fruit' and 'veg' in kwargs:
        print(f"i like {' and '.join(args)} in breakfast")
        print(f"my fav fruit is {kwargs['fruit']} and my fav veg is {kwargs['veg']}")
multiple_args('milk','chocos',fruit='apple',veg='ladyfinger')
