<<<<<<< HEAD
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
    Raised when the client cannot connect to weheartit.com
    '''
    pass

class NoUsersFound(Error):
    '''
    Raised when a search result returns no users.
    '''
    pass
    

=======
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
    

>>>>>>> 6d9e8c9dcc13547be1aca742ffbdb8e9f800a414
