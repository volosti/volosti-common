from volosti_common.person import queries, schemas


def test_account_change_schema() -> None:
    schema = schemas.AccountChange()
    data = {
        'username': 'username',
    }
    result = schema.typed_load_one(data)
    assert result == data


def test_password_change_schema() -> None:
    schema = schemas.PasswordChange()
    data = {
        'current_password': 'current_password',
        'new_password': 'new_password',
        'confirm_password': 'new_password',
    }
    result = schema.typed_load_one(data)
    assert result == data


def test_sign_in_schema() -> None:
    schema = schemas.SignIn()
    data = {
        'username': 'username',
        'password': 'password',
    }
    result = schema.typed_load_one(data)
    assert result == data


def test_sign_up_schema() -> None:
    schema = schemas.SignUp()
    data = {
        'username': 'username',
        'password': 'password',
        'confirm_password': 'password',
    }
    result = schema.typed_load_one(data)
    assert result == data
