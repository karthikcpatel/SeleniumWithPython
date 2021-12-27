pipeline {
  agent any
  stages {
    stage('Buzz Buzz') {
      steps {
        echo 'Bees Buzz'
        archiveArtifacts(artifacts: 'target/*.jar', fingerprint: true)
        junit '**/surefire-reports/**/*.xml'
      }
    }

    stage('Bees Bees') {
      steps {
        echo 'Bees Buzzing!'
      }
    }

  }
}
