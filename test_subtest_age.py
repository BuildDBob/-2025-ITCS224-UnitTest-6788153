import unittest  
from age import categorize_by_age 

class TestIsEven(unittest.TestCase): 

    def test_is_child(self): 
        for number in [0,1,2,3,4,5,6,7,8,9]: 
            with self.subTest(number=number): 
                self.assertEqual(categorize_by_age(number), "Child")
                print(f"\n{number} is considered as a Child.")

    def test_is_adolescent(self): 
        for number in [10, 11, 12, 13, 14, 15, 16, 17, 18]: 
            with self.subTest(number=number): 
                self.assertEqual(categorize_by_age(number), "Adolescent")
                print(f"\n{number} is considered as an Adolescent.")

    def test_is_adult(self):
        for number in range(19, 66): 
            with self.subTest(number=number): 
                self.assertEqual(categorize_by_age(number), "Adult")
                print(f"\n{number} is considered as an Adult.")

if __name__ == "__main__": 

    unittest.main(verbosity=2) 