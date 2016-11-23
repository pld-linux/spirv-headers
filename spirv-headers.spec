
%define commit	bd47a9abaefac00be692eae677daed1b977e625c

Summary:	SPIR-V headers
Name:		spirv-headers
Version:	1.1_rev4
Release:	1
License:	distributable
Group:		Libraries
Source0:	https://github.com/KhronosGroup/SPIRV-Headers/archive/%{commit}/%{name}-%{commit}.tar.gz
# Source0-md5:	73b64fcfb897e1b3c192602b59161360
URL:		https://github.com/KhronosGroup/SPIRV-Headers
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains machine-readable files from the SPIR-V Registry.
This includes:

- Header files for various languages.
- JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.

%prep
%setup -qn SPIRV-Headers-%{commit}

%build

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
