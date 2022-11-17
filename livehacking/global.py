x = 666

def f():
    global x
    x = 42
    print('local:', x)

f()

print('global:', x)
