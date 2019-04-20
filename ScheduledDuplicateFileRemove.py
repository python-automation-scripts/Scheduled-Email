import datetime;
from sys import *;
import ChecksumFunctionalityModule as module;
import time;
import schedule;
import datetime;
import EmailModule;
import os;

def CreateOutput(DirName,Output_File):
	List =  module.DeleteDuplicateFiles(DirName);
	
	if(List):
		data = "\n\n Files Deleted  At  :  " + str(datetime.datetime.now()) + "\n\n";
	
		for string in List:
			data += string;
			data += "\n";
		

		fd = open(Output_File,"a");
		fd.write(data);
		fd.close();


def sendmail(UserName,Password,To_FileName,Attachment):
	if(os.path.exists(To_FileName) and os.path.exists(Attachment)):
		EmailModule.sendmail(UserName,Password,To_FileName,Attachment);

def main():
	if  len(argv) != 5:
		print("Invalid number arguments");
		exit();

	if (argv[1] == "-h") or (argv[1] == "-H"):
		print("\n\n\t\t........................This is FileSystem Automation........................\n\n");
		print("\n " + argv[0]+ " -h For Help");
		print("\n " + argv[0]+ " -u For Usage");		
		exit();

	if (argv[1] == "-u") or (argv[1] == "-U"):
		print("\n <Usage> " + argv[0]+ " Directory_Name Username Password To_Filename");
		exit();

	try:
		DirName = argv[1];
		UserName = argv[2];
		Password = argv[3];
		To_FileName = argv[4];
		Output_File = "Files_Deleted.txt";

		schedule.every(1).hours.do( lambda : CreateOutput(DirName,Output_File));
		schedule.every().day.at("01:19").do( lambda : sendmail(UserName,Password,To_FileName,Output_File));
		
		while True:
			schedule.run_pending();
			time.sleep(1);

	except Exception as E:
		fd = open("Error_Log.txt",'a');
		logmsg = "\n\n Error :  "+ str(E) + "\n Log Time " + str(datetime.datetime.now()) +"\n\n";
		fd.write(logmsg);
		fd.close();

if(__name__ == "__main__"):
	main();