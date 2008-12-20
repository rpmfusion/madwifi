%define revision r3867-20080924

Name:           madwifi
Version:        0.9.4
Release:        51.%(echo %{revision}| tr - _)%{?dist}
Summary:        Kernel module and Diagnostic tools for Atheros wireless devices

Group:          System Environment/Base
License:        GPLv2
URL:            http://madwifi.org/
Source0:        http://snapshots.madwifi.org/madwifi-trunk/madwifi-trunk-%{revision}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Provides:       madwifi-kmod-common = %{version}
Requires:       madwifi-kmod >= %{version}

Source1:        madwifi-modprobe.d
Source2:        ath5k_blacklist-modprobe.d

# kmod not supported for ppc64
ExcludeArch:    ppc64

%description
madwifi is the Multiband Atheros Driver for WiFi, a linux device
driver for 802.11a/b/g universal NIC cards - either Cardbus, PCI or
MiniPCI - that use Atheros chipsets (ar5210, ar5211, ar5212).

This package contains diagnostic tools you can use to get information
about your madwifi Atheros wireless connections. You do not need this
package to make a madwifi connection.

%package devel
Summary:        Headers for building apps against madwifi
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains headers for building apps against madwifi.

%prep
%setup -q -n madwifi-trunk-%{revision}


%build
make -C tools CFLAGS="${RPM_OPT_FLAGS}"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make -C tools DESTDIR=$RPM_BUILD_ROOT BINDIR=%{_bindir} MANDIR=%{_mandir} STRIP=/bin/echo install
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}/include/sys
mkdir -p $RPM_BUILD_ROOT%{_includedir}/%{name}/net80211
find include net80211 -name \*.h -exec cp {} $RPM_BUILD_ROOT%{_includedir}/%{name}/{} \;

install -D -p -m 0644 %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/madwifi
install -D -p -m 0644 %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/modprobe.d/blacklist-ath5k

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYRIGHT README THANKS
%{_bindir}/*
%{_mandir}/man8/*
%config(noreplace) %{_sysconfdir}/modprobe.d/madwifi
%config(noreplace) %{_sysconfdir}/modprobe.d/blacklist-ath5k

%files devel
%defattr(-,root,root,-)
%{_includedir}/*


%changelog
* Sat Dec 20 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> - 0.9.4-51.r3867_20080924
- ExcludeArch ppc64

* Tue Sep 30 2008 kwizart < kwizart at gmail.com > - 0.9.4-50.r3867-20080924
- Update to r3867-20080924

* Tue Jul 15 2008 kwizart < kwizart at gmail.com > - 0.9.4-10.r3771
- Update snapshot to r3771-20080715

* Wed Feb 13 2008 kwizart < kwizart at gmail.com > - 0.9.4-1
- Update to 0.9.4

* Thu Oct 18 2007 kwizart < kwizart at gmail.com > - 0.9.3.3-1
- Update to 0.9.3.3
- Security bugfix: http://bugzilla.livna.org/show_bug.cgi?id=1675
  CVE-2007-5448: madwifi assertion error DoS
- Add blacklist-ath5k

* Sun Sep 09 2007 Thorsten Leemhuis <fedora[AT]leemhuis.info> - 0.9.3.2-1
- Update to 0.9.3.2

* Wed May 23 2007 Dams <anvil[AT]livna.org> - 0.9.3.1-1
- Updated to 0.9.3.1

* Mon Mar 19 2007 Dams <anvil[AT]livna.org> - 0.9.3-1
- Updated to 0.9.3

* Fri Dec  8 2006 Dams <anvil[AT]livna.org> - 0.9.2.1-1
- Updated to upstream 0.9.2.1

* Fri Aug 18 2006 Dams <anvil[AT]livna.org> - 0.9.2-1
- Updated to 0.9.2
- Dont strip tools (#992)
- Fixed typo in description (#997)

* Thu Jun 15 2006 Dams <anvil[AT]livna.org> - 0.9.0-1
- Updated to 0.9.0

* Sat May 20 2006 Dams <anvil[AT]livna.org> - 0.0.0.20060520-6
- Updated to snapshot 20060250

* Sun May 14 2006 Ville Skyttä <ville.skytta at iki.fi> - 0.0.0.20060317-5
- Require madwifi-kmod instead of kmod-madwifi (#970).

* Sat Mar 25 2006 Gianluca Sforna <giallu [AT] gmail [DOT] com> 0.0.0.20060317-4
- added modprobe.d config file

* Sat Mar 18 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.0.0.20060317-3
- devel package accidently got dropped -- readd it

* Sat Mar 18 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.0.0.20060317-2
- solve the kernel-check in another way

* Sat Mar 18 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.0.0.20060317-1
- madwifi-avoid-kernelpathcheck.diff still needed
- move 20060317 from release to version

* Sat Mar 18 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.lvn.17.20060317
- remove excludearch, otherwise the buildsys trys to build pacakge for athon & co

* Sat Mar 18 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.lvn.16.20060317
- update to 20060317
- build for ppc, too
- drop 0.lvn

* Tue Feb 28 2006 Andreas Bierfert <andreas.bierfert[AT]lowlatency.de>
- add dist

* Sat Feb 11 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.lvn.15.20060211
- split into packages for userland and kmod

* Sat Feb 11 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.lvn.14.20060128
- Update to madwifi-old-r1417-20060128 (#759)

* Wed Jan 04 2006 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.lvn.13.20050917
- Add a -devel subpackage so that apps like hostapd can be built against it
  (patch from ignacio, #724)

* Sun Dec 18 2005 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.lvn.12.20050917
- Revert to 2005-09-17

* Fri Dec 16 2005 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.lvn.11.20051216
- Update to 2005-12-16

* Sat Dec 03 2005 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.lvn.10.20051130
- Update to 2005-11-30

* Sat Nov 19 2005 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.lvn.9.20051114
- Update to 2005-11-14 from madwifi.org (madwifi-ng)

* Sat Nov 12 2005 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.lvn.8.20051112
- Update to 2005-11-12

* Sat Sep 17 2005 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.lvn.7.20050917
- Update to 2005-09-17

* Wed Jul 20 2005 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.0-0.lvn.6.20050715
- Avoid the check for kernel-patch and kernel-config on i386 if we only build
  userland

* Fri Jul 15 2005 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.0-0.lvn.5.20050715
- Update to 2005-07-15 (after merge of BSD branch)

* Sat Jul 09 2005 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.0-0.lvn.4.20050709
- Update to 2005-07-09
- Support x86_64
- adjust kernel-build stuff to current livna scheme
- drop tools subpackage, just use the name "madwifi"

* Sun Jan 23 2005 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.0-0.lvn.3.20050220
- Update to 2005-02-20
- ExclusivArch %%{ix86} for now
- Build tools also as suggested in #355 my Michael A. Peters 
  <funkyres [AT] gmail [DOT] com>  

* Sun Jan 23 2005 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.0-0.lvn.3.20041229
- Update to 20041229 on recommendation by Gianluca Sforna

* Sun Jan 09 2005 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.0-0.lvn.2.20041127
- BR sharutils (thanks Gianluca Sforna for catching this bug)

* Fri Nov 26 2004 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info> 0.0-0.lvn.1.20041127
- Initial Version
- Applied Ville Skyttä's nameing scheme from bash-completion
- Used cvs-snapshot web-location mentioned on Homepage as source
- Cause of the issue with the included HAL I choosed livna as repo.
   For details on the HAL and its distribution see:
   http://www.mattfoster.clara.co.uk/madwifi-5.htm
