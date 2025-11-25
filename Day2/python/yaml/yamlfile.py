import yaml

def writeToYAMLFile( filename, content ):
    file = open(filename, "a")
    yaml.dump( content, file )

def readFromYAMLFile( filename ):
    file = open(filename, "r") 
    data = yaml.safe_load(file)
    print(data)

profile = {
     "name": "Jeganathan Swaminathan",
     "role": "Freelance Sofware Consultant",
     "trainings": ["Openshift", "Microservices", "Python"],
     "experience": 25
}

writeToYAMLFile( "profiles.yml", profile )
readFromYAMLFile( "profiles.yml" )
