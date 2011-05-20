from plone.theme.interfaces import IDefaultPloneLayer
from zope.interface import Interface

class IThemeSpecific(IDefaultPloneLayer):
    """Marker interface that defines a Zope 3 browser layer.
    """

class IColumnControl(Interface):
    """ """

    def getColumnsClass():
        """ Returns the CSS class based on columns presence. """
        
    def getColumnOneClass():
        """ Returns the CSS class based on columns presence. """
        
    def getColumnTwoClass():
        """ Returns the CSS class based on columns presence. """