Name:           mimic
Summary:        tts
Version:        newest
Release:        1
License:        BSD
Source0:        %{name}-%{version}.tar.gz 
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  python, portaudio-devel
%define _unpackaged_files_terminate_build 0

%description

%prep
%setup -q


%build
./configure
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
rm -rf /usr/lib/debug/


%clean
make clean
rm -rf $RPM_BUILD_ROOT


%files
/usr/local/bin/mimic
%defattr(-,root,root,-)
