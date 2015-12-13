%global commit 1563f6f8833d88b7cde399cbf93f35b8b4b81586
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           debruijn
Version:        0.0.0
Release:        0.1.git%{shortcommit}%{?dist}
Summary:        Software for the generation de Bruijn sequences for neuroscience experiments

License:        BSD with advertising
URL:            https://github.com/gkaguirrelab/DeBruijn
Source0:        https://github.com/gkaguirrelab/DeBruijn/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
# https://github.com/gkaguirrelab/DeBruijn/pull/2
Patch0:         0001-add-CMake-definitions.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  fftw-devel

%description
%{summary}.

%prep
%autosetup -n DeBruijn-%{commit}
# drop precompiled binary
rm -f %{name}
mkdir build
chmod -x *

%build
pushd build
  %cmake ..
  %make_build
popd

%install
pushd build
  %make_install
popd

%check
%{buildroot}%{_bindir} -v 3 2

%files
# zbyszek: ignatenkobrain: Yeah, the copying file seems to be wrong. I think the headers are the authorative source.
# zbyszek: I seems to be based on http://webdocs.cs.ualberta.ca/~joe/Theses/HCarchive/conditions.html, which bsd 4-clause.
# zbyszek: The proper name seems to be "BSD with advertising" according to https://fedoraproject.org/wiki/Licensing:Main?rd=Licensing#Good_Licenses.
# https://github.com/gkaguirrelab/DeBruijn/issues/1
#license LICENSE
%{_bindir}/%{name}

%changelog
* Sat Dec 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.0.0-0.1.git1563f6f
- Initial package
