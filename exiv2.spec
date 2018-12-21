#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : exiv2
Version  : 0.27
Release  : 15
URL      : https://github.com/Exiv2/exiv2/archive/0.27.tar.gz
Source0  : https://github.com/Exiv2/exiv2/archive/0.27.tar.gz
Summary  : @PROJECT_DESCRIPTION@
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: exiv2-bin = %{version}-%{release}
Requires: exiv2-data = %{version}-%{release}
Requires: exiv2-lib = %{version}-%{release}
Requires: exiv2-license = %{version}-%{release}
Requires: exiv2-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : expat-dev
BuildRequires : gettext-dev
BuildRequires : glibc-dev
BuildRequires : googletest-dev
BuildRequires : zlib-dev

%description
organize uses the Boost library (http://www.boost.org).
Configuration settings for Boost are in the file boost.mk
in this directory and should be changed as required.

%package bin
Summary: bin components for the exiv2 package.
Group: Binaries
Requires: exiv2-data = %{version}-%{release}
Requires: exiv2-license = %{version}-%{release}
Requires: exiv2-man = %{version}-%{release}

%description bin
bin components for the exiv2 package.


%package data
Summary: data components for the exiv2 package.
Group: Data

%description data
data components for the exiv2 package.


%package dev
Summary: dev components for the exiv2 package.
Group: Development
Requires: exiv2-lib = %{version}-%{release}
Requires: exiv2-bin = %{version}-%{release}
Requires: exiv2-data = %{version}-%{release}
Provides: exiv2-devel = %{version}-%{release}

%description dev
dev components for the exiv2 package.


%package lib
Summary: lib components for the exiv2 package.
Group: Libraries
Requires: exiv2-data = %{version}-%{release}
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
%setup -q -n exiv2-0.27

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545425477
mkdir -p clr-build
pushd clr-build
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1545425477
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/exiv2
cp COPYING %{buildroot}/usr/share/package-licenses/exiv2/COPYING
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/exiv2/COPYING-CMAKE-SCRIPTS
cp doc/COPYING-XMPSDK %{buildroot}/usr/share/package-licenses/exiv2/doc_COPYING-XMPSDK
cp license.txt %{buildroot}/usr/share/package-licenses/exiv2/license.txt
cp test/data/COPYRIGHT %{buildroot}/usr/share/package-licenses/exiv2/test_data_COPYRIGHT
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/addmoddel
/usr/bin/convert-test
/usr/bin/easyaccess-test
/usr/bin/exifcomment
/usr/bin/exifdata
/usr/bin/exifdata-test
/usr/bin/exifprint
/usr/bin/exifvalue
/usr/bin/exiv2
/usr/bin/exiv2json
/usr/bin/geotag
/usr/bin/ini-test
/usr/bin/iotest
/usr/bin/iptceasy
/usr/bin/iptcprint
/usr/bin/iptctest
/usr/bin/key-test
/usr/bin/largeiptc-test
/usr/bin/metacopy
/usr/bin/mmap-test
/usr/bin/mrwthumb
/usr/bin/path-test
/usr/bin/prevtest
/usr/bin/stringto-test
/usr/bin/taglist
/usr/bin/tiff-test
/usr/bin/werror-test
/usr/bin/write-test
/usr/bin/write2-test
/usr/bin/xmpdump
/usr/bin/xmpparse
/usr/bin/xmpparser-test
/usr/bin/xmpprint
/usr/bin/xmpsample

%files data
%defattr(-,root,root,-)
/usr/share/exiv2/cmake/exiv2Config-relwithdebinfo.cmake
/usr/share/exiv2/cmake/exiv2Config.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/exiv2/asfvideo.hpp
/usr/include/exiv2/basicio.hpp
/usr/include/exiv2/bigtiffimage.hpp
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
/usr/include/exiv2/ini.hpp
/usr/include/exiv2/iptc.hpp
/usr/include/exiv2/jp2image.hpp
/usr/include/exiv2/jpgimage.hpp
/usr/include/exiv2/matroskavideo.hpp
/usr/include/exiv2/metadatum.hpp
/usr/include/exiv2/mrwimage.hpp
/usr/include/exiv2/orfimage.hpp
/usr/include/exiv2/pgfimage.hpp
/usr/include/exiv2/pngimage.hpp
/usr/include/exiv2/preview.hpp
/usr/include/exiv2/properties.hpp
/usr/include/exiv2/psdimage.hpp
/usr/include/exiv2/quicktimevideo.hpp
/usr/include/exiv2/rafimage.hpp
/usr/include/exiv2/riffvideo.hpp
/usr/include/exiv2/rw2image.hpp
/usr/include/exiv2/rwlock.hpp
/usr/include/exiv2/slice.hpp
/usr/include/exiv2/ssh.hpp
/usr/include/exiv2/tags.hpp
/usr/include/exiv2/tgaimage.hpp
/usr/include/exiv2/tiffimage.hpp
/usr/include/exiv2/types.hpp
/usr/include/exiv2/utilsvideo.hpp
/usr/include/exiv2/value.hpp
/usr/include/exiv2/version.hpp
/usr/include/exiv2/webpimage.hpp
/usr/include/exiv2/xmp_exiv2.hpp
/usr/include/exiv2/xmpsidecar.hpp
/usr/lib64/libexiv2.so
/usr/lib64/pkgconfig/exiv2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libexiv2.so.0.27.0
/usr/lib64/libexiv2.so.27

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/exiv2/COPYING
/usr/share/package-licenses/exiv2/COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/exiv2/doc_COPYING-XMPSDK
/usr/share/package-licenses/exiv2/license.txt
/usr/share/package-licenses/exiv2/test_data_COPYRIGHT

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/exiv2.1
/usr/share/man/man1/exiv2samples.1
