pipeline {
  agent { label 'centos'}
  stages {
    stage('build'){
      steps{
        sh 'pwd'
        sh 'ls -ltr'
        sh 'whoami'
        sh 'echo $USER'
      }
    
    }
    
    stage("test"){
      steps{
        sh 'echo "testing"'
      }
    }
    
    stage("deploy"){
      steps{
        sh 'echo "deploying"'
      }
    }
  
  
  }
}
