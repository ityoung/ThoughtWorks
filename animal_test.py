# -*- coding:utf-8 -*- 
'''
Created on 2016-9-20
ThoughtWorks' homework: 2017-chengdu
== Unittest Part ==
@author: young
'''

import unittest
import animal

class TestDict(unittest.TestCase):
    def test_isDate(self):
        dtCorrect       = '2016/09/02 22:30:46'
        dtNoSpace       = '2016/09/0222:30:46'
        dtOverTimeRange = '2016/09/02 25:30:46'
        dt2BitYear      = '16/09/02 22:30:46'
        self.assertTrue(animal.isDate(dtCorrect))
        self.assertFalse(animal.isDate(dtNoSpace))
        self.assertFalse(animal.isDate(dtOverTimeRange))
        self.assertFalse(animal.isDate(dt2BitYear))

    def test_isID(self):
        idCorrect   = '351055db-33e6-4f9b-bfe1-16f1ac446ac1'
        idWithSpace = '351055db 33e6 4f9b bfe1 16f1ac446ac1'
        self.assertTrue(animal.isID(idCorrect))
        self.assertFalse(animal.isID(idWithSpace))
        
    def test_isAnimal(self):
        animalCorrectNew = 'cat1 10 9'
        animalCorrectOld = 'cat1 10 9 2 -1'
        animalNoDigitPos = 'cat1 10 9 2 -'
        animal3DigitPos  = 'cat1 10 9 2'
        animal5DigitPos  = 'cat1 10 9 2 -1 6'
        self.assertTrue(animal.isAnimal(animalCorrectNew))
        self.assertTrue(animal.isAnimal(animalCorrectOld))
        self.assertFalse(animal.isAnimal(animalNoDigitPos))
        self.assertFalse(animal.isAnimal(animal3DigitPos))
        self.assertFalse(animal.isAnimal(animal5DigitPos))

    def test_isAnimalDataRight(self):
        newAnimalCorrect  = 'cat1 10 9'
        oldAnimalCorrect1 = 'cat1 10 9 2 -1'
        oldAnimalCorrect2 = 'cat1 12 8 3 4'
        oldAnimalFalse    = 'cat1 11 8 3 4'
        newAnimalFalse    = 'cat2 11 8 3 4'
        self.assertTrue(animal.isAnimalDataRight(newAnimalCorrect))
        self.assertTrue(animal.isAnimalDataRight(oldAnimalCorrect1))
        self.assertTrue(animal.isAnimalDataRight(oldAnimalCorrect2))
        self.assertFalse(animal.isAnimalDataRight(oldAnimalFalse))
        self.assertFalse(animal.isAnimalDataRight(newAnimalFalse))

    def test_delFalseAnimal(self):
        animal.animalDict = {'cat2': [2, 3, True], 'cat1': [10, 9, False]}
        animal.animalDict = animal.delFalseAnimal(animal.animalDict)
        self.assertIn('cat2', animal.animalDict)
        self.assertNotIn('cat1', animal.animalDict)
        
    def test_isDateOrderRight(self):
        timeS = '2016/09/02 22:30:46'
        timeM = '2016/09/02 22:30:52'
        self.assertTrue(animal.isDateOrderRight(timeS))
        self.assertTrue(animal.isDateOrderRight(timeM))
        self.assertFalse(animal.isDateOrderRight(timeS))

if __name__ == '__main__':
    unittest.main()
