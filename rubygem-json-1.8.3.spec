%define rbname json
%define version 1.8.3
%define release 1

Summary: JSON Implementation for Ruby
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: Distributable
URL: http://flori.github.com/json
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
#Source1: ruby-gems-%{rbname}.spec.in
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0.0
BuildRequires: ruby >= 2.0.0
BuildArch: ppc
Provides: ruby(Json) = %{version}

%define gemdir /opt/freeware/lib/ruby/gems/2.0.0
%define gembuilddir %{buildroot}%{gemdir}

%description
This is a JSON implementation as a Ruby extension in C.


%prep
%setup -T -c

%build

%install
%{__rm} -rf %{buildroot}
mkdir -p %{gembuilddir}
gem install --local --install-dir %{gembuilddir} --force %{SOURCE0}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root)
%{gemdir}/gems/%{rbname}-%{version}/


%doc %{gemdir}/doc/%{rbname}-%{version}
%{gemdir}/cache/%{rbname}-%{version}.gem
%{gemdir}/specifications/%{rbname}-%{version}.gemspec

%changelog
* Tue Nov 03 2015 by Bill Wilcox - 1.8.3
- created rpm for gem.
* Mon Sep 08 2014 by Bill Wilcox - 1.8.1
- created rpm for gem.

