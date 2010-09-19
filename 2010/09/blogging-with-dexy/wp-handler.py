### @export "imports"
import xmlrpclib
class WordPressHandler(DexyHandler):
    ALIASES = ['wp']

### @export "process-text"
    def process_text(self, input_text):
        f = open("wp-config.json", "r")
        wp_conf = json.load(f)
        f.close()

        expected_keys = ["pass", "user", "xmlrpc_url"]
        actual_keys = sorted(wp_conf.keys())
        if not (actual_keys == expected_keys):
            exception_msg = "expected to find wp-config.json file with keys %s, instead found %s"
            raise Exception(exception_msg % (expected_keys, actual_keys))
### @export "post-json"
        self.artifact.load_input_artifacts()
        matches = [k for k in self.artifact.input_artifacts_dict.keys() if k.endswith("post.json|dexy")]
        k = matches[0]
        # Read config from file        
        post_conf = json.loads(self.artifact.input_artifacts_dict[k]['data'])
        
### @export "connect"
        # Connect to server
        s = xmlrpclib.ServerProxy(wp_conf["xmlrpc_url"], verbose=False)

### @export "upload-media"
        def upload_files_to_wp(regexp, input_text):
            url_cache = {}

### @export "search-loop"
            for t in re.findall(regexp, input_text):
                if url_cache.has_key(t[1]):
                    url = url_cache[t[1]]
                    print "using cached url for", t[1], url
                else:

### @export "upload-media-file"
                    f = open(t[1], 'rb')
                    image_base_64 = xmlrpclib.Binary(f.read())
                    f.close()

### @export "mime-types"
                    mime_types = {
                        'png' : 'image/png',
                        'jpg' : 'image/jpeg',
                        'jpeg' : 'image/jpeg',
                        'aiff' : 'audio/x-aiff',
                        'wav' : 'audio/x-wav',
                        'wave' : 'audio/x-wav',
                        'mp3' : 'audio/mpeg'
                    }

### @export "upload-dict"
                    upload_file = {
                        'name' : t[1].split("/")[1],
                        'type' : mime_types[t[2]], # *should* raise error if not on whitelist
                        'bits' : image_base_64,
                        'overwrite' : 'true'
                    }

### @export "do-upload-media-file"
                    upload_result = s.wp.uploadFile(0, wp_conf["user"], wp_conf["pass"], upload_file)
                    url = upload_result['url']
                    url_cache[t[1]] = url
                    print "uploaded", t[1], "to", url

### @export "replace-url"
                replace_string = t[0].replace(t[1], url)
                input_text = input_text.replace(t[0], replace_string)
            return input_text

### @export "do-upload-media"
        input_text = upload_files_to_wp('(<img src="(artifacts/.+\.(\w{2,4}))")', input_text)
        input_text = upload_files_to_wp('(<embed src="(artifacts/.+\.(\w{2,4}))")', input_text)
        input_text = upload_files_to_wp('(<audio src="(artifacts/.+\.(\w{2,4}))")', input_text)

### @export "upload-post"
        content = { 'title' : post_conf['title'], 'description' : input_text}
        publish = post_conf['publish']
        if post_conf.has_key('post_id'):
            post_id = post_conf['post_id']
            s.metaWeblog.editPost(post_id, wp_conf["user"], wp_conf["pass"], content, publish)
        else:
            post_id = s.metaWeblog.newPost(0, wp_conf["user"], wp_conf["pass"], content, publish)
            # Save post_id in JSON file for next revision 
            post_conf['post_id'] = post_id
            json_file = re.sub('\|dexy$', "", k)
            f = open(json_file, 'w')
            json.dump(post_conf, f)
            f.close()
        return "post %s updated" % post_id

