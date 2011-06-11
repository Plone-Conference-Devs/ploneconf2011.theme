import StringIO
import transaction

def setupVarious(context):

    if context.readDataFile('ploneconf2011.theme_default.txt') is None:
        return

    # set the default front page property of layout to be a new view
    site = context.getSite()
    front = site.get('front-page')
    if front:
        front.layout = 'home_page_view'
        
        # set the default content so that we can see what this will look like
        # but don't override if its already been set
        if front.getText().count("Make it your own"):
            front.setText("""<h2>Ah, San Francisco</h2>
It's time to start planning your pilgrimage to the annual Plone Conference in San Francisco. We're building an action-packed lineup of training, talks, and sprints for you and 400 of your closest friends. Reunite with old friends and finally put a face to that IRC handle this November. Registration opens soon!""")
            front.setDescription("")

    # set the initial images
    slide = site.get('slideshow-folder')
    if slide:
        
        # only add if this is a first time setup
        if not slide.getChildNodes():
            # XXX: this would be fun if it was reading a metadata file instead :)
            #       dreams for another day I guess...
            # I like your dreams ~S
            addMe = [
                        ("ss-sprint.jpg", "Contribute Back", "Sprint | November 7-8"), 
                        ("ss-conf.jpg", "Catch Up", "Conference | November 3-6"), 
                        ("ss-training.jpg", "Get Learned", "Training | November 1-2"), 
                    ]
            for (location, title, description) in addMe:
                
                imageId = location.split(".")[0]
                
                imageFile = context.openDataFile(location, 'images')
                if imageFile:   
                    transaction.begin() # in case this list gets huge
                    
                    slide.invokeFactory(id=imageId, type_name='Image')
                    newImage = slide.get(imageId)
                    newImage.setImage(imageFile.read())
                    imageFile.close()
                    
                    newImage.setTitle(title)
                    newImage.setDescription(description)
                    newImage.reindexObject() #required for title to persist
                    transaction.commit()
                    
                    
                


            