%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .GA
%global namedversion %{version}%{?namedreltag}

Name:             apiviz
Version:          1.3.2
Release:          8.3
Summary:          APIviz is a JavaDoc doclet to generate class and package diagrams
Group:            Development/Java
License:          LGPLv2+
URL:              http://code.google.com/p/apiviz/
Source0:          http://apiviz.googlecode.com/files/apiviz-%{namedversion}-dist.tar.gz
Patch0:           0001-JDK7-compatibility.patch
Patch1:           0002-JDK8-compatibility.patch

BuildArch:        noarch

BuildRequires:    jpackage-utils
BuildRequires:    maven-local
BuildRequires:    maven-antrun-plugin
BuildRequires:    maven-compiler-plugin
BuildRequires:    maven-install-plugin
BuildRequires:    maven-jar-plugin
BuildRequires:    maven-javadoc-plugin
BuildRequires:    maven-release-plugin
BuildRequires:    maven-resources-plugin
BuildRequires:    maven-enforcer-plugin
BuildRequires:    maven-surefire-plugin
BuildRequires:    maven-surefire-provider-junit
BuildRequires:    maven-plugin-jxr
BuildRequires:    jdepend
BuildRequires:    ant-contrib
BuildRequires:    junit

%description
APIviz is a JavaDoc doclet which extends the Java standard doclet.
It generates comprehensive UML-like class and package diagrams for
quick understanding of the overall API structure. 

%package javadoc
Summary:          Javadocs for %{name}
Group:            Documentation

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n apiviz-%{namedversion}
%patch0 -p1
%patch1 -p1

find -name '*.class' -exec rm -f '{}' \;
find -name '*.jar' -exec rm -f '{}' \;

#%pom_xpath_remove "pom:dependencies/pom:dependency[pom:artifactId = 'tools']/pom:scope"
#%pom_xpath_remove "pom:dependencies/pom:dependency[pom:artifactId = 'tools']/pom:systemPath"

%pom_remove_dep com.sun:tools
%pom_add_dep com.sun:tools:any:compile

%mvn_alias "org.jboss.apiviz:apiviz" "net.gleamynode.apiviz:apiviz"

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc COPYRIGHT.txt LICENSE.jdepend.txt LICENSE.txt NOTICE.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt

%changelog
* Tue Jun 17 2014 Marek Goldmann <mgoldman@redhat.com> - 1.3.2-8
- Switch to xmvn + BR updates

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Mar 28 2014 Michael Simacek <msimacek@redhat.com> - 1.3.2-6
- Use Requires: java-headless rebuild (#1067528)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.3.2-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Wed Oct 17 2012 Marek Goldmann <mgoldman@redhat.com> - 1.3.2-2
- Added maven-enforcer-plugin BR

* Wed Oct 17 2012 Marek Goldmann <mgoldman@redhat.com> - 1.3.2-1
- Upstream release 1.3.2.GA
- Removed JDK7 patch

* Mon Sep  3 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.3.1-8
- Add missing R: graphviz

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Mar 12 2012 Marek Goldmann <mgoldman@redhat.com> 1.3.1-6
- Added additional POM mapping

* Fri Mar 09 2012 Marek Goldmann <mgoldman@redhat.com> 1.3.1-5
- Relocated jars to _javadir

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Nov 18 2011 Marek Goldmann <mgoldman@redhat.com> 1.3.1-3
- Working on on jdk7

* Wed Jul 27 2011 Marek Goldmann <mgoldman@redhat.com> 1.3.1-2
- Using upstream tarball

* Wed Jul 20 2011 Marek Goldmann <mgoldman@redhat.com> 1.3.1-1
- Initial packaging


