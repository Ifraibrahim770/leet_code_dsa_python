def test_back_recursion(n):
    def back_tracking(number):
        if number == 0:
            return
        print(number)
        back_tracking(number - 1)

    back_tracking(n)


test_back_recursion(10)
