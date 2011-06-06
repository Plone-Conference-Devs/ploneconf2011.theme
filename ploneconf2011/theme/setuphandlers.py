def setupVarious(context):

    # Ordinarily, GenericSetup handlers check for the existence of XML files.
    # Here, we are not parsing an XML file, but we use this text file as a
    # flag to check that we actually meant for this import step to be run.
    # The file is found in profiles/default.

    if context.readDataFile('ploneconf2011.theme_default.txt') is None:
        return

    # set the default front page property of layout to be a new view
    site = context.getSite()
    front = site.get('front-page')
    if front:
        front.layout = 'home_page_view'