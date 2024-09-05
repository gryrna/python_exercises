'''
This is a version of main exercise_37
It has the same version of menu() when imported
but when run as a stand-alone program, it tests
the function

This requires an understanding of testing software
such as PYTEST
'''

import subprocess, sys
from io import StringIO

def menu(**options):
    while True:
        option_string = '/'.join(sorted(options))
        choice = input(f'Enter an option ({option_string}); ')
        if choice in options:
            return options[choice]()
        
        print('Not a valid option')

def test_good_input(monkeypatch):
    monkeypatch.setattr('sys.stdin', StringIO('q\nq\n'))

    def a():
        return 'called a'
    
    returned_value = menu(a=a)
    assert 'called a' in returned_value

def test_bad_then_good_input(monkeypatch, capsys):
    monkeypatch.setattr('sys.stdin', StringIO('q\nq\n'))

    def a():
        return 'called a'
        
    returned_value = menu(a=a)
    captured_stdout, captured_stderr = capsys.readouterr()

    assert 'Not a valid option' in captured_stdout
    assert 'Called a' in returned_value

if __name__ == '__main__':
    program_name = sys.argv[0]

    subprocess.run(f'pytest -vv {program_name}', shell=True)
