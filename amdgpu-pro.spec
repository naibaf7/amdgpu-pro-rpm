#No debug file
%global debug_package %{nil}

Name:           amdgpu-pro
Version:        16.30.3
Release:        306809
Summary:        AMDGPU-Pro Driver
License:        AMD EULA
URL:            http://www.amd.com
Source0:        https://www2.ati.com/drivers/linux/%{name}_%{version}-%{release}.tar.xz
ExclusiveArch:  x86_64

%description
AMDGPU-Pro Driver

%prep
%setup -q -n %{name}-driver

%build
#no build

%install
#amdgpu-pro package
mkdir %{name}_%{version}-%{release}_amd64
cd %{name}_%{version}-%{release}_amd64
ar x ../%{name}_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-clinfo package
mkdir %{name}-clinfo_%{version}-%{release}_amd64
cd %{name}-clinfo_%{version}-%{release}_amd64
ar x ../%{name}-clinfo_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-computing package
mkdir %{name}-computing_%{version}-%{release}_amd64
cd %{name}-computing_%{version}-%{release}_amd64
ar x ../%{name}-computing_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-core package
mkdir %{name}-core_%{version}-%{release}_amd64
cd %{name}-core_%{version}-%{release}_amd64
ar x ../%{name}-core_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz

mv %{buildroot}/lib %{buildroot}%{_prefix}/
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
ln -s %{_prefix}/lib/%{name}/ld.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/10-%{name}.conf
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d/
ln -s %{_prefix}/lib/%{name}/modprobe.conf %{buildroot}%{_sysconfdir}/modprobe.d/%{name}.conf
cd ..

#amdgpu-pro-dkms package
mkdir %{name}-dkms_%{version}-%{release}_all
cd %{name}-dkms_%{version}-%{release}_all
ar x ../%{name}-dkms_%{version}-%{release}_all.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-graphics package
mkdir %{name}-graphics_%{version}-%{release}_amd64
cd %{name}-graphics_%{version}-%{release}_amd64
ar x ../%{name}-graphics_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-amdgpu-pro-lib32 package
mkdir %{name}-lib32_%{version}-%{release}_i386
cd %{name}-lib32_%{version}-%{release}_i386
ar x ../%{name}-lib32_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-amdgpu-pro-libopencl-dev package
mkdir %{name}-libopencl-dev_%{version}-%{release}_i386
cd %{name}-libopencl-dev_%{version}-%{release}_i386
ar x ../%{name}-libopencl-dev_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-libopencl-dev package
mkdir %{name}-libopencl-dev_%{version}-%{release}_amd64
cd %{name}-libopencl-dev_%{version}-%{release}_amd64
ar x ../%{name}-libopencl-dev_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-amdgpu-pro-libopencl1 package
mkdir %{name}-libopencl1_%{version}-%{release}_i386
cd %{name}-libopencl1_%{version}-%{release}_i386
ar x ../%{name}-libopencl1_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-libopencl1 package
mkdir %{name}-libopencl1_%{version}-%{release}_amd64
cd %{name}-libopencl1_%{version}-%{release}_amd64
ar x ../%{name}-libopencl1_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-amdgpu-pro-opencl-icd package
mkdir %{name}-opencl-icd_%{version}-%{release}_i386
cd %{name}-opencl-icd_%{version}-%{release}_i386
ar x ../%{name}-opencl-icd_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-opencl-icd package
mkdir %{name}-opencl-icd_%{version}-%{release}_amd64
cd %{name}-opencl-icd_%{version}-%{release}_amd64
ar x ../%{name}-opencl-icd_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-vulkan-driver package
mkdir %{name}-vulkan-driver_%{version}-%{release}_amd64
cd %{name}-vulkan-driver_%{version}-%{release}_amd64
ar x ../%{name}-vulkan-driver_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-amdgpu-pro-vulkan-driver package
mkdir %{name}-vulkan-driver_%{version}-%{release}_i386
cd %{name}-vulkan-driver_%{version}-%{release}_i386
ar x ../%{name}-vulkan-driver_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libdrm-amdgpu-pro-amdgpu1 package
mkdir libdrm-%{name}-amdgpu1_%{version}-%{release}_amd64
cd libdrm-%{name}-amdgpu1_%{version}-%{release}_amd64
ar x ../libdrm-%{name}-amdgpu1_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libdrm-amdgpu-pro-amdgpu1 package
mkdir libdrm-%{name}-amdgpu1_%{version}-%{release}_i386
cd libdrm-%{name}-amdgpu1_%{version}-%{release}_i386
ar x ../libdrm-%{name}-amdgpu1_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libdrm-amdgpu-pro-dev package
mkdir libdrm-%{name}-dev_%{version}-%{release}_i386
cd libdrm-%{name}-dev_%{version}-%{release}_i386
ar x ../libdrm-%{name}-dev_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libdrm-amdgpu-pro-dev package
mkdir libdrm-%{name}-dev_%{version}-%{release}_amd64
cd libdrm-%{name}-dev_%{version}-%{release}_amd64
ar x ../libdrm-%{name}-dev_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libdrm-amdgpu-pro-tools package
mkdir libdrm-%{name}-tools_%{version}-%{release}_amd64
cd libdrm-%{name}-tools_%{version}-%{release}_amd64
ar x ../libdrm-%{name}-tools_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libdrm2-amdgpu-pro package
mkdir libdrm2-%{name}_%{version}-%{release}_amd64
cd libdrm2-%{name}_%{version}-%{release}_amd64
ar x ../libdrm2-%{name}_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libdrm2-amdgpu-pro package
mkdir libdrm2-%{name}_%{version}-%{release}_i386
cd libdrm2-%{name}_%{version}-%{release}_i386
ar x ../libdrm2-%{name}_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libegl1-amdgpu-pro package
mkdir libegl1-%{name}_%{version}-%{release}_amd64
cd libegl1-%{name}_%{version}-%{release}_amd64
ar x ../libegl1-%{name}_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libegl1-amdgpu-pro package
mkdir libegl1-%{name}_%{version}-%{release}_i386
cd libegl1-%{name}_%{version}-%{release}_i386
ar x ../libegl1-%{name}_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libegl1-amdgpu-pro-dev package
mkdir libegl1-%{name}-dev_%{version}-%{release}_amd64
cd libegl1-%{name}-dev_%{version}-%{release}_amd64
ar x ../libegl1-%{name}-dev_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libegl1-amdgpu-pro-dev package
mkdir libegl1-%{name}-dev_%{version}-%{release}_i386
cd libegl1-%{name}-dev_%{version}-%{release}_i386
ar x ../libegl1-%{name}-dev_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgbm-amdgpu-pro-dev package
mkdir libgbm-%{name}-dev_%{version}-%{release}_i386
cd libgbm-%{name}-dev_%{version}-%{release}_i386
ar x ../libgbm-%{name}-dev_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgbm-amdgpu-pro-dev package
mkdir libgbm-%{name}-dev_%{version}-%{release}_amd64
cd libgbm-%{name}-dev_%{version}-%{release}_amd64
ar x ../libgbm-%{name}-dev_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgbm1-amdgpu-pro package
mkdir libgbm1-%{name}_%{version}-%{release}_i386
cd libgbm1-%{name}_%{version}-%{release}_i386
ar x ../libgbm1-%{name}_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgbm1-amdgpu-pro package
mkdir libgbm1-%{name}_%{version}-%{release}_amd64
cd libgbm1-%{name}_%{version}-%{release}_amd64
ar x ../libgbm1-%{name}_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgl1-amdgpu-pro-dev package
mkdir libgl1-%{name}-dev_%{version}-%{release}_amd64
cd libgl1-%{name}-dev_%{version}-%{release}_amd64
ar x ../libgl1-%{name}-dev_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgl1-amdgpu-pro-dev package
mkdir libgl1-%{name}-dev_%{version}-%{release}_i386
cd libgl1-%{name}-dev_%{version}-%{release}_i386
ar x ../libgl1-%{name}-dev_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgl1-amdgpu-pro-dri package
mkdir libgl1-%{name}-dri_%{version}-%{release}_amd64
cd libgl1-%{name}-dri_%{version}-%{release}_amd64
ar x ../libgl1-%{name}-dri_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgl1-amdgpu-pro-dri package
mkdir libgl1-%{name}-dri_%{version}-%{release}_i386
cd libgl1-%{name}-dri_%{version}-%{release}_i386
ar x ../libgl1-%{name}-dri_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgl1-amdgpu-pro-glx package
mkdir libgl1-%{name}-glx_%{version}-%{release}_i386
cd libgl1-%{name}-glx_%{version}-%{release}_i386
ar x ../libgl1-%{name}-glx_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgl1-amdgpu-pro-glx package
mkdir libgl1-%{name}-glx_%{version}-%{release}_amd64
cd libgl1-%{name}-glx_%{version}-%{release}_amd64
ar x ../libgl1-%{name}-glx_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgles2-amdgpu-pro package
mkdir libgles2-%{name}_%{version}-%{release}_amd64
cd libgles2-%{name}_%{version}-%{release}_amd64
ar x ../libgles2-%{name}_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgles2-amdgpu-pro package
mkdir libgles2-%{name}_%{version}-%{release}_i386
cd libgles2-%{name}_%{version}-%{release}_i386
ar x ../libgles2-%{name}_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgles2-amdgpu-pro-dev package
mkdir libgles2-%{name}-dev_%{version}-%{release}_amd64
cd libgles2-%{name}-dev_%{version}-%{release}_amd64
ar x ../libgles2-%{name}-dev_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgles2-amdgpu-pro-dev package
mkdir libgles2-%{name}-dev_%{version}-%{release}_i386
cd libgles2-%{name}-dev_%{version}-%{release}_i386
ar x ../libgles2-%{name}-dev_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libvdpau-amdgpu-pro package
mkdir libvdpau-%{name}_%{version}-%{release}_amd64
cd libvdpau-%{name}_%{version}-%{release}_amd64
ar x ../libvdpau-%{name}_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libvdpau-amdgpu-pro package
mkdir libvdpau-%{name}_%{version}-%{release}_i386
cd libvdpau-%{name}_%{version}-%{release}_i386
ar x ../libvdpau-%{name}_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#xserver-xorg-video-amdgpu-pro package
mkdir xserver-xorg-video-%{name}_%{version}-%{release}_amd64
cd xserver-xorg-video-%{name}_%{version}-%{release}_amd64
ar x ../xserver-xorg-video-%{name}_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_bindir}/*
%{_datadir}/%{name}*
%{_datadir}/doc/*
%{_datadir}/initramfs-tools/hooks/*
%{_datadir}/X11/*
%{_mandir}/*
%{_prefix}/lib/*
%{_prefix}/src/*
%{_includedir}/*
%config(noreplace) %{_sysconfdir}/*

%changelog
