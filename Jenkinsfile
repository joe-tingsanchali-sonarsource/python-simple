node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner'
    def sonarParams = ""
    
    // Debug: Print environment variables
    echo "BRANCH_NAME: ${env.BRANCH_NAME}"
    echo "CHANGE_ID: ${env.CHANGE_ID}"
    echo "CHANGE_BRANCH: ${env.CHANGE_BRANCH}"
    echo "CHANGE_TARGET: ${env.CHANGE_TARGET}"
    
    // Check if this is a Pull Request build
    if (env.CHANGE_ID) {
      // PR analysis parameters
      // See: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters/parameters-not-settable-in-ui#pull-request-analysis
      sonarParams = "-Dsonar.pullrequest.key=${env.CHANGE_ID} " +
                    "-Dsonar.pullrequest.branch=${env.CHANGE_BRANCH} " +
                    "-Dsonar.pullrequest.base=${env.CHANGE_TARGET ?: 'main'}"
      echo "PR detected, using params: ${sonarParams}"
    } else if (env.BRANCH_NAME && env.BRANCH_NAME != 'main') {
      // Branch analysis (non-main branches)
      // See: https://docs.sonarsource.com/sonarqube-cloud/enriching/branch-analysis-setup#setup-with-a-non-integrated-build-environment
      sonarParams = "-Dsonar.branch.name=${env.BRANCH_NAME} " +
                    "-Dsonar.branch.target=main"
      echo "Branch detected, using params: ${sonarParams}"
    } else {
      echo "Main branch detected, no extra params"
    }
    
    withSonarQubeEnv('SonarCloud') {
      sh "${scannerHome}/bin/sonar-scanner ${sonarParams}"
    }
  }
}

stage("Quality Gate") {
  timeout(time: 1, unit: 'HOURS') {
    def qg = waitForQualityGate(abortPipeline: true)
    if (qg.status != 'OK') {
      error "Pipeline aborted due to quality gate failure: ${qg.status}"
    }
  }
}
