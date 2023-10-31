#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v2
# autospec commit: 250a666
#
%define keepstatic 1
Name     : exiv2
Version  : 0.28.0
Release  : 50
URL      : https://github.com/Exiv2/exiv2/archive/v0.28.0/exiv2-0.28.0.tar.gz
Source0  : https://github.com/Exiv2/exiv2/archive/v0.28.0/exiv2-0.28.0.tar.gz
Summary  : Exif, Iptc and XMP metadata manipulation library and tools
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: exiv2-bin = %{version}-%{release}
Requires: exiv2-lib = %{version}-%{release}
Requires: exiv2-license = %{version}-%{release}
Requires: exiv2-man = %{version}-%{release}
BuildRequires : brotli-dev
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : expat-dev
BuildRequires : gettext-dev
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : inih-dev
BuildRequires : zlib-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Exiv2 is a C++ library and a command line utility to read, write, delete and modify Exif, IPTC, XMP and ICC image metadata.  Exiv2 also features a collection of sample and test command-line programs.  Please be aware that while the program _**exiv2**_ enjoys full support from Team Exiv2, the other programs have been written for test, documentation or development purposes.  You are expected to read the code to discover the specification of programs other than _**exiv2**_.

%package bin
Summary: bin components for the exiv2 package.
Group: Binaries
Requires: exiv2-license = %{version}-%{release}

%description bin
bin components for the exiv2 package.


%package dev
Summary: dev components for the exiv2 package.
Group: Development
Requires: exiv2-lib = %{version}-%{release}
Requires: exiv2-bin = %{version}-%{release}
Provides: exiv2-devel = %{version}-%{release}
Requires: exiv2 = %{version}-%{release}

%description dev
dev components for the exiv2 package.


%package lib
Summary: lib components for the exiv2 package.
Group: Libraries
Requires: exiv2-license = %{version}-%{release}

%description lib
lib components for the exiv2 package.


%package license
Summary: license components for the exiv2 package.
Group: Default

%description license
license components for the exiv2 package.


%package man
Summary: man components for the exiv2 package.
Group: Default

%description man
man components for the exiv2 package.


%prep
%setup -q -n exiv2-0.28.0
cd %{_builddir}/exiv2-0.28.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1698774771
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1698774771
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/exiv2
cp %{_builddir}/exiv2-%{version}/COPYING %{buildroot}/usr/share/package-licenses/exiv2/be0b40ce8f9532b75966a20d14af123d3c6b05aa || :
cp %{_builddir}/exiv2-%{version}/doc/COPYING-XMPSDK %{buildroot}/usr/share/package-licenses/exiv2/e70d36a2ced771e55c1c902dd740bf95013ce59c || :
cp %{_builddir}/exiv2-%{version}/test/data/COPYRIGHT %{buildroot}/usr/share/package-licenses/exiv2/e24a9903abce58262de5ec8c9a4b54247c89191a || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/exiv2
/usr/bin/exiv2

%files dev
%defattr(-,root,root,-)
/usr/include/exiv2/asfvideo.hpp
/usr/include/exiv2/basicio.hpp
/usr/include/exiv2/bmffimage.hpp
/usr/include/exiv2/bmpimage.hpp
/usr/include/exiv2/config.h
/usr/include/exiv2/convert.hpp
/usr/include/exiv2/cr2image.hpp
/usr/include/exiv2/crwimage.hpp
/usr/include/exiv2/datasets.hpp
/usr/include/exiv2/easyaccess.hpp
/usr/include/exiv2/epsimage.hpp
/usr/include/exiv2/error.hpp
/usr/include/exiv2/exif.hpp
/usr/include/exiv2/exiv2.hpp
/usr/include/exiv2/exiv2lib_export.h
/usr/include/exiv2/exv_conf.h
/usr/include/exiv2/futils.hpp
/usr/include/exiv2/gifimage.hpp
/usr/include/exiv2/http.hpp
/usr/include/exiv2/image.hpp
/usr/include/exiv2/image_types.hpp
/usr/include/exiv2/iptc.hpp
/usr/include/exiv2/jp2image.hpp
/usr/include/exiv2/jpgimage.hpp
/usr/include/exiv2/matroskavideo.hpp
/usr/include/exiv2/metadatum.hpp
/usr/include/exiv2/mrwimage.hpp
/usr/include/exiv2/orfimage.hpp
/usr/include/exiv2/pgfimage.hpp
/usr/include/exiv2/photoshop.hpp
/usr/include/exiv2/pngimage.hpp
/usr/include/exiv2/preview.hpp
/usr/include/exiv2/properties.hpp
/usr/include/exiv2/psdimage.hpp
/usr/include/exiv2/quicktimevideo.hpp
/usr/include/exiv2/rafimage.hpp
/usr/include/exiv2/riffvideo.hpp
/usr/include/exiv2/rw2image.hpp
/usr/include/exiv2/slice.hpp
/usr/include/exiv2/tags.hpp
/usr/include/exiv2/tgaimage.hpp
/usr/include/exiv2/tiffimage.hpp
/usr/include/exiv2/types.hpp
/usr/include/exiv2/value.hpp
/usr/include/exiv2/version.hpp
/usr/include/exiv2/webpimage.hpp
/usr/include/exiv2/xmp_exiv2.hpp
/usr/include/exiv2/xmpsidecar.hpp
/usr/lib64/cmake/exiv2/exiv2Config-relwithdebinfo.cmake
/usr/lib64/cmake/exiv2/exiv2Config.cmake
/usr/lib64/cmake/exiv2/exiv2ConfigVersion.cmake
/usr/lib64/libexiv2.so
/usr/lib64/pkgconfig/exiv2.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libexiv2.so.0.28.0
/usr/lib64/libexiv2.so.0.28.0
/usr/lib64/libexiv2.so.28

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/exiv2/be0b40ce8f9532b75966a20d14af123d3c6b05aa
/usr/share/package-licenses/exiv2/e24a9903abce58262de5ec8c9a4b54247c89191a
/usr/share/package-licenses/exiv2/e70d36a2ced771e55c1c902dd740bf95013ce59c

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/exiv2.1
