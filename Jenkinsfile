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
      steps{}
    }
    
    stage("deploy"){
      steps{}
    }
  
  
  }
}
