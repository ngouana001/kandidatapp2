pipeline {
    environment {
        IMAGE_NAME = "kandidatapp2"
        DOCKERHUB_ID = "royem001"
        DOCKERHUB_PASSWORD = credentials('dockerhub_password')
        HOST_IP = "${HOST_IP_PARAM}"
        HOST_PORT = "${HOST_PORT_PARAM}"
    }
    agent none
    stages {
       stage('Build image') {
           agent any
           steps {
              script {
                sh '''
                  echo "BUILD"
                  docker build -t ${DOCKERHUB_ID}/$IMAGE_NAME:${GIT_COMMIT} .
                  '''
              }
           }
       }
       stage('Run container') {
          agent any
          steps {
            script {
              sh '''
                  docker rm -f $IMAGE_NAME
                  docker run --name $IMAGE_NAME -d -p $HOST_PORT:80 ${DOCKERHUB_ID}/$IMAGE_NAME:${GIT_COMMIT}
                  sleep 5
              '''
             }
          }
       }

<<<<<<< HEAD
       stage('Test unitaires Application') {
=======


       stage('unit-Tests Application') {
>>>>>>> 978e9f8b64a8ed8be9563ad00daedb053f385e5a
           agent any
           steps {
              script {
                     switch(GIT_BRANCH) {
                        case "origin/Login": 
<<<<<<< HEAD
                             echo "CODE DE TEST du login";
                            break
                        case "origin/Logout":
                            echo "CODE DE TEST du logout";
                            break
                        case "origin/Register":
                            echo "CODE DE TEST du Register";
                            break
                        case "origin/master":
                            echo "CODE DE TEST du master";
=======
                             echo " TEST login";
                            break
                        case "origin/Logout":
                            echo "TEST logout";
                            break
                        case "origin/Register":
                            echo "TEST Register";
                            break
                        case "origin/master":
                            echo "TEST master";
>>>>>>> 978e9f8b64a8ed8be9563ad00daedb053f385e5a
                            break                        
                    } 
              }
           }
       }
               
<<<<<<< HEAD
       stage('Tests fonctionnels') {
=======
       stage('funktionstests ') {
>>>>>>> 978e9f8b64a8ed8be9563ad00daedb053f385e5a
           agent any
           steps {
              script {
                sh '''
                    curl ${HOST_IP}:${HOST_PORT} -I  | grep -i 302
                   '''
              }
           }
       }
       stage('Clean container') {
          agent any
          steps {
             script {
               sh '''
                   docker stop $IMAGE_NAME
                   docker rm $IMAGE_NAME
               '''
             }
          }
      }

      stage('Anmeldung und Push-Image auf Docker-Hub') {
          agent any
          steps {
              script {
                env.branche="test"
                    sh '''
                        echo $DOCKERHUB_PASSWORD | docker login -u ${DOCKERHUB_ID} --password-stdin
                    '''
                    switch(GIT_BRANCH) {
                        case "origin/Login": 
                            echo "BRANCHE LOGIN";
                            env.branche="login";
                            break
                        case "origin/Logout":
                            env.branche="logout";
                            break
                        case "origin/Register":
                            env.branche="register";
                            break
                        case "origin/master":
                            env.branche="master";
                            break                        
                    } 
                    sh '''
                        echo "Push image on dockerhub" 
                        docker tag ${DOCKERHUB_ID}/$IMAGE_NAME:${GIT_COMMIT} ${DOCKERHUB_ID}/${IMAGE_NAME}:${branche}-${GIT_COMMIT}
                        docker push ${DOCKERHUB_ID}/${IMAGE_NAME}:${branche}-${GIT_COMMIT}
                        echo $tag_name
                    '''                                   
                    if (tag_name  == 'v*') 
                        {
                            sh '''
<<<<<<< HEAD
                                echo "Production de la nouvelle release ${TAG_NAME} "
=======
                                echo "neus release ${TAG_NAME} "
>>>>>>> 978e9f8b64a8ed8be9563ad00daedb053f385e5a
                                docker tag ${DOCKERHUB_ID}/$IMAGE_NAME:${GIT_COMMIT} ${DOCKERHUB_ID}/${IMAGE_NAME}:${TAG_NAME}
                                docker push ${DOCKERHUB_ID}/${IMAGE_NAME}:${TAG_NAME} 

                            '''
                        }
                }
           }
       }

    }   
}
