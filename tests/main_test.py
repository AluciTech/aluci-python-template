import pytest
from main import run


def test_main_prints_hello(capsys):
    """main() should print 'Hello, World!' followed by a newline."""
    # Call the function under test
    run()
    # Capture stdout/stderr
    captured = capsys.readouterr()
    # Assert the output is exactly what we expect
    assert captured.out == "Hello, World!\n"
    assert captured.err == ""
