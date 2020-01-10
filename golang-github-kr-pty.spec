%global debug_package   %{nil}
%global import_path     github.com/kr/pty
%global gopath          %{_datadir}/gocode
%global commit          98c7b800832d8aaa5ab1362ba0f19eea291900d9
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-kr-pty
Version:        0
Release:        0.19.git%{shortcommit}%{?dist}
Summary:        PTY interface for Go
License:        MIT
URL:            http://godoc.org/%{import_path}
Source0:        https://%{import_path}/archive/%{commit}/pty-%{shortcommit}.tar.gz
%if 0%{?fedora} >= 19
BuildArch:      noarch
%else
ExclusiveArch:  %{ix86} x86_64 %{arm}
%endif

%description
Pty is a Go package for using UNIX pseudo-terminals.

%package devel
BuildRequires:  golang
Requires:       golang
Summary:        PTY interface for Go
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
Pty is a Go package for using UNIX pseudo-terminals.

This package contains library source intended for building other packages
which use kr/pty.

%prep
%setup -n pty-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}

%files devel
%defattr(-,root,root,-)
%doc License README.md
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/github.com
%dir %attr(755,root,root) %{gopath}/src/github.com/kr
%dir %attr(755,root,root) %{gopath}/src/github.com/kr/pty
%{gopath}/src/%{import_path}/*.go

%changelog
* Fri Mar 07 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.19.git98c7b80
-  Add pty_unsupported.go file in order to allow projects to import the
package and still compile on other os/arch

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.18.git3b1f648
- exclusivearch for el6+

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.17.git3b1f648
- revert golang >= 1.2 version requirement

* Wed Jan 15 2014 Lokesh Mandvekar <lsm5@redhat.com> 0-0.16.git3b1f648
- require golang 1.2 and up

* Wed Oct 16 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.15.git3b1f648
- removed double quotes from provides

* Tue Oct 08 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.14.git3b1f648
- noarch for f19+ and rhel7+, exclusivearch otherwise

* Mon Oct 07 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.13.git3b1f648
- exclusivearch as per golang

* Sun Oct 06 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.12.git3b1f648
- excluded for ppc64
- debug_package nil

* Wed Oct 02 2013 Lokesh Mandvekar <lsm5@fedoraproject.org> 0-0.11.git3b1f648
- docker first run error fix

* Sun Sep 22 2013 Matthew Miller <mattdm@fedoraproject.org> 0-0.10.git27435c6
- install just the source code for devel package

* Tue Sep 17 2013 Lokesh Mandvekar <lsm5@redhat.com> 0-0.9.git27435c6
- version format changed
- docdir unversioned

* Mon Sep 16 2013 Lokesh Mandvekar <lsm5@redhat.com> git27435c6-8
- No debuginfo generated, was empty to begin with
- package owns all directories in import_path

* Mon Sep 16 2013 Lokesh Mandvekar <lsm5@redhat.com> git27435c6-7
- only devel package generated
- Provides moved to devel package
- docdir modified

* Wed Sep 11 2013 Lokesh Mandvekar <lsm5@redhat.com> git27435c6-6
- rm from install section removed

* Tue Sep 10 2013 Lokesh Mandvekar <lsm5@redhat.com> git27435c6-5
- cleanup in prep and build as per guidelines

* Tue Sep 10 2013 Lokesh Mandvekar <lsm5@redhat.com> git27435c6-4
- Build under all circumstances
- Go pkg archives handled (thanks to Vincent Batts (vbatts@redhat.com)

* Thu Aug 29 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-3
- Devel package generated

* Wed Aug 28 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-2
- Fixed permissions

* Mon Aug 26 2013 Lokesh Mandvekar <lsm5@redhat.com> 0.0.1-1
- Initial fedora package
