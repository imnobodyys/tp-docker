# tp-docker
Exercice:Manipulation de base des conteneurs  
  
Étape 1   
docker --version  
Cette commande affiche la version de Docker installée sur la machine, pour vérifier que Docker est bien installé et opérationnel.  
<img width="771" height="52" alt="image" src="https://github.com/user-attachments/assets/44972ba1-4f92-4fe2-abbd-50b7b8219654" />  
  
Étape 2  
docker images  
Liste les images Docker présentes localement (nom, tag, image ID, date, taille). Cela permet de voir quelles images sont déjà disponibles avant de lancer des conteneurs.  
<img width="2325" height="79" alt="image" src="https://github.com/user-attachments/assets/4b8078fc-acf5-4543-bb4a-013afb50d300" />  
  
Étape 3  
docker pull hello-world  
Télécharge l’image hello-world depuis Docker Hub vers la machine locale. C’est une image minimale utilisée pour tester le bon fonctionnement de Docker.  
<img width="1562" height="272" alt="image" src="https://github.com/user-attachments/assets/023f972d-809e-4cf9-8d73-0145958dfd42" />  
  
Étape 4  
docker run hello-world  
Crée et exécute un conteneur à partir de l’image hello-world. Le conteneur affiche un message de test puis s’arrête automatiquement, ce qui confirme que Docker peut lancer des conteneurs correctement.  
<img width="1592" height="758" alt="image" src="https://github.com/user-attachments/assets/08a63a17-0aa0-4590-a42c-86ecec13e451" />   
  
Étape 5  
docker ps  
Affiche uniquement les conteneurs en cours d’exécution (running). Ici la liste est vide car le conteneur hello-world se termine immédiatement après l’affichage du message.  
<img width="1390" height="47" alt="image" src="https://github.com/user-attachments/assets/ecb4b5f5-567e-4a3f-89c9-ba2329ee6d21" />  
  
Étape 6  
docker ps -a  
Affiche tous les conteneurs, y compris ceux arrêtés (exited). On voit donc le conteneur hello-world avec l’état Exited.  
<img width="2257" height="85" alt="image" src="https://github.com/user-attachments/assets/e46e543c-ce1f-4414-9317-9524912eb0ea" />  
  
Étape 7  
bdocker rm 88e9dc65da4  
Supprime le conteneur (par son ID) pour nettoyer l’environnement.  Affiche tous les conteneurs il n'y a rien.
<img width="1612" height="134" alt="image" src="https://github.com/user-attachments/assets/57229617-4d2f-4158-9dd2-f7776f6b337c" />  
   
Étape 8  
docker rmi d4aaab6242e0  
Supprime l’image Docker locale (par son image ID). Affiche tous les image il n'y a rien.
<img width="1563" height="96" alt="image" src="https://github.com/user-attachments/assets/3fb3b977-f5ed-45bf-81ee-9495a0e44175" />  
  
Exercice : Création d'un serveur web avec Docker  
  
Étape 1  
docker pull nginx  
Télécharge l’image officielle nginx depuis Docker Hub afin de pouvoir lancer un serveur web Nginx dans un conteneur.  
<img width="1608" height="533" alt="image" src="https://github.com/user-attachments/assets/9aa3e2db-4862-4ec8-a848-b36798bff54a" />  
   
Étape 2  
docker run -d -p 8080:80 --name mon_nginx nginx  
crée + démarre un conteneur à partir de l’image nginx ,mode détaché (en arrière-plan),redirige le port 8080 de la machine vers le port 80 du conteneur (HTTP),donne un nom au conteneu.  
<img width="1266" height="56" alt="image" src="https://github.com/user-attachments/assets/518869eb-0fff-4270-9ca1-d9c8d428e2a9" />  
  
Étape 3  
docker ps  
Affiche le conteneur en cours d’exécution. On vérifie que mon_nginx est bien en statut Up et que le mapping de ports est actif.  
<img width="2305" height="171" alt="image" src="https://github.com/user-attachments/assets/b531fd1e-3803-4d93-9159-99069e661369" />  
  
Étape 4  
En ouvrant http://localhost:8080, on accède au serveur Nginx dans le conteneur via la redirection de ports.  
<img width="2871" height="694" alt="image" src="https://github.com/user-attachments/assets/71736978-95aa-42fc-af98-9336cb379688" />  
   
Étape 5  
docker stop mon_nginx  
Arrête proprement le conteneur mon_nginx,Affiche uniquement les conteneurs en cours d’exécution. Ici la liste est vide car le conteneur se termine quand on stop.   
<img width="1425" height="210" alt="image" src="https://github.com/user-attachments/assets/2a93a1dc-7d92-4bb1-aebc-981c5a0d89bb" />  
  
Étape 6  
docker rm mon_nginx  
Supprime le conteneur (par son ID) pour nettoyer l’environnement.  Affiche tous les conteneurs il n'y a rien.  
<img width="1468" height="220" alt="image" src="https://github.com/user-attachments/assets/0daa69af-c4a4-4366-a536-9561b36b4591" />  













