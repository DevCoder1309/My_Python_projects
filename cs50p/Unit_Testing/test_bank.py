import bank


def main():
    test_value()


def test_value():
    assert bank.value("hello") == int('0')
    assert bank.value("HELLO") == int('0')
    assert bank.value("hey there") == int('20')
    assert bank.value("wahts up") == int('100')


if __name__ == "__main__":
    main()
