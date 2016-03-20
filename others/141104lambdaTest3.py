def action(x):
    return lambda y:y+x
act=action(2)
print act
print act(4)
