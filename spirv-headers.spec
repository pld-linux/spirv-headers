# (commit 814e728b30ddd0f4509233099a3ad96fd4318c07)
%define		gitref	sdk-1.2.198.0

Summary:	SPIR-V headers
Summary(pl.UTF-8):	Pliki nagłówkowe SPIR-V
Name:		spirv-headers
# see CMakeLists.txt /VERSION or include/spirv/unified1/spirv.h /SPV_VERSION + /SPV_REVISION (whichever is greater)
Version:	1.5.5
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/KhronosGroup/SPIRV-Headers/tags
Source0:	https://github.com/KhronosGroup/SPIRV-Headers/archive/%{gitref}/SPIRV-Headers-%{gitref}.tar.gz
# Source0-md5:	298b70404ee9b6482397125c920d3c6b
URL:		https://github.com/KhronosGroup/SPIRV-Headers
BuildRequires:	cmake >= 3.0
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
install -d build
cd build
%cmake ..

%{__make}

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
