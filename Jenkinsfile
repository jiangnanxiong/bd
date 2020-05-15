pipeline {
  agent any
  stages {
    stage('git pull') {
      steps {
        git 'https://github.com/jiangnanxiong/bd.git'
      }
    }

    stage('run') {
      steps {
        bat 'python run.py'
      }
    }

  }
}