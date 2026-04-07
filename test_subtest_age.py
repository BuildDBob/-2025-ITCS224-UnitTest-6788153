import unittest  
from age import categorize_by_age 

class TestIsEven(unittest.TestCase): 

    def test_is_adolescent(self): 
        for number in [10, 11, 12, 13, 14, 15, 16, 17, 18]: 
            with self.subTest(number=number): 
                self.assertEqual(categorize_by_age(number), "Adolescent")
                print(f"\n{number} is considered as an Adolescent.")
 

if __name__ == "__main__": 

    unittest.main(verbosity=2) 