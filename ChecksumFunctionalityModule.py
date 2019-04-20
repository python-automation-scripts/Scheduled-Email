
import os;
import hashlib;


def hashfile(path,blocksize = 1024):
	fd = open(path,"rb");
	hasher = hashlib.md5();
	buf = fd.read(blocksize);

	while len(buf) > 0:
		hasher.update(buf);
		buf = fd.read(blocksize);

	fd.close();

	return hasher.hexdigest();

def GetChecksum(DirName):
	if(not os.path.isabs(DirName)):
		DirName = os.path.abspath(DirName);

	if(os.path.isdir(DirName)):
		
		duplicate = {};

		for folder, subfolder, files in os.walk(DirName):
			for file in files:
				DirName = os.path.join(folder,file);
				
				file_hash = hashfile(DirName);

				if(file_hash in duplicate):
					duplicate[file_hash].append(DirName);
				else:
					duplicate[file_hash] = [DirName];

	return duplicate;

def FileDuplicate(DirName):
	dictionary = GetChecksum(DirName);
	return GetDuplicate(dictionary);


def GetDuplicate(dictionary):	
	results = list(filter(lambda x: len(x) > 1,dictionary.values()));	
	List = list();
	
	fileCnt = 0;
	for result in results:
		for subresult in result:
			fileCnt +=1;
			if(fileCnt >= 2):
				List.append(subresult);
		fileCnt = 0;
	return List;


def DeleteDuplicateFiles(DirName):
	List = FileDuplicate(DirName);

	for file in List:
		os.remove(file);
	return List;



def ChkFileExists(filename,cnt = 0):	#checks if file exists and return the new file name for eg Demo_Copy.txt, Demo_Copy_1.txt	

	if(not os.path.exists(filename)):
		return filename;
	elif("_Copy" not in filename):	
		a = filename.split('.');
		newfilename = a[0] + "_Copy." + a[1]; 
		filename = newfilename;
	else:
		a = filename.split('_Copy');
		b = filename.split('.');
		newfilename = a[0] + "_Copy_" + str(cnt) +"."+ b[1];
		filename = newfilename;		
	cnt += 1;
	return ChkFileExists(filename,cnt);	