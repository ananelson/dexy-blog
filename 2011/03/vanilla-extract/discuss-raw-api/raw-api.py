from StringIO import StringIO
import json
import pycurl
import urllib

USER_COOKIE = "1-1298749894%7Cc9..."

c = pycurl.Curl()
b = StringIO()
c.setopt(c.URL, "http://discuss.dexy.it/api/session")
c.setopt(c.COOKIE, "Vanilla=%s" % USER_COOKIE)
c.setopt(c.WRITEFUNCTION, b.write)
c.perform()

print b.getvalue()
session_info = json.loads(b.getvalue())

transient_key = session_info['user']['TransientKey']
print "transient key:", transient_key

discussion_data = [
  ("Discussion/Name", "test post"),
  ("Discussion/CategoryID", 1),
  ("Discussion/TransientKey", transient_key),
  ("Discussion/Body", """
 <p>Li Europan <span class="xx">lingues</span> es membres del sam familie.
   Lor separat existentie es un myth. Por scientie, musica, sport etc, litot
   Europa usa li sam vocabular. Li lingues differe solmen in li grammatica, li
   pronunciation e li plu commun vocabules.</p>

Omnicos directe al desirabilite de un nov lingua franca: On refusa continuar payar custosi traductores. At solmen va esser necessi far uniform grammatica, pronunciation e plu sommun paroles.

Ma quande lingues coalesce, li grammatica del resultant lingue es plu simplic e regulari quam ti del coalescent lingues. Li nov lingua franca va esser plu simplic e regulari quam li existent Europan lingues. It va esser tam simplic quam Occidental in fact, it va esser Occidental.
""")]

c = pycurl.Curl()
b = StringIO()
c.setopt(c.URL, "http://discuss.dexy.it/api/discussion/add")
c.setopt(c.COOKIE, "Vanilla=%s" % USER_COOKIE)
c.setopt(c.POST, 1)
c.setopt(c.POSTFIELDS, urllib.urlencode(discussion_data))
c.setopt(c.WRITEFUNCTION, b.write)
#c.setopt(c.VERBOSE, 1)
c.perform()

print "=================================================="
print b.getvalue()

