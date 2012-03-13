### @export "source-env"
source ~/.wp-env.sh

### @export "wp-fcmd-help"
dexy fcmd -alias wp -cmd create_keyfile -help

### @export "apis-fcmd-help"
dexy fcmd -alias apis -cmd create_keyfile -help

### @export "call-wp-fcmd"
dexy fcmd -alias wp -cmd create_keyfile
ls -l .dexyapis

### @export "copy-actual-dexyapis-file"
mv ex1-dexyapis .dexyapis
mv ex1-dexy .dexy
mv ex1-index.html index.html
mv ex1-wordpress.json wordpress.json

### @export "fcmds"
dexy fcmds -alias wp

### @export "list-categories"
dexy fcmd -alias wp -cmd list_categories -help
dexy fcmd -alias wp -cmd list_categories

### @export "dexy-setup"
dexy setup

### @export "dexy"
dexy -loglevel DEBUG

### @export "cap1"
export POST_ID=`jazor wordpress.json postid`
export URL="http://dexydemo.wordpress.com/?p=$POST_ID&preview=true"
export LOGIN_URL="http://dexydemo.wordpress.com/wp-login.php"
screenshot -url $URL -filename dexy--screencap1.png -loginuser $WP_USERNAME -loginpass "$WP_PASSWORD" -loginurl $LOGIN_URL -scalew 600

### @export "publish"
python set-to-publish.py wordpress.json

### @export "dexy-to-publish"
dexy -loglevel DEBUG

### @export "cap2"
cat output-long/index.html-wp.txt
export URL="http://dexydemo.wordpress.com/?p=$POST_ID"
screenshot -url $URL -filename dexy--screencap2.png -scalew 600

### @export "new-example"
mv ex2-dexy .dexy
mv ex2-index.md index.md
mv ex2-example.py example.py
mv ex2-example.js example.js

### @export "change-title"
python change-title.py wordpress.json "My Fancier Blog Post"

### @export "dexy-new-example"
dexy -loglevel DEBUG

### @export "cap3"
screenshot -url $URL -filename dexy--screencap3.png -scalew 600
