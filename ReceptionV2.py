import socket
import os
from fonctionPratiques import *
import sys
from time import time
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip=input('IP:')
print('PORT :')
port=int(input())
client.connect((ip,port))
print('connecte')
recu=client.recv(1024).decode()
fichier=bytes()
if(recu=="N"):
	print("[*]Annule par le serveur")

else:
	taille,ext=recu.split(',')
	taille=int(taille)
	tailleRecu=0
	print("La taille du fichier {} a recevoir est de {} octets\nConfirmer?(o/N)".format(ext,taille))
	reponse=input()
	client.send(reponse.encode())
	stop=False
	if(reponse.upper()=='O'):
		print('[*]En cours de reception...')
		debut=time()
		while(not(stop)):
		
			recu=client.recv(1024*256)
			tailleRecu=sys.getsizeof(fichier)
			if(recu==b'stop' or recu==b''):
				fichier+=recu
				stop=True
				break
			fichier+=recu
			print('\r{}/{}'.format(tailleRecu,taille),end='')
		print('[*]Fin de la reception!')
		print('vitesse: {} kB/s'.format(((time()-debut)/taille)/1024))
		print(recu)
		print(tailleRecu,'/',taille)

print("[*]Termine")
print("Afficher le contenu en texte?(illisible)(o/N)")

if(Rep1_0()==True):
	print(fichier)

else:
	print("[*]Affichage de la reception annule")

print("Enregistrer le fichier recu?")

if(Rep1_0()==True):
	print("Entrez le chemin jusqu'au fichier a envoyer au client(# si dossier actuel)")
	chemin=input()
	if (not(chemin=="#")):
		os.chdir(chemin)
	print("Entrez le nom du fichier sans l'extension")
	nomFichier=input()+ext

	with open(nomFichier,"wb") as file:
		file.write(fichier)
		print("[*]Enregistrement termine")

client.close()
