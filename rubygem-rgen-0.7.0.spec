%define rbname rgen
%define version 0.7.0
%define release 1

Summary: RGen is a framework for Model Driven Software Development (MDSD) in Ruby.
Name: rubygem-%{rbname}

Version: %{version}
Release: %{release}
Group: Development/Ruby
License: N/A
URL: http://ruby-gen.org/
Source0: %{rbname}-%{version}.gem
# Make sure the spec template is included in the SRPM
#Source1: ruby-gems-%{rbname}.spec.in
BuildRoot: %{_tmppath}/%{name}-%{version}-root
Requires: ruby >= 2.0.0
BuildRequires: ruby >= 2.0.0
BuildArch: noarch
Provides: ruby(%{rbname}) = %{version}

%define gemdir /opt/freeware/lib/ruby/gems/2.0.0
%define gembuilddir %{buildroot}%{gemdir}

%description
RGen is a framework for Model Driven Software Development (MDSD)
in Ruby. This means that it helps you build Metamodels, instantiate
Models, modify and transform Models and finally generate arbitrary
textual content from it.

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
* Tue Nov 03 2015 by Bill Wilcox - 0.7.0
- created rpm for gem.

