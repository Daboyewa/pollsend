node {
	checkout scm 
    
    	try {
        	stage('Run unit/integration test') {
        	sh 'make test'
  	  }       
        
        	stage('build application artifacts') {
        	sh 'make build'
    	  }
        
        	stage('Create release environment and run accptance tests') {
        	sh 'make release'
    	  }
        
       		stage('Tag and publis release image') {
        	sh "make tag latest \$(git rev-parse --short HEAD) \$(git tag --points-at HEAD)"
        	sh "make buildtag master \$(git tag --point-at HEAD)"
        	withEnv(["DOCKER_USER=${DOCKER_USER}",
                 	"DOCKER_PASSWORD=${DOCKER_PASSWORD}",
                 	"DOCKER_EMAIL=${DOCKER_EMAIL}"]) {
            	sh "make login"
            	sh "make publish"         
          }       
       }  
    }
    
        finally {
                stage ('Collect test reports') {
        	step([$class: 'JUnitResultArchiver', testResults: '**/reports/*.xml'])
          }
                stage('clean up') {
                sh 'sudo make clean'
                sh 'sudo make logout'
         }
     }
}
