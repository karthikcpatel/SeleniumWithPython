pipeline {
  agent any
  stages {
    stage('Buzz Buzz') {
      steps {
        echo 'Bees Buzz'
        archive (includes: 'pkg/*.gem')
        publishHTML (target: [
          allowMissing: false,
          alwaysLinkToLastBuild: false,
          keepAll: true,
          reportDir: 'web selenium\\screenshots',
          reportFiles: 'index.html',
          reportName: "KP Pipeline Report"
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
