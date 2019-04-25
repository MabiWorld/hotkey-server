import os
import cgi
from http.server import BaseHTTPRequestHandler, HTTPServer

working = os.path.join(os.path.dirname(os.path.abspath(__file__)), "hotkeys")
try: os.mkdir(working)
except: pass

class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		try:
			if self.path.startswith("/ui/"):
				hotkeyFile = self.path.split("/")[-1]
				print("Received hotkey request for %s" % hotkeyFile)
				f = open(os.path.join(working, hotkeyFile), "rb")

				self.send_response(200)
				self.send_header("Content-type", "text/xml")
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			#endif
			return
		except IOError:
			self.send_error(404, "0")
		#endtry
	#enddef

	def do_POST(self):
		ctype, pdict = cgi.parse_header(self.headers.get("Content-Type"))
		if ctype == "multipart/form-data":
			if self.path == "/UiUpload.asp":
				# gross
				pdict["boundary"] = pdict["boundary"].encode("ascii")
				pdict["CONTENT-LENGTH"] = self.headers.get("Content-Length")

				query = cgi.parse_multipart(self.rfile, pdict)
				print("Received hotkey upload for %s" % query["char_id"][0])
				f = open(os.path.join(working, query["char_id"][0] + ".xml"), "wb")
				f.write(query["ui"][0])
				f.close()
			#endif
			# Gives the same response for both avatarupload_2.asp and UiUpload.asp
			self.send_response(200)
			self.end_headers()
			self.wfile.write(b"1");
		#endif
	#enddef
#endclass

def main():
	try:
		server = HTTPServer(("mabiui.nexon.net", 80), MyHandler)
		print("Started local hotkey server...")
		server.serve_forever()
	except KeyboardInterrupt:
		print("Shutdown requested...")
		server.socket.close()
	#enddef
#endclass

if __name__ == "__main__": main()

