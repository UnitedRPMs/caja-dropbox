#
# spec file for package caja-dropbox
#
# Copyright (c) 2020 UnitedRPMs.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 1.24

Summary: 		Dropbox extension for caja
Name: 			caja-dropbox
Version: 		1.24.0
Release: 		7%{?dist}
License: 		GPLv2+
Group:			User Interface/Desktops
URL: 			http://git.mate-desktop.org/%{name}
Source0: 		http://pub.mate-desktop.org/releases/%{branch}/%{name}-%{version}.tar.xz 

ExclusiveArch:  i686 x86_64

BuildRequires:  caja-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
BuildRequires:  pkgconfig(pygobject-3.0)
BuildRequires:  pygtk2-devel
BuildRequires:	python3-docutils

Requires:       dropbox 
Requires:       caja-extensions
Requires:       pygtk2

%description
Dropbox extension for caja file manager
Dropbox allows you to sync your files online and across
your computers automatically.

%prep
%setup -q

%build
%configure

make %{?_smp_mflags}

%install
%{make_install}

find ${RPM_BUILD_ROOT} -type f -name "*.la" -exec rm -f {} ';'
find ${RPM_BUILD_ROOT} -type f -name "*.a" -exec rm -f {} ';'

rm -rf ${RPM_BUILD_ROOT}%{_bindir}
rm -rf ${RPM_BUILD_ROOT}%{_datadir}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%doc AUTHORS COPYING NEWS README 
%{_libdir}/caja/extensions-2.0/libcaja-dropbox.so


%changelog

* Tue Feb 11 2020 David Va <davidva AT tuta DOT io> - 1.24.0-7
- Updated to 1.24.0

* Thu Apr 25 2019 David Va <davidva AT tutanota DOT com> - 1.22.1-7
- Updated to 1.22.1

* Sat Apr 06 2019 David Va <davidva AT tutanota DOT com> - 1.22.0-7
- Updated to 1.22.0

* Fri Feb 09 2018 David Va <davidva AT tutanota DOT com> - 1.20.0-2
- Updated to 1.20.0

* Mon Jul 03 2017 David Va <davidva AT tutanota DOT com> - 1.18.0-2
- Changed Requires of dropbox, UnitedRPMs does not provides a fool epoch tag of dropbox

* Thu Jun 29 2017 Wolfgang Ulbrich <fedora@raveit.de> - 1.18.0-1
- update to 1.18.0 release

* Sat Mar 25 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.17.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Dec 11 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.17.0-1
- update to 1.17.0 release

* Thu Sep 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.16.0-1
- update to 1.16.0 release

* Thu Aug 11 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.15.0-1
- update to 1.15.0 release

* Sun Jun 19 2016 Leigh Scott <leigh123linux@googlemail.com> - 1.14.0-1
- update to 1.14.0 release

* Sun Nov 15 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Sun Aug 09 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-3
- update to 1.10.0 release

* Sat Jan 10 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.0-3
- add ExclusiveArch

* Sat Dec 20 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.0-2
- use rpmfusion dropbox require
- fix license information
- remove non needed patches

* Fri Oct 10 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.0-1
- switch to mate upstream
- update to 1.8.0 release

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.6.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jul 13 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-6
- bump version to fix build

* Sun Jul 13 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-5
- try use a fake X session to find pygtk2 BR

* Sun Jul 21 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-4
- don't use fake X session for build server
- add script binary with serialize images
- fix pygtk2 configure issue

* Sat Jul 20 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-3
- add exports

* Thu May 16 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-2
- use a fake X session to find pygtk2 BR, fix build server issue
- fix autoconf/automake deprecations

* Sun May 12 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.0-1
- add require hicolor-icon-theme
- remove useless libmatenotify BR
- clean up BR's
- switch to current upstream source
- fix licence information

* Thu Mar 21 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-2
- initial build for fedora

* Fri Nov 16 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-1
- build against official fedora mate-desktop
- remove epoch
- test remove libmate require
- clean BR
- add rpm scriptlets
- improve spec file

* Mon Aug 27 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-0100
- build for f18

* Thu Jul 05 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-4
- switch to Mate-Desktop source

* Thu Feb 23 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-3
- fixed build error for i686

* Mon Feb 13 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-2
- rebuild for enable builds for .i686

* Thu Jan 19 2012 Wolfgang Ulbrich <chat-to-me@raveit.de> - 0.7.1-1
- start building for caja   

