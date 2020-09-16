try:
    c = 5/0
except Exception as e:
    print('an error happened {}'.format(e))
except TypeError as e:
    print(e)
else:
    print("Every thing is fine")
finally:
    print("Finally run")


class ValueTooHighError(Exception):
    pass


def test_value(x):
    if(x > 100):
        raise ValueTooHighError('value is too high')


test_value(1001)
