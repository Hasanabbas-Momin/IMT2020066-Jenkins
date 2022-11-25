pipeline { 
    agent any
    stages {
        stage('Clone Git') {
            steps {
                git "https://github.com/Hasanabbas-Momin/IMT2020066-Jenkins.git"
            }
        }
        stage('Build Code') {
            steps {
                sh "chmod u+x p.py"
                sh "./p.py"
            }
        }
        stage('Test Code Passed') {
            steps {
                sh "chmod u+x unit_test_1.py"
                sh "./unit_test_1.py"
            }
        }
        stage('Test Code Failed') {
            steps {
                sh "chmod u+x unit_test_2.py"
                sh "./unit_test_2.py"
            }
        }
    } 
}
