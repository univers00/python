def wsgi_handler(enviroment,response):
    print("*******")
    print(enviroment)
    print("*******")
    
    response("200",[])
    return [b"hello from wsgi"]
