import boto, os, time

localPath = "/Users/lbot/Documents/Code/lee-port/www"
uploadFileNames = []

s3 = boto.connect_s3()

bucket = s3.create_bucket('skynet-demo-%s' % int(time.time()))

bucket.configure_website('index.html')

for dirName, subdirList, fileList in os.walk(localPath):
    #print('Found directory: %s' % dirName)
    for fname in fileList:
        #TODO: make this work for windows.
        uploadFileNames.append(dirName.replace(localPath,"")+"/"+fname)
 
for file in uploadFileNames:
    key = bucket.new_key(file)
    key.set_contents_from_filename(localPath+file)
    key.make_public()
    print "uploaded "+file
