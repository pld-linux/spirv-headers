%define		commit	29817199b7069bac971e5365d180295d4b077ebe

Summary:	SPIR-V headers
Summary(pl.UTF-8):	Pliki nagłówkowe SPIR-V
Name:		spirv-headers
Version:	1.5.4
Release:	3
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/KhronosGroup/SPIRV-Headers/releases
Source0:	https://github.com/KhronosGroup/SPIRV-Headers/archive/%{commit}/%{name}-%{commit}.tar.gz
# Source0-md5:	6274b7fbd13c25e42d86126c734a6876
URL:		https://github.com/KhronosGroup/SPIRV-Headers
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
%setup -qn SPIRV-Headers-%{commit}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_includedir}
cp -a include/spirv $RPM_BUILD_ROOT%{_includedir}/spirv

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.md
%{_includedir}/spirv
