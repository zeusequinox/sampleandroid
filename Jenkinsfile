pipeline {
  agent { label 'centos'}
  environment {
    ALIAS = credentials('alias')
    KEYSTORE_PASSWORD = credentials('keystore_password')
    KEY_PASSWORD = credentials('key_password')
    KEYSTORE = credentials('keystore')
  }
  stages {
    stage('build'){
      steps{
        sh 'echo "STEP 1 Gradle Tasks"'
        sh 'sudo -E env "PATH=$PATH" ./gradlew tasks'
        sh 'echo "STEP 2 GRADLE ASSEMBLE RELEASE"'
        sh 'sudo -E env "PATH=$PATH" ./gradlew assembleRelease'
        sh 'echo "STEP 3 GRADLE BUNDLE RELEASE"'
        sh 'sudo -E env "PATH=$PATH" ./gradlew bundleRelease'
        sh 'echo "STEP 4 ZIP ALIGN APK"'
        sh 'sudo -E env "PATH=$PATH" zipalign -p 4 /app/build/outputs/apk/release/app-release-unsigned.apk app-aligned.apk'
        sh 'echo "STEP 5 SIGN APK"'
        sh 'sudo -E env "PATH=$PATH" apksigner sign --ks $KEYSTORE --ks-key-alias $ALIAS --ks-pass pass:$KEYSTORE_PASSWORD --key-pass pass:$KEY_PASSWORD app-aligned.apk'
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
