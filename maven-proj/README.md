```bash
# Install Java 11 and Maven
sudo apt install -y openjdk-11-jdk maven

# Check versions
java -version
mvn -v

# Create Maven project using quickstart archetype
mvn archetype:generate \
 -DgroupId=com.example \
 -DartifactId=myapp \
 -DarchetypeArtifactId=maven-archetype-quickstart \
 -DinteractiveMode=false

# Go to project folder
cd myapp

# (Optional) Update Java version in pom.xml
# Add inside 
# <properties>
# <maven.compiler.source>11</maven.compiler.source>
# <maven.compiler.target>11</maven.compiler.target>
# </properties>

# Compile the project
mvn compile

# Run the project (default quickstart main class)
mvn exec:java -Dexec.mainClass="com.example.App"

# Package as JAR
mvn package

# Run the packaged JAR
java -cp target/myapp-1.0-SNAPSHOT.jar com.example.App
