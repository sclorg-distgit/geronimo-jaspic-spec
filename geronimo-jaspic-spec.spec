%global pkg_name geronimo-jaspic-spec
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

%define api_version 1.0
%define g_pkg_name geronimo-jaspic_%{api_version}_spec
Name:          %{?scl_prefix}%{pkg_name}
Version:       1.1
Release:       9.6%{?dist}
Summary:       Java Authentication SPI for Containers
License:       ASL 2.0 and W3C
URL:           http://geronimo.apache.org/
Source0:       http://repo2.maven.org/maven2/org/apache/geronimo/specs/%{g_pkg_name}/%{version}/%{g_pkg_name}-%{version}-source-release.tar.gz

BuildArch:     noarch

BuildRequires: %{?scl_prefix}maven-local
BuildRequires: %{?scl_prefix}maven-plugin-bundle
BuildRequires: %{?scl_prefix}geronimo-osgi-support
BuildRequires: %{?scl_prefix}geronimo-parent-poms
BuildRequires: %{?scl_prefix}javapackages-tools

%description
Java Authentication Service Provider Interface for Containers (JSR-196) api.

%package javadoc
Summary:        API documentation for %{pkg_name}

%description javadoc
%{summary}.


%prep
%setup -q -n %{g_pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x

for d in LICENSE NOTICE ; do
  iconv -f iso8859-1 -t utf-8 $d > $d.conv && mv -f $d.conv $d
  sed -i 's/\r//' $d
done

%pom_xpath_remove "pom:parent"
%pom_xpath_inject "pom:project" "
    <parent>
      <groupId>org.apache.geronimo.specs</groupId>
      <artifactId>specs</artifactId>
      <version>any</version>
    </parent>"
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_file  : %{pkg_name}
%mvn_alias : org.eclipse.jetty.orbit:javax.security.auth.message
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE

%changelog
* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-9.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-9.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-9.4
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-9.3
- Remove requires on java

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-9.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-9.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.1-9
- Mass rebuild 2013-12-27

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-8
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Mon Mar  4 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-7
- Add depmap for org.eclipse.jetty.orbit
- Resolves: rhbz#917621

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 1.1-5
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Jan 17 2013 Michal Srb <msrb@redhat.com> - 1.1-4
- Build with xmvn

* Thu Aug 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-3
- Fix license tag

* Mon Jul 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-2
- Add BR: geronimo-osgi-support

* Mon Jul 23 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 1.1-1
- Update to upstream version 1.1

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Dec 19 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 1.0-1
- Initial package (based on Mageia version)
