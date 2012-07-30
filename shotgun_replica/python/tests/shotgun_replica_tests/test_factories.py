# -*- coding: utf-8 -*-

'''
Created on 21.05.2012

@author: bach
'''
import unittest
from shotgun_replica.factories import getObject
from shotgun_replica.entities import Task, Step, Project
from tests_elefant import testTaskID
from elefant.utilities.debug import debug

class Test(unittest.TestCase):

    def setUp(self):
        self.testtask = getObject(Task().getType(), testTaskID)
        pass

    def tearDown(self):
        pass

    def testObjectRetrieval(self):
        shotID = 1607
        shot = getObject("Shot", shotID)
        self.assertTrue(shot != None, "Shot %d does not exist?" % shotID)
        
        shotID = 1606
        shot = getObject("Shot", shotID)
        self.assertTrue(shot == None, "Shot %d does exist?" % shotID)

    def testLinkedFieldRetrieval(self):
        self.assertEqual(type(self.testtask.step), Step)

    def testDictGeneration(self):
        shotID = 1607
        shot = getObject("Shot", shotID)
        datadict = shot.getShotgunDict()
        
        self.assertTrue(datadict != None)
        self.assertEqual(datadict["code"], "ts020")

    def testAttributeRetrieval(self):
        shotID = 1607
        shot = getObject("Shot", shotID)
        self.assertEqual(type(shot.project), Project)
        self.assertEqual(type(shot.project), Project)
        
        tasks = shot.tasks
        self.assertTrue(len(tasks) > 0)
        self.assertEqual(type(tasks[0]), Task)
        
        self.assertFalse(shot == self.testtask)
        self.assertFalse(shot == "HANS")


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()