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
          reportDir: 'leetcode',
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
