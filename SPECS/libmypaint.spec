Name: libmypaint
Version: 1.6.1
Release: 9%{?dist}
Summary: Library for making brush strokes

# Compute some version related macros.
# Ugly, need to get quoting percent signs straight.
%global major %(ver=%{version}; echo ${ver%%%%.*})
%global minor %(ver=%{version}; ver=${ver#%major.}; echo ${ver%%%%.*})
%global micro %(ver=%{version}; ver=${ver#%major.%minor.}; echo ${ver%%%%.*})

License: ISC
URL: https://github.com/mypaint/libmypaint
Source0: https://github.com/mypaint/libmypaint/releases/download/v%{version}/libmypaint-%{version}.tar.xz

BuildRequires: babl-devel
BuildRequires: gcc
BuildRequires: doxygen
BuildRequires: glib2-devel
BuildRequires: gobject-introspection-devel
BuildRequires: intltool
BuildRequires: json-c-devel
BuildRequires: python3-breathe
BuildRequires: python3-sphinx
BuildRequires: make

Conflicts: mypaint < 1.3.0

%description
This is a self-contained library containing the MyPaint brush engine.

%package devel
Summary: Development files for libmypaint
Requires: %{name}%{?isa} = %{?epoch:%{epoch}:}%{version}-%{release}
Requires: pkgconfig
Provides: bundled(fastapprox) = 0.3.2
# rng-double source: https://www-cs-faculty.stanford.edu/~knuth/programs/rng-double.c
Provides: bundled(rng-double)

%description devel
This package contains files needed for development with libmypaint.

%prep
%autosetup -p1

# Make sure the build uses python3
sed -i -e 's/python -c/python3 -c/g' configure

%build
%configure --enable-docs --enable-introspection=yes --disable-gegl
%make_build

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -delete -print

%find_lang %{name}

%ldconfig_scriptlets

%files -f %{name}.lang
%license COPYING
%doc README.md
%{_libdir}/libmypaint.so.0*
%dir %{_libdir}/girepository-1.0
%{_libdir}/girepository-1.0/MyPaint-%{major}.%{minor}.typelib

%files devel
%doc doc/build/*
%{_libdir}/libmypaint.so
%{_includedir}/%{name}
%{_libdir}/pkgconfig/libmypaint.pc
%dir %{_datadir}/gir-1.0
%{_datadir}/gir-1.0/MyPaint-%{major}.%{minor}.gir

%changelog
* Tue Aug 09 2022 Josef Ridky <jridky@redhat.com> - 1.6.1-9
- add provides for rng-double library #2064301

* Wed Mar 16 2022 Josef Ridky <jridky@redhat.com> - 1.6.1-8
- add provides for fastapprox library #2064301

* Wed Feb 09 2022 Josef Ridky <jridky@redhat.com> - 1.6.1-7
- add gating.yaml file

* Thu Jan 20 2022 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Thu Jul 22 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jul 10 2021 Björn Esser <besser82@fedoraproject.org> - 1.6.1-4
- Rebuild for versioned symbols in json-c

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri May 15 2020 Kalev Lember <klember@redhat.com> - 1.6.1-1
- Update to 1.6.1
- Tighten soname globs

* Tue Apr 21 2020 Björn Esser <besser82@fedoraproject.org> - 1.5.0-2
- Rebuild (json-c)

* Wed Feb 19 2020 Kalev Lember <klember@redhat.com> - 1.5.0-1
- Update to 1.5.0

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 29 2019 Kalev Lember <klember@redhat.com> - 1.4.0-2
- Remove previous version ABI compat hack

* Tue Nov 12 2019 Kalev Lember <klember@redhat.com> - 1.4.0-1
- Update to 1.4.0

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 13 2019 Kalev Lember <klember@redhat.com> - 1.3.0-12
- Fix FTBFS with latest gegl04

* Sat Mar 09 2019 Nils Philippsen <nils@tiptoe.de> - 1.3.0-11
- use python3-sphinx, python3-breathe for building documentation

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed May 02 2018 Nils Philippsen <nils@tiptoe.de> - 1.3.0-8
- rebuild with gegl04

* Tue Mar 06 2018 Björn Esser <besser82@fedoraproject.org> - 1.3.0-7
- Rebuilt for libjson-c.so.4 (json-c v0.13.1)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Dec 13 2017 Björn Esser <besser82@fedoraproject.org> - 1.3.0-5
- Rebuilt for libjson-c.so.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Jan 27 2017 Nils Philippsen <nils@tiptoe.de> - 1.3.0-1
- version 1.3.0 final
- conflict with mypaint < 1.3.0
- mention pkgconfig, introspection files explicitly

* Sun Jul 31 2016 Nils Philippsen <nils@tiptoe.de> - 1.3.0-0.2.beta.1
- fix locale names 'ar_AR' -> 'ar'
- fix build dependencies
- fix summary and description texts
- use current build and install macros
- remove all .la files beneath %%_libdir
- ship development documentation

* Sun Jul 31 2016 Nils Philippsen <nils@tiptoe.de> - 1.3.0-0.1.beta.1
- initial release of 1.3.0-beta.1
