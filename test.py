from calculator import add

def test_add():
    #test case 1
    addition=add(-1,3)
    assert addition==2, "The test has passed"
#test case 2
    addition=add(0,0)
    assert addition==0, "The test has passed"
#test case 3
    addition=add(-3,3)
    assert addition==0, "The test has passed"
print("All the tests were succefully")