pipeline {
  agent { label "linux" }
  stages {
    stage("build") {
      steps {
        sh """
          docker build -t myapp .
        """
      }
    }
    stage("run") {
      steps {
        sh """
          docker run --rm myapp
        """
      }
    }
  }
}
