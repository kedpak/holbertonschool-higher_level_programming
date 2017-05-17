# Synopsis
The test package doctest is a way of testing one's python code. This project will utilize doctest to test some python code

# Description
With this test, one can write tests within the docstring, which also can serve as documentation. The characters '>>>' begin the documentation, which is followed by a call, and then the results are displayed on the next line. 

# Examples 
'def test(text)
"""
>>> test('hey')
'Hey'
from string import capwords
return capwords(test)