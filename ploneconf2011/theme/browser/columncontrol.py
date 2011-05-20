# This code taken from Plone SunBurst Theme.  Thanks!

from zope.interface import implements
from zope.component import getMultiAdapter

from Acquisition import aq_inner
from Products.Five import BrowserView

from ploneconf2011.theme.browser.interfaces import IColumnControl

_marker = []


class ColumnControl(BrowserView):
    implements(IColumnControl)

    # Utility methods

    def getColumnsClass(self, view=None, column='blah'):
        """Determine whether a column should be shown. The left column is called
        plone.leftcolumn; the right column is called plone.rightcolumn.
        """
        context = aq_inner(self.context)
        plone_view = getMultiAdapter((context, self.request), name=u'plone')
        sl = plone_view.have_portlets('plone.leftcolumn', view=view);
        sr = plone_view.have_portlets('plone.rightcolumn', view=view);
        portal_state = getMultiAdapter((context, self.request), name=u'plone_portal_state')
        
        column_one_width = "grid_width_is_3"
        column_two_width = "grid_width_is_3"
        
        if column == 'content':
            if not sl and not sr:
                # we don't have columns, thus content takes the whole width
                return "cell width-full position_0 full-content"
            elif sl and sr and (portal_state.is_rtl()):
                # In case we have both columns, and are in RTL language
                return "cell grid_width_is_6 prefix_3 middle-content"
            elif sl and sr and (not portal_state.is_rtl()):
                # In case we have both columns, and are not in a RTL language
                return "cell grid_width_is_6 prefix_3 middle-content"
            elif (sr and not sl) and (portal_state.is_rtl()):
                # We have right column and we are in RTL language
                return "cell grid_width_is_9 position_0 left-content"
            elif (sr and not sl) and (not portal_state.is_rtl()):
                # We have right column and we are NOT in RTL language
                return "cell grid_width_is_9 position_0 left-content"
            elif (sl and not sr) and (portal_state.is_rtl()):
                # We have left column and we are in RTL language
                return "cell grid_width_is_9 prefix_3 right-content"
            elif (sl and not sr) and (not portal_state.is_rtl()):
                # We have left column and we are in NOT RTL language
                return "cell grid_width_is_9 prefix_3 right-content"
        elif column =='one':
            if not sl and not sr:
                # we don't have columns, thus content takes the whole width
                return "cell " + column_one_width
            elif sl and sr and (portal_state.is_rtl()):
                # In case we have both columns, and are in RTL language
                return "cell prefix_0 " + column_one_width
            elif sl and sr and (not portal_state.is_rtl()):
                # In case we have both columns, and are not in a RTL language
                return "cell prefix_0 " + column_one_width
            elif (sr and not sl) and (portal_state.is_rtl()):
                # We have right column and we are in RTL language
                return "cell " + column_one_width
            elif (sr and not sl) and (not portal_state.is_rtl()):
                # We have right column and we are NOT in RTL language
                return "cell " + column_one_width
            elif (sl and not sr) and (portal_state.is_rtl()):
                # We have left column and we are in RTL language
                return "cell position_0 " + column_one_width
            elif (sl and not sr) and (not portal_state.is_rtl()):
                # We have left column and we are in NOT RTL language
                return "cell prefix_0 " + column_one_width
        elif column =='two':
            if not sl and not sr:
                # we don't have columns, thus content takes the whole width
                return "cell " + column_two_width
            elif sl and sr and (portal_state.is_rtl()):
                # In case we have both columns, and are in RTL language
                return "cell position_0 " + column_two_width
            elif sl and sr and (not portal_state.is_rtl()):
                # In case we have both columns, and are not in a RTL language
                return "cell prefix_9 " + column_two_width
            elif (sr and not sl) and (portal_state.is_rtl()):
                # We have right column and we are in RTL language
                return "cell position_0 " + column_two_width
            elif (sr and not sl) and (not portal_state.is_rtl()):
                # We have right column and we are NOT in RTL language
                return "cell  prefix_9 " + column_two_width
            elif (sl and not sr) and (portal_state.is_rtl()):
                # We have left column and we are in RTL language
                return "cell " + column_two_width
            elif (sl and not sr) and (not portal_state.is_rtl()):
                # We have left column and we are in NOT RTL language
                return "cell" + column_two_width
        else:
            return "didntpasscolumn"