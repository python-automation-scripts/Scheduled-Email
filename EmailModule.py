import re;
import smtplib;
import urllib;
import os;
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

def is_connected():
	try:
		urllib.urlopen("http://216.58.192.142",timeout = 5);
		return True;
	except urllibURLError as err:
		return False;

def findemail(To_FileName):
	fd = open(To_FileName,"r");
	data = fd.read();
	fd.close();

	List = re.findall(r'\S+@\S+', data);
	return List;

def sendmail(UserName,Password,To_FileName,Attachment):
	
	if(os.path.exists(To_FileName) and os.path.exists(Attachment)):
		ToList = findemail(To_FileName);
		filename = Attachment;

		try:
			msg = MIMEMultipart();
			msg['Subject'] = "Duplicate File deletion report";
			
			attachment = open(filename, "rb");
			p = MIMEBase('application', 'octet-stream');
			p.set_payload((attachment).read());
			encoders.encode_base64(p); 
			p.add_header('Content-Disposition', "attachment; filename= %s" % filename);   
			msg.attach(p); 
			
			email_text = msg.as_string();

			server = smtplib.SMTP_SSL("smtp.gmail.com",465);
			server.ehlo();
			server.login(UserName,Password);
			server.sendmail(UserName,ToList,email_text);


		except Exception as E:
			print(E);




