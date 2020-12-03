

# under same folder 
# cap.py 
# test.py

# # cap.py
# def cap_test(text):
#     return text.capitalize()


# test.py
import unittest 
import cap

# inherit from unittest 
class TestCap(unittest.TestCase):
    
    def test_one_word(self):
        text = "python"
        # call cap_text(text ) from cap.py
        result = cap.cap_text(text)
        self.assertEqual(result, "Python")
        
    # def test_multi_words(self):
    #     text = "monty python"
    #     # call cap_text(text ) from cap.py
    #     result = cap.cap_text(text)
    #     self.assertEqual(result, "Monty Python")

# once execute, run unittest.main()
if __name__ == "__main__":
    unittest.main()



# EE
# ======================================================================
# ERROR: test_multi_words (__main__.TestCap)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "85_unittest_library.py", line 29, in test_multi_words
#     result = cap.cap_text(text)
# AttributeError: module 'cap' has no attribute 'cap_text'

# ======================================================================
# ERROR: test_one_word (__main__.TestCap)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "85_unittest_library.py", line 23, in test_one_word
#     result = cap.cap_text(text)
# AttributeError: module 'cap' has no attribute 'cap_text'

# ----------------------------------------------------------------------
# Ran 2 tests in 0.001s

# FAILED (errors=2)



