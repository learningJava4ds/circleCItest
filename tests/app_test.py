from app import main

import pytest

# input("Number of times to run test: ")

def test_app_main(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x: "Mark")
    main()
    #assert input("aa") == "Mark"
    return

#app.main()

