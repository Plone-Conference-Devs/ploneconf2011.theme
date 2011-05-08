This is the template overrides folder used by z3c.jbot

To use z3c.jbot, make sure it is in the list of eggs in base.cfg

To override a viewlet, e.g., the footer, add the template into this folder with this name:
    plone.app.layout.viewlets.footer.pt

Then restart the instance.  After that, any changes will show on page refresh.

**Keep this file here, having this directory empty can cause errors during release.
