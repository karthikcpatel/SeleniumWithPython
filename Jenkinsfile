pipeline {
  agent any
  stages {
    stage('Buzz Buzz') {
      steps {
        echo 'Bees Buzz'
        publishHTML (target: [
          allowMissing: false,
          alwaysLinkToLastBuild: false,
          keepAll: true,
          reportDir: 'coverage',
          reportFiles: 'index.html',
          reportName: "RCov Report"
        ])
      }
    }

    stage('Bees Bees') {
      steps {
        echo 'Bees Buzzing!'
      }
    }

  }
}
