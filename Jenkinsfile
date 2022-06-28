pipeline{
    agent any
    environment {
        AWS_ACCOUNT_ID="577252187772"
        AWS_DEFAULT_REGION="us-east-1" 
        IMAGE_REPO_NAME="jenkins-pipeline-docker"
        IMAGE_TAG="latest"
        REPOSITORY_URI = "${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}"
    }
    stages {
        stage('Logging into AWS ECR') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: '44ebb02f-f196-4dbb-a72d-78727702c16d', accessKeyVariable: 'AWS_ACCESS_KEY_ID', secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                  sh "aws ecr get-login-password --region ${AWS_DEFAULT_REGION} | docker login --username AWS --password-stdin ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com"
                }
            }
          }
        stage('gitclone') {
            steps {
                git branch: 'main',
                    credentialsId: 'c3e2de58-f6a8-4f22-9fbc-3e34fbdb93e5',
                    url: 'git@github.com:DmitryBond/MyJenkinsDocker.git'
            }
        }
        stage('Build') {
            steps {
                sh "whoami"
                sh 'sudo docker build -t jenkins-pipeline-docker:latest .'
            }
        } 
       stage('Pushing to ECR') {
             steps {  
                sh "docker tag ${IMAGE_REPO_NAME}:${IMAGE_TAG} ${REPOSITORY_URI}:$IMAGE_TAG"
                sh "docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${IMAGE_REPO_NAME}:${IMAGE_TAG}"
            }
        }
        stage('Deploy to ECS') {
             steps {
                sh 'aws ecs delete-service --cluster JenkinsDockerFargate --service JenkinsFargateTask --force'
                sh 'sleep 60'
                sh 'aws ecs create-service --cluster JenkinsDockerFargate --service-name JenkinsFargateTask --task-definition JenkinsFargate:1 --desired-count 1 --launch-type "FARGATE" --network-configuration "awsvpcConfiguration={subnets=[subnet-0a121e0a92a299939],securityGroups=[sg-04eb8b114a02c9b7d],assignPublicIp=ENABLED}"'
                sh 'aws ecs list-services --cluster JenkinsDockerFargate'
            }
        }
               
    }
}
