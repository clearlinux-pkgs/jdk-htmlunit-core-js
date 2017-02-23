Name     : jdk-htmlunit-core-js
Version  : core.js.2.17
Release  : 3
URL      : https://github.com/HtmlUnit/htmlunit-core-js/archive/core-js-2.17.tar.gz
Source0  : https://github.com/HtmlUnit/htmlunit-core-js/archive/core-js-2.17.tar.gz
Source1  : https://github.com/HtmlUnit/htmlunit-rhino-fork/archive/ef0faa3e34ef6c3b42c1be4474d0252d96eb4535/htmlunit-rhino-fork-ef0faa3e34ef6c3b42c1be4474d0252d96eb4535.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MPL-2.0-no-copyleft-exception
BuildRequires : jdk-junit4
BuildRequires : apache-ant
BuildRequires : apache-maven
BuildRequires : javapackages-tools
BuildRequires : jdk-aether
BuildRequires : jdk-aopalliance
BuildRequires : jdk-atinject
BuildRequires : jdk-cdi-api
BuildRequires : jdk-commons-cli
BuildRequires : jdk-commons-codec
BuildRequires : jdk-commons-io
BuildRequires : jdk-commons-lang
BuildRequires : jdk-commons-lang3
BuildRequires : jdk-commons-logging
BuildRequires : jdk-guava
BuildRequires : jdk-guice
BuildRequires : jdk-httpcomponents-client
BuildRequires : jdk-httpcomponents-core
BuildRequires : jdk-jsoup
BuildRequires : jdk-jsr-305
BuildRequires : jdk-objectweb-asm
BuildRequires : jdk-plexus-cipher
BuildRequires : jdk-plexus-classworlds
BuildRequires : jdk-plexus-containers
BuildRequires : jdk-plexus-interpolation
BuildRequires : jdk-plexus-sec-dispatcher
BuildRequires : jdk-plexus-utils
BuildRequires : jdk-sisu
BuildRequires : jdk-slf4j
BuildRequires : jdk-wagon
BuildRequires : lxml
BuildRequires : openjdk-dev
BuildRequires : python3
BuildRequires : six
BuildRequires : xmvn
Patch0   : htmlunit-core-js-2.17-build.patch

%description
LiveConnect 3

%prep
%setup -q -n htmlunit-core-js-core-js-2.17

mv %{SOURCE1} .
tar -xf htmlunit-rhino-fork-ef0faa3e34ef6c3b42c1be4474d0252d96eb4535.tar.gz
mv htmlunit-rhino-fork-ef0faa3e34ef6c3b42c1be4474d0252d96eb4535 htmlunit-rhino-fork

# Remove innecessary files
find . -name "*.class"  -print -delete
find . -name "*.jar" -print -delete
find . -name "*.tar.*" -print -delete
find . -name '*.zip' -print -delete

%patch0 -p1

sed -i 's|depends="test"||' build.xml

%build
JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk ant jar-all

%install
python3 /usr/share/java-utils/mvn_artifact.py pom.xml target/htmlunit-core-js-2.17.jar
python3 /usr/share/java-utils/mvn_file.py net.sourceforge.htmlunit:htmlunit-core-js htmlunit-core-js
xmvn-install  -R .xmvn-reactor -n htmlunit-core-js -d %{buildroot}

%files
%defattr(-,root,root,-)
/usr/share/java/htmlunit-core-js.jar
/usr/share/maven-metadata/htmlunit-core-js.xml
/usr/share/maven-poms/htmlunit-core-js.pom
