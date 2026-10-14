import http.server, functools, sys
DIR = r"C:\Users\Alfonso\Documents\claude code\acceler-portfolio"
Handler = functools.partial(http.server.SimpleHTTPRequestHandler, directory=DIR)
http.server.ThreadingHTTPServer.allow_reuse_address = True
http.server.ThreadingHTTPServer(("127.0.0.1", 8787), Handler).serve_forever()
