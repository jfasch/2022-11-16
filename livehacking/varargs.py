import sys

def f(*args, **kwargs):
    print('das ist eine superere print function')
    delay = kwargs.pop('delay')
    if delay is not None:
        print('... und ein delay hamma auch')
    print(*args, **kwargs)

f(1, 2, 3, 'abc', delay=100, file=sys.stderr, end='\ngruess gott\n\n\n')
