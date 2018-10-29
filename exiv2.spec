#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : exiv2
Version  : 0.26.trunk
Release  : 10
URL      : http://www.exiv2.org/builds/exiv2-0.26-trunk.tar.gz
Source0  : http://www.exiv2.org/builds/exiv2-0.26-trunk.tar.gz
Summary  : Image metadata library and tools
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: exiv2-bin = %{version}-%{release}
Requires: exiv2-lib = %{version}-%{release}
Requires: exiv2-license = %{version}-%{release}
Requires: exiv2-locales = %{version}-%{release}
Requires: exiv2-man = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-configure
BuildRequires : buildreq-qmake
BuildRequires : expat-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : zlib-dev
Patch1: CVE-2017-11683.patch
Patch2: CVE-2017-14860.patch
Patch3: CVE-2017-14864.patch
Patch4: CVE-2017-17669.patch
Patch5: CVE-2017-17723.patch
Patch6: CVE-2017-17725.patch
Patch7: CVE-2018-5772.patch
Patch8: CVE-2018-8976.patch
Patch9: CVE-2018-8977.patch
Patch10: CVE-2018-10958.patch
Patch11: CVE-2018-10998.patch
Patch12: CVE-2018-11531.patch
Patch13: CVE-2018-12264.patch
Patch14: CVE-2018-14046.patch

%description
@@@Marco@@@@@b                   ;mm                       /##Gilles###\
j@@@#Robin",                     Brad                     /@@@Thomas@@@@Q
@@@#       \                     ##                     @@@b     |@@@b
@@@#          .;;;;,     ,;;;, ,;;;;  ,;;;p      .;;;   7@@      ]Alan
@@@#           j@@@@,   ]@@#/  '@@@#  j@@@#      ]@@^           ;@@@"
@@@Andreas@C     "@@@p @@@"     @@@b   j@@@p     @@b           @@@#/
@@@#^7"7%#\       ^@@@@@#~      Benb    1@@@    {@#          s@@@#
@@@#                Niels       @@@b     @@@Q  ]@#         ;@@@#/
@@@#              ,@@##@@m      @@@b      @@@p @@C        #@@#C
@@@#       ,/    s@@#  @@@@     @@@b       Volker       @Tuan@
]@@@Abhinav@@\   /@@@\    \@@@Q  @@@Q       %@@@#      /@@@@Mahesh@@#
/@@Raphael@@@@@\ /@@@@@\     C++  Metadata  Library    /@Sridhar@@@v0.26\

%package bin
Summary: bin components for the exiv2 package.
Group: Binaries
Requires: exiv2-license = %{version}-%{release}
Requires: exiv2-man = %{version}-%{release}

%description bin
bin components for the exiv2 package.


%package dev
Summary: dev components for the exiv2 package.
Group: Development
Requires: exiv2-lib = %{version}-%{release}
Requires: exiv2-bin = %{version}-%{release}
Provides: exiv2-devel = %{version}-%{release}

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


%package locales
Summary: locales components for the exiv2 package.
Group: Default

%description locales
locales components for the exiv2 package.


%package man
Summary: man components for the exiv2 package.
Group: Default

%description man
man components for the exiv2 package.


%prep
%setup -q -n exiv2-trunk
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540842561
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1540842561
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/exiv2
cp COPYING %{buildroot}/usr/share/package-licenses/exiv2/COPYING
cp COPYING-CMAKE-SCRIPTS %{buildroot}/usr/share/package-licenses/exiv2/COPYING-CMAKE-SCRIPTS
cp doc/COPYING-XMPSDK %{buildroot}/usr/share/package-licenses/exiv2/doc_COPYING-XMPSDK
%make_install
%find_lang exiv2

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/exiv2

%files dev
%defattr(-,root,root,-)
/usr/include/exiv2/basicio.hpp
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
/usr/include/exiv2/exv_conf.h
/usr/include/exiv2/exv_msvc.h
/usr/include/exiv2/futils.hpp
/usr/include/exiv2/gifimage.hpp
/usr/include/exiv2/http.hpp
/usr/include/exiv2/image.hpp
/usr/include/exiv2/ini.hpp
/usr/include/exiv2/iptc.hpp
/usr/include/exiv2/jp2image.hpp
/usr/include/exiv2/jpgimage.hpp
/usr/include/exiv2/metadatum.hpp
/usr/include/exiv2/mrwimage.hpp
/usr/include/exiv2/orfimage.hpp
/usr/include/exiv2/pgfimage.hpp
/usr/include/exiv2/pngimage.hpp
/usr/include/exiv2/preview.hpp
/usr/include/exiv2/properties.hpp
/usr/include/exiv2/psdimage.hpp
/usr/include/exiv2/rafimage.hpp
/usr/include/exiv2/rw2image.hpp
/usr/include/exiv2/rwlock.hpp
/usr/include/exiv2/svn_version.h
/usr/include/exiv2/tags.hpp
/usr/include/exiv2/tgaimage.hpp
/usr/include/exiv2/tiffimage.hpp
/usr/include/exiv2/types.hpp
/usr/include/exiv2/value.hpp
/usr/include/exiv2/version.hpp
/usr/include/exiv2/webpimage.hpp
/usr/include/exiv2/xmp.hpp
/usr/include/exiv2/xmpsidecar.hpp
/usr/lib64/libexiv2.so
/usr/lib64/pkgconfig/exiv2.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libexiv2.so.26
/usr/lib64/libexiv2.so.26.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/exiv2/COPYING
/usr/share/package-licenses/exiv2/COPYING-CMAKE-SCRIPTS
/usr/share/package-licenses/exiv2/doc_COPYING-XMPSDK

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/exiv2.1
/usr/share/man/man1/exiv2samples.1

%files locales -f exiv2.lang
%defattr(-,root,root,-)

