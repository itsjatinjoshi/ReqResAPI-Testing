pipeline{
    agent any
    stages{
        stage("Clone the repository") {
            steps {
                bat '''
                cd C:\\Project
                if not exist ReqResAPI-Testing (
                    git 'https://github.com/itsjatinjoshi/ReqResAPI-Testing.git'
                ) else (
                    cd ReqResAPI-Testing
                    git config --global --add safe.directory C:/Project/ReqResAPI-Testing
                    git pull
                )
                '''
            }
        }
        stage("Setup Virtual Environment") {
            steps {
                bat '''
                cd C:\\Project\\ReqResAPI-Testing
                if not exist rest_api_venv (
                    "%PYTHON%" -m venv rest_api_venv
                )
                '''
            }
        }
        stage("Activate Virtual Environment") {
            steps {
                bat '''
                cd C:\\Project\\ReqResAPI-Testing
                cd rest_api_venv\\Scripts
                call activate

                pip install --upgrade pip
                pip install -r requirements.txt
                )
                '''
            }
        }
        stage("Run TestCase") {
            steps {
                bat '''
                cd C:\\Project\\ReqResAPI-Testing
                call rest_api_venv\\Scripts\\activate.bat

                pytest \\test\\.
                )
                '''
            }
        }
    }
}
