# Error Handler for whi

class Error():
    '''
    Base class where errors originate from.
    '''
    pass

class NoPostsFound(Error):
    '''
    Raised when no posts are returned from a search result.
    '''
    pass

class NoCollectionsFound(Error):
    '''
    Raised when no collections are returned from a search result.
    '''
    pass

class ConnectionError(Error):
    '''
    Called when the client cannot connect to weheartit.com
    '''
    

