
class AnonymousUser:
    """Anonymous User of a domain"""
    
    def __init__( self, domain, **kwargs ):
        self.id = kwargs.get( 'id', uuid.uuid1() )
    
    def generate_id( self ):
        self.id = uuid.uuid1()
        return self.id
        
        
