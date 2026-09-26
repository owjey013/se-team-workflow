def login(username, password):
    if not username or not password:
        raise ValueError("Username and password required")
    print("Authenticated")
    return True