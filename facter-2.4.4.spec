%define _prefix /opt/freeware
%define _defaultdocdir %{_prefix}/doc
%define _rubybin /opt/freeware/bin/ruby
%define tarballname facter

%{!?ruby_sitelibdir: %define ruby_sitelibdir %(%{_rubybin} -rrbconfig -e 'puts Config::CONFIG["sitelibdir"]')}


Summary: Ruby module for collecting simple facts about a host operating system
Name: facter
Version: 2.4.4
Release: 1
License: Apache 2.0
Group: System Environment/Base
URL: http://www.puppetlabs.com/puppet/related-projects/%{tarballname}/
Source: %{tarballname}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{tarballname}-%{version}-%{release}-root
BuildArch: noarch

Requires: ruby >= 2.0.0
Provides: facter = 2.4.4
BuildRequires: ruby >= 2.0.0 python readline gdbm

%description
Ruby module for collecting simple facts about a host Operating
system. Some of the facts are preconfigured, such as the hostname and the
operating system. Additional facts can be added through simple Ruby scripts

%prep
rm -rf %{_builddir}/%{name}-%{version}
%setup



%build

%install
%{_rubybin} install.rb --destdir=%{buildroot} --quick --no-rdoc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%{_bindir}/facter
%{ruby_sitelibdir}/facter.rb
%{ruby_sitelibdir}/facter
%doc CHANGELOG INSTALL LICENSE README.md


%changelog
* Tue Nov 03 2015 Bill Wilcox <bwilcox@4ied.net>
- updated for facter 2.4.4.
* Thu Apr 03 2014 Bill Wilcox <bwilcox@4ied.net>
- updated for facter 1.7.5.
* Mon Dec 23 2013 Bill Wilcox <bwilcox@4ied.net>
- created for /opt/freeware install path
* Wed Dec 09 2013 Bill Wilcox <bwilcox@4ied.net>
- updaed for facter 1.7.3.
* Wed Nov 27 2013 Bill Wilcox <bwilcox@4ied.net>
- Modified prefix for private directory install
* Mon Dec 19 2011 Nick Bausch <nick.bausch@gmail.com> - 1.6.3-1.puppet.local
- First facter-puppet-local build for AIX
* Mon Oct 31 2011 Michael Stahnke <stahnma@puppetlabs.com> - 1.6.3-0.1rc1
- 1.6.3 rc1
