import unittest

from zope.testing import doctestunit
from zope.component import testing
from Testing import ZopeTestCase as ztc

from Products.Five import zcml
from Products.Five import fiveconfigure
from Products.PloneTestCase import PloneTestCase as ptc
from Products.PloneTestCase.layer import PloneSite
ptc.setupPloneSite()

import ploneconf2011.theme

class TestCase(ptc.PloneTestCase):
    class layer(PloneSite):
        @classmethod
        def setUp(cls):
            fiveconfigure.debug_mode = True
            zcml.load_config('configure.zcml',
                             ploneconf2011.theme)
            fiveconfigure.debug_mode = False

        @classmethod
        def tearDown(cls):
            pass


def test_suite():
    return unittest.TestSuite([

        # Unit tests
        #doctestunit.DocFileSuite(
        #    'README.txt', package='ploneconf2011.theme',
        #    setUp=testing.setUp, tearDown=testing.tearDown),

        #doctestunit.DocTestSuite(
        #    module='ploneconf2011.theme.mymodule',
        #    setUp=testing.setUp, tearDown=testing.tearDown),


        # Integration tests that use PloneTestCase
        #ztc.ZopeDocFileSuite(
        #    'README.txt', package='ploneconf2011.theme',
        #    test_class=TestCase),

        #ztc.FunctionalDocFileSuite(
        #    'browser.txt', package='ploneconf2011.theme',
        #    test_class=TestCase),

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
