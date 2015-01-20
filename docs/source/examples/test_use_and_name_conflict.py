from pych.extern import Chapel
import os.path

currentloc = os.path.dirname(os.path.realpath(__file__))

@Chapel(depend=[currentloc + '/sfiles/chapel/'], sfile='user.chpl')
def useArbitrary():
    return None

@Chapel(sfile='nonuser.chpl')
def foo(x=int, y=int):
    return int

if __name__ == '__main__':
    useArbitrary()
    print (foo(1, 2)) # Should NOT be 6, should be 2
    # a function called foo from a different source file is used by useArbitrary
    # but that shouldn't interfere with the foo referenced here.

import testcase
# contains the general testing method, which allows us to gather output

def test_using_other_chapel_code():
    out = testcase.runpy(os.path.realpath(__file__))
    assert out.endswith('6\n14 14 3 14 14\n14 14 3 14 14\n(num = 4, contents = 3.0)\n(num = 4, contents = 3.0)\n2\n')
