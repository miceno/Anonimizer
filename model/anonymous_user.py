
class AnonymousUser:
    """Anonymous User of a domain"""
    
    def __init__( self, email, domain, **kwargs ):
        self.email = email
        self.id = kwargs.get( 'id', uuid.uuid1() )
    
    def generate_id( self ):
        self.id = uuid.uuid1()
        return self.id
        
        
