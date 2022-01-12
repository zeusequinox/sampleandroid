pipeline {
  agent { label 'centos'}
  stages {
    stage('build'){
      steps{
        sh 'echo $(pwd)'
        sh 'echo $(ls -ltr)'
      }
    
    }
    
    stage("test"){
      steps{
        sh 'echo "testing"'
      }
    }
    
    stage("deploy"){
      steps{
        sh 'echo "deploying"
      }
    }
  
  
  }
}
