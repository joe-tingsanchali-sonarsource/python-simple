node {
  stage('SCM') {
    checkout scm
  }
  stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner'
    def sonarParams = ""
    
    // Check if this is a Pull Request build
    if (env.CHANGE_ID) {
      // PR analysis parameters
      // See: https://docs.sonarsource.com/sonarqube-cloud/advanced-setup/analysis-parameters/parameters-not-settable-in-ui#pull-request-analysis
      sonarParams = "-Dsonar.pullrequest.key=${env.CHANGE_ID} " +
                    "-Dsonar.pullrequest.branch=${env.CHANGE_BRANCH} " +
                    "-Dsonar.pullrequest.base=${env.CHANGE_TARGET ?: 'main'}"
    } else if (env.BRANCH_NAME && env.BRANCH_NAME != 'main') {
      // Branch analysis (non-main branches)
      sonarParams = "-Dsonar.branch.name=${env.BRANCH_NAME}"
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
