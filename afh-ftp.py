#!/usr/bin/env python3
from afh import AFH
import config, sys

if not len(sys.argv) == 3:
	exit("Usage: afh-ftp [folder-id] [file-name]")

folderId = sys.argv[1]
fileName = sys.argv[2]
fileSize = None

afh = AFH(config.cookie, config.uid, config.username)
fileList = afh.getFileListFTP()

for file in fileList['DATA']:
	if file[0] == fileName:
		fileSize = file[1]

if fileSize == None:
	exit("[ERROR] Unable to find the file!")

fileId = afh.getFileId(folderId, fileName)
importData = afh.importFileFTP(fileId['DATA']['fid'], fileName)
uploadData = afh.updateFile(fileId['DATA']['fid'], importData['DATA']['md5hash'], importData['DATA']['upload_date'], fileSize)

''' Cool debug stuff :3
print('fileList :', fileList)
print('fileId :', fileId)
print('importData :', importData)
print('uploadData :', uploadData)
'''

print('https://www.androidfilehost.com/?fid=' + fileId['DATA']['fid'])
