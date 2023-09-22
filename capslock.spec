#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
#
Name     : capslock
Version  : 0.1.1
Release  : 1
URL      : https://github.com/google/capslock/archive/refs/tags/v0.1.1.tar.gz
Source0  : https://github.com/google/capslock/archive/refs/tags/v0.1.1.tar.gz
Source1  : http://localhost/cgit/projects/capslock-vendor/snapshot/capslock-vendor-0.1.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: capslock-bin = %{version}-%{release}
Requires: capslock-license = %{version}-%{release}
BuildRequires : buildreq-golang
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Add-install-target-makefile.patch

%description
![capslock](docs/capslock-banner.png)
Capslock is a capability analysis CLI for Go packages that informs users of
which privileged operations a given package can access. This works by
classifying the **capabilities** of Go packages by following transitive calls to privileged
standard library operations.

%package bin
Summary: bin components for the capslock package.
Group: Binaries
Requires: capslock-license = %{version}-%{release}

%description bin
bin components for the capslock package.


%package license
Summary: license components for the capslock package.
Group: Default

%description license
license components for the capslock package.


%prep
%setup -q -n capslock-0.1.1
cd %{_builddir}
tar xf %{_sourcedir}/capslock-vendor-0.1.1.tar.xz
cd %{_builddir}/capslock-0.1.1
mkdir -p ./
cp -r %{_builddir}/capslock-vendor-0.1.1/* %{_builddir}/capslock-0.1.1/./
%patch -P 1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695414544
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
make  %{?_smp_mflags}  -f Makefile


%install
export SOURCE_DATE_EPOCH=1695414544
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/capslock
cp %{_builddir}/capslock-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/capslock/f5a9af6e07091e7c533c6801ff5bf317df4dae28 || :
cp %{_builddir}/capslock-vendor-%{version}/vendor/github.com/google/go-cmp/LICENSE %{buildroot}/usr/share/package-licenses/capslock/7080652cc78cd9855d39e324529a3b5f3745dcd6 || :
cp %{_builddir}/capslock-vendor-%{version}/vendor/golang.org/x/mod/LICENSE %{buildroot}/usr/share/package-licenses/capslock/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/capslock-vendor-%{version}/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/capslock/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/capslock-vendor-%{version}/vendor/golang.org/x/tools/LICENSE %{buildroot}/usr/share/package-licenses/capslock/d6a5f1ecaedd723c325a2063375b3517e808a2b5 || :
cp %{_builddir}/capslock-vendor-%{version}/vendor/google.golang.org/protobuf/LICENSE %{buildroot}/usr/share/package-licenses/capslock/74850a25a5319bdddc0d998eb8926c18bada282b || :
DESTDIR=%{buildroot}/usr/bin/ make install -f Makefile

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/capslock

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/capslock/7080652cc78cd9855d39e324529a3b5f3745dcd6
/usr/share/package-licenses/capslock/74850a25a5319bdddc0d998eb8926c18bada282b
/usr/share/package-licenses/capslock/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/capslock/f5a9af6e07091e7c533c6801ff5bf317df4dae28
