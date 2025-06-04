from greetings.hello import get_greeting

def test_get_greeting():
    assert get_greeting("World") == "Hello World!"
    assert get_greeting("Alice") == "Hello Alice!"
    assert get_greeting("") == "Hello !"
    assert get_greeting() == "Hello !"
    assert get_greeting("Max", "Moriz") == "Hello Max and Moriz!"
