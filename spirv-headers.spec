# (commit 2acb319af38d43be3ea76bfabf3998e5281d8d12)
%define		gitref	vulkan-sdk-1.3.290.0

Summary:	SPIR-V headers
Summary(pl.UTF-8):	Pliki nagłówkowe SPIR-V
Name:		spirv-headers
# see CMakeLists.txt /VERSION or include/spirv/unified1/spirv.h /SPV_VERSION + /SPV_REVISION (whichever is greater)
Version:	1.6.1
Release:	4
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/KhronosGroup/SPIRV-Headers/tags
Source0:	https://github.com/KhronosGroup/SPIRV-Headers/archive/%{gitref}/SPIRV-Headers-%{gitref}.tar.gz
# Source0-md5:	e9da8c949d89084b8a0a6b128ca6a30d
URL:		https://github.com/KhronosGroup/SPIRV-Headers
BuildRequires:	cmake >= 3.14
BuildRequires:	rpmbuild(macros) >= 1.605
Conflicts:	spirv-tools-devel < v2016.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains machine-readable files from the SPIR-V Registry.
This includes:
- header files for various languages,
- JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.

%description -l pl.UTF-8
Ten pakiet zawiera czytelne dla maszyny pliki z rejestru SPIR-V.
Obejmują one:
- pliki nagłówkowe dla różnych języków,
- pliki JSON opisujące gramatykę podstawowego zestawu instrukcji
  SPIR-V oraz rozszerzonego zestawu instrukcji GLSL.std.450.

%prep
%setup -qn SPIRV-Headers-%{gitref}

%build
# relative CMAKE_INSTALL_INCLUDEDIR for .pc file
%cmake -B build \
	-DCMAKE_INSTALL_INCLUDEDIR=include

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_includedir}/spirv
%{_datadir}/cmake/SPIRV-Headers
%{_npkgconfigdir}/SPIRV-Headers.pc
