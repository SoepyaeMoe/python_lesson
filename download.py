from urllib.request import urlretrieve;

urlName = input('url: ');
fileName = input('file name: ');

urlretrieve(urlName, 'image/'+fileName+'.jpg');