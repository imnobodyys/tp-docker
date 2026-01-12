# tp-docker
  
# Exercice:Manipulation de base des conteneurs  
  
## Étape 1   

Commande: docker --version  
Explication: Cette commande affiche la version de Docker installée sur la machine, pour vérifier que Docker est bien installé et opérationnel.  
Résultat :  
<img width="771" height="52" alt="image" src="https://github.com/user-attachments/assets/44972ba1-4f92-4fe2-abbd-50b7b8219654" />  
  
## Étape 2  
Commande: docker images  
Explication: Liste les images Docker présentes localement (nom, tag, image ID, date, taille). Cela permet de voir quelles images sont déjà disponibles avant de lancer des conteneurs.  
Résultat :  
<img width="2325" height="79" alt="image" src="https://github.com/user-attachments/assets/4b8078fc-acf5-4543-bb4a-013afb50d300" />  
  
## Étape 3  
Commande: docker pull hello-world  
Explication: Télécharge l’image hello-world depuis Docker Hub vers la machine locale. C’est une image minimale utilisée pour tester le bon fonctionnement de Docker.  
Résultat :  
<img width="1562" height="272" alt="image" src="https://github.com/user-attachments/assets/023f972d-809e-4cf9-8d73-0145958dfd42" />  
  
## Étape 4  
Commande: docker run hello-world  
Explication: Crée et exécute un conteneur à partir de l’image hello-world. Le conteneur affiche un message de test puis s’arrête automatiquement, ce qui confirme que Docker peut lancer des conteneurs correctement.  
Résultat :  
<img width="1592" height="758" alt="image" src="https://github.com/user-attachments/assets/08a63a17-0aa0-4590-a42c-86ecec13e451" />   
  
## Étape 5  
Commande: docker ps  
Explication: Affiche uniquement les conteneurs en cours d’exécution (running). Ici la liste est vide car le conteneur hello-world se termine immédiatement après l’affichage du message.  
Résultat :  
<img width="1390" height="47" alt="image" src="https://github.com/user-attachments/assets/ecb4b5f5-567e-4a3f-89c9-ba2329ee6d21" />  
  
## Étape 6  
Commande: docker ps -a  
Explication: Affiche tous les conteneurs, y compris ceux arrêtés (exited). On voit donc le conteneur hello-world avec l’état Exited.  
Résultat :  
<img width="2257" height="85" alt="image" src="https://github.com/user-attachments/assets/e46e543c-ce1f-4414-9317-9524912eb0ea" />  
  
## Étape 7  
Commande: bdocker rm 88e9dc65da4  
Explication: Supprime le conteneur (par son ID) pour nettoyer l’environnement.  Affiche tous les conteneurs il n'y a rien.  
Résultat :  
<img width="1612" height="134" alt="image" src="https://github.com/user-attachments/assets/57229617-4d2f-4158-9dd2-f7776f6b337c" />  
   
## Étape 8  
Commande: docker rmi d4aaab6242e0  
Explication: Supprime l’image Docker locale (par son image ID). Affiche tous les image il n'y a rien.  
Résultat :  
<img width="1563" height="96" alt="image" src="https://github.com/user-attachments/assets/3fb3b977-f5ed-45bf-81ee-9495a0e44175" />  
  
# Exercice : Création d'un serveur web avec Docker  
  
## Étape 1  
Commande: docker pull nginx  
Explication: Télécharge l’image officielle nginx depuis Docker Hub afin de pouvoir lancer un serveur web Nginx dans un conteneur.  
Résultat :  
<img width="1608" height="533" alt="image" src="https://github.com/user-attachments/assets/9aa3e2db-4862-4ec8-a848-b36798bff54a" />  
   
## Étape 2  
Commande: docker run -d -p 8080:80 --name mon_nginx nginx  
Explication: crée + démarre un conteneur à partir de l’image nginx ,mode détaché (en arrière-plan),redirige le port 8080 de la machine vers le port 80 du conteneur (HTTP),donne un nom au conteneu.  Résultat :
<img width="1266" height="56" alt="image" src="https://github.com/user-attachments/assets/518869eb-0fff-4270-9ca1-d9c8d428e2a9" />  
  
## Étape 3  
Commande: docker ps  
Explication: Affiche le conteneur en cours d’exécution. On vérifie que mon_nginx est bien en statut Up et que le mapping de ports est actif.  
Résultat :  
<img width="2305" height="171" alt="image" src="https://github.com/user-attachments/assets/b531fd1e-3803-4d93-9159-99069e661369" />  
  
## Étape 4  
Explication: En ouvrant http://localhost:8080, on accède au serveur Nginx dans le conteneur via la redirection de ports.  
Résultat :  
<img width="2871" height="694" alt="image" src="https://github.com/user-attachments/assets/71736978-95aa-42fc-af98-9336cb379688" />  
   
## Étape 5  
Commande: docker stop mon_nginx  
Explication: Arrête proprement le conteneur mon_nginx,Affiche uniquement les conteneurs en cours d’exécution. Ici la liste est vide car le conteneur se termine quand on stop.   
Résultat :  
<img width="1425" height="210" alt="image" src="https://github.com/user-attachments/assets/2a93a1dc-7d92-4bb1-aebc-981c5a0d89bb" />  
  
## Étape 6  
Commande: docker rm mon_nginx  
Explication: Supprime le conteneur (par son ID) pour nettoyer l’environnement.  Affiche tous les conteneurs il n'y a rien.  
Résultat :  
<img width="1468" height="220" alt="image" src="https://github.com/user-attachments/assets/0daa69af-c4a4-4366-a536-9561b36b4591" />  
  
# Exercice : Déploiement d'une application Python Flask  

## Étape 1  
Explication: J'ai créé une application Flask qui affiche un message "Hello World"  
Résultat :  
<img width="1248" height="577" alt="image" src="https://github.com/user-attachments/assets/0dcbf7fa-45a7-476b-a81d-5e4e4cb7fac1" />  

## Étape 2  
Commande: creer dockfile  
Explication: écrit un Dockerfile qui définit comment construire l'image Docker de mon application. Ce fichier contient toutes les instructions nécessaires pour créer un environnement isolé avec Python et Flask.   
Résultat :  
<img width="1036" height="347" alt="image" src="https://github.com/user-attachments/assets/95c98042-bc3f-42ac-b58b-4f0d0aa288ac" />  
  
## Étape 3  
Commande: docker build -t flask-app .   
Explication: Docker lit le Dockerfile et crée une image contenant Python, Flask et notre application.  
Résultat :  
<img width="1580" height="815" alt="image" src="https://github.com/user-attachments/assets/1ca7170a-8d0d-4557-aaaa-7685cb37be78" />  

## Étape 4  
Commande: docker run -d -p 5000:5000 --name mon-flask-app flask-app   
Explication: Le conteneur est créé et l'application Flask est accessible.  
Résultat :  
<img width="1446" height="479" alt="image" src="https://github.com/user-attachments/assets/70c96e50-2964-44f3-b9bf-bfaf68f1638b" />  
  
## Étape 5    
Explication: Après avoir terminé les tests, on peut arrêter et supprimer le conteneur,Si l'image n'est plus nécessaire, on peut également la supprimer   
Résultat :  
<img width="1187" height="328" alt="image" src="https://github.com/user-attachments/assets/9b0a3f3f-42d4-4fab-aaef-2c836e07a5d1" />  




# Exercice : Utilisation de docker compose  
## Étape 1  
Explication: Modifier cloude3.py pour la connexion MongoDB   
Résultat :  
<img width="1600" height="1228" alt="image" src="https://github.com/user-attachments/assets/a65d8536-e0ce-44f0-b4dc-b9cdddeda986" />  
  
## Étape 2  
Explication: Créer requirements.txt  
Résultat :  
<img width="1249" height="504" alt="image" src="https://github.com/user-attachments/assets/6dff5107-e67a-4aa1-a3ce-444c70fa83af" />  
  
## Étape 3  
Explication: Modifier le Dockerfile  
Résultat :  
<img width="1117" height="559" alt="image" src="https://github.com/user-attachments/assets/97bcc837-8c5c-439f-8c08-286c3e7e50f2" />  
  
## Étape 4   
Explication: Créer docker-compose.yml  
Résultat :  
<img width="1727" height="1178" alt="image" src="https://github.com/user-attachments/assets/f8c2f4e3-4b0e-4433-a2e8-bdbe8915d66c" />  
  
## Étape 6   

Commande: docker-compose up -d  
Explication: Lancer Docker Compose  
Résultat :  
<img width="2423" height="1090" alt="image" src="https://github.com/user-attachments/assets/ac659a5d-2131-47e5-b5b3-0bd9c6faf590" />  
Vérifier que les conteneurs fonctionnent  
docker-compose ps  
<img width="2421" height="194" alt="image" src="https://github.com/user-attachments/assets/fa0b0e11-bb0c-4560-be39-7d8d4316d20f" />  

## Étape 7  
Explication: Tester la connexion MongoDB  
Résultat :  
<img width="1894" height="558" alt="image" src="https://github.com/user-attachments/assets/59e8ce83-c161-423f-84b3-48523c70f6ba" />  
<img width="1475" height="588" alt="image" src="https://github.com/user-attachments/assets/194a6b96-6ad8-4840-8e2d-8911e467abba" />  
<img width="1407" height="502" alt="image" src="https://github.com/user-attachments/assets/8aacd4a3-029a-4287-a9d4-5952eb347855" />  
  
## Étape 8  
Commande: docker-compose stop  
Explication:Cette commande arrête tous les conteneurs définis dans le fichier docker-compose.yml sans les supprimer. Les conteneurs restent présents sur le système mais ne sont plus en cours d'exécution. Cette approche est utile lorsqu'on souhaite mettre en pause l'application temporairement sans perdre la configuration des conteneurs.  
Résultat :  
<img width="2422" height="134" alt="image" src="https://github.com/user-attachments/assets/28f4fd4b-5ced-4266-b49a-1a957d6027b6" />  
  
## Étape 9  
Commande: docker-compose ps -a  
Explication:Cette commande affiche l'état de tous les conteneurs gérés par Docker Compose, y compris ceux qui sont arrêtés. Le paramètre `-a` (all) permet de voir également les conteneurs qui ne sont pas en cours d'exécution.     
Résultat :  
<img width="2477" height="139" alt="image" src="https://github.com/user-attachments/assets/ac888403-2c07-43eb-ab14-14b2b461dff2" />  

## Étape 10
Commande: docker-compose down   
Explication:Cette commande ne supprime PAS les volumes de données par défaut. Les données MongoDB sont donc préservées dans le volume `mongo-data`. Pour supprimer également les volumes, il faudrait utiliser `docker-compose down -v`.     
Résultat :  
<img width="2453" height="174" alt="image" src="https://github.com/user-attachments/assets/ca46f594-b5b7-4ccd-8dc2-b7641a19255f" />  








