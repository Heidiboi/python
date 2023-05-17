import hashlib

def get_pw(pw):
    
    pw_to_bytes = bytes(pw, 'utf8')
    m = hashlib.sha256()
    m.update( pw_to_bytes )
    a=m.hexdigest() 
    return a
