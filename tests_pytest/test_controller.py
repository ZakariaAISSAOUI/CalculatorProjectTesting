from calculate.controller import Controller


def test_run_addition(mocker):
    expected_value = 20.
    sut = Controller()

    # Mocking user input
    mocker.patch('calculate.view.View.get_user_input').side_effect = ["1", "10+10", "5"]

    # Mocking addition operation
    mocker.patch('calculate.operators.Operators.addition', return_value=expected_value)

    # Mocking continue_message() for cleanliness
    mocker.patch('calculate.view.View.continue_message')

    # Running the controller
    sut.run()

    # Assertions
    assert sut.result == expected_value


def test_run_subtraction(mocker):
    expected_value = 0.0
    sut = Controller()

    mocker.patch('calculate.view.View.get_user_input').side_effect = ["2", "10-10", "5"]
    mocker.patch('calculate.operators.Operators.subtraction', return_value=expected_value)
    mocker.patch('calculate.view.View.continue_message')

    sut.run()
    assert sut.result == expected_value


def test_run_multiplication(mocker):
    expected_value = 100.0
    sut = Controller()
    
    mocker.patch('calculate.view.View.get_user_input').side_effect = ["3", "10*10", "5"]
    mocker.patch('calculate.operators.Operators.multiplication', return_value=expected_value)
    mocker.patch('calculate.view.View.continue_message')

    sut.run()
    assert sut.result == expected_value


def test_run_division(mocker):
    expected_value = 1.0
    sut = Controller()

    mocker.patch('calculate.view.View.get_user_input').side_effect = ["4", "10/10", "5"]
    mocker.patch('calculate.operators.Operators.division', return_value=expected_value)
    mocker.patch('calculate.view.View.continue_message')

    sut.run()
    assert sut.result == expected_value
