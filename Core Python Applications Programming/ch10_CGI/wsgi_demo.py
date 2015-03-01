from cgi import parse_qs, escape

def hello_world(environ, start_response):
#    print 'environ=>',environ,'start_response=>',start_response
    
    parameters = parse_qs(environ.get('QUERY_STRING', ''))
    print 'parameters=>',parameters
    if 'subject' in parameters:
        subject = escape(parameters['subject'][0])
    else:
        subject = 'World'
    start_response('200 OK', [('Content-Type', 'text/html')])
    print 'subject is %(subject)s' %{'subject':subject}
    return ['''Hello %(subject)s    Hello %(subject)s!''' % {'subject': subject}]
 
if __name__ =='__main__':
 from wsgiref.simple_server import make_server
 srv=make_server('localhost',8000,hello_world)
 srv.serve_forever()
