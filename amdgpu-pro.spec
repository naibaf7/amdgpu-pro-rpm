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
%setup -q -n %{name}

%build
#no build

%install
#amdgpu-pro package
mkdir %{name}_%{version}-%{release}_amd64
cd %{name}_%{version}-%{release}_amd64
ar x %{name}_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-clinfo package
mkdir %{name}-clinfo_%{version}-%{release}_amd64
cd %{name}-clinfo_%{version}-%{release}_amd64
ar x %{name}-clinfo_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-computing package
mkdir %{name}-computing_%{version}-%{release}_amd64
cd %{name}-computing_%{version}-%{release}_amd64
ar x %{name}-computing_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-core package
mkdir %{name}-core_%{version}-%{release}_amd64
cd %{name}-core_%{version}-%{release}_amd64
ar x %{name}-core_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz

mv %{buildroot}/lib %{buildroot}%{_prefix}/
mkdir -p %{buildroot}%{_sysconfdir}/ld.so.conf.d/
ln -s %{_prefix}/lib/amdgpu-pro/ld.conf %{buildroot}%{_sysconfdir}/ld.so.conf.d/10-amdgpu-pro.conf
mkdir -p %{buildroot}%{_sysconfdir}/modprobe.d/
ln -s %{_prefix}/lib/amdgpu-pro/modprobe.conf %{buildroot}%{_sysconfdir}/modprobe.d/amdgpu-pro.conf
cd ..

#amdgpu-pro-dkms package
mkdir %{name}-dkms_%{version}-%{release}_all
cd %{name}-dkms_%{version}-%{release}_all
ar x %{name}-dkms_%{version}-%{release}_all.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-graphics package
mkdir %{name}-graphics_%{version}-%{release}_amd64
cd %{name}-graphics_%{version}-%{release}_amd64
ar x %{name}-graphics_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-amdgpu-pro-lib32 package
mkdir %{name}-lib32_%{version}-%{release}_i386
cd %{name}-lib32_%{version}-%{release}_i386
ar x %{name}-lib32_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-amdgpu-pro-libopencl-dev package
mkdir %{name}-libopencl-dev_%{version}-%{release}_i386
cd %{name}-libopencl-dev_%{version}-%{release}_i386
ar x %{name}-libopencl-dev_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-libopencl-dev package
mkdir %{name}-libopencl-dev_%{version}-%{release}_amd64
cd %{name}-libopencl-dev_%{version}-%{release}_amd64
ar x %{name}-libopencl-dev_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-amdgpu-pro-libopencl1 package
mkdir %{name}-libopencl1_%{version}-%{release}_i386
cd %{name}-libopencl1_%{version}-%{release}_i386
ar x %{name}-libopencl1_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-libopencl1 package
mkdir %{name}-libopencl1_%{version}-%{release}_amd64
cd %{name}-libopencl1_%{version}-%{release}_amd64
ar x %{name}-libopencl1_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-amdgpu-pro-opencl-icd package
mkdir %{name}-opencl-icd_%{version}-%{release}_i386
cd %{name}-opencl-icd_%{version}-%{release}_i386
ar x %{name}-opencl-icd_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-opencl-icd package
mkdir %{name}-opencl-icd_%{version}-%{release}_amd64
cd %{name}-opencl-icd_%{version}-%{release}_amd64
ar x %{name}-opencl-icd_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#amdgpu-pro-vulkan-driver package
mkdir %{name}-vulkan-driver_%{version}-%{release}_amd64
cd %{name}-vulkan-driver_%{version}-%{release}_amd64
ar x %{name}-vulkan-driver_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-amdgpu-pro-vulkan-driver package
mkdir %{name}-vulkan-driver_%{version}-%{release}_i386
cd %{name}-vulkan-driver_%{version}-%{release}_i386
ar x %{name}-vulkan-driver_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libdrm-amdgpu-pro-amdgpu1 package
mkdir libdrm-amdgpu-pro-amdgpu1_%{version}-%{release}_amd64
cd libdrm-amdgpu-pro-amdgpu1_%{version}-%{release}_amd64
ar x libdrm-amdgpu-pro-amdgpu1_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libdrm-amdgpu-pro-amdgpu1 package
mkdir libdrm-amdgpu-pro-amdgpu1_%{version}-%{release}_i386
cd libdrm-amdgpu-pro-amdgpu1_%{version}-%{release}_i386
ar x libdrm-amdgpu-pro-amdgpu1_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libdrm-amdgpu-pro-dev package
mkdir libdrm-amdgpu-pro-dev_%{version}-%{release}_i386
cd libdrm-amdgpu-pro-dev_%{version}-%{release}_i386
ar x libdrm-amdgpu-pro-dev_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libdrm-amdgpu-pro-dev package
mkdir libdrm-amdgpu-pro-dev_%{version}-%{release}_amd64
cd libdrm-amdgpu-pro-dev_%{version}-%{release}_amd64
ar x libdrm-amdgpu-pro-dev_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libdrm-amdgpu-pro-tools package
mkdir libdrm-amdgpu-pro-tools_%{version}-%{release}_amd64
cd libdrm-amdgpu-pro-tools_%{version}-%{release}_amd64
ar x libdrm-amdgpu-pro-tools_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libdrm2-amdgpu-pro package
mkdir libdrm2-amdgpu-pro_%{version}-%{release}_amd64
cd libdrm2-amdgpu-pro_%{version}-%{release}_amd64
ar x libdrm2-amdgpu-pro_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libdrm2-amdgpu-pro package
mkdir libdrm2-amdgpu-pro_%{version}-%{release}_i386
cd libdrm2-amdgpu-pro_%{version}-%{release}_i386
ar x libdrm2-amdgpu-pro_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libegl1-amdgpu-pro package
mkdir libegl1-amdgpu-pro_%{version}-%{release}_amd64
cd libegl1-amdgpu-pro_%{version}-%{release}_amd64
ar x libegl1-amdgpu-pro_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libegl1-amdgpu-pro package
mkdir libegl1-amdgpu-pro_%{version}-%{release}_i386
cd libegl1-amdgpu-pro_%{version}-%{release}_i386
ar x libegl1-amdgpu-pro_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libegl1-amdgpu-pro-dev package
mkdir libegl1-amdgpu-pro-dev_%{version}-%{release}_amd64
cd libegl1-amdgpu-pro-dev_%{version}-%{release}_amd64
ar x libegl1-amdgpu-pro-dev_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libegl1-amdgpu-pro-dev package
mkdir libegl1-amdgpu-pro-dev_%{version}-%{release}_i386
cd libegl1-amdgpu-pro-dev_%{version}-%{release}_i386
ar x libegl1-amdgpu-pro-dev_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgbm-amdgpu-pro-dev package
mkdir libgbm-amdgpu-pro-dev_%{version}-%{release}_i386
cd libgbm-amdgpu-pro-dev_%{version}-%{release}_i386
ar x libgbm-amdgpu-pro-dev_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgbm-amdgpu-pro-dev package
mkdir libgbm-amdgpu-pro-dev_%{version}-%{release}_amd64
cd libgbm-amdgpu-pro-dev_%{version}-%{release}_amd64
ar x libgbm-amdgpu-pro-dev_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgbm1-amdgpu-pro package
mkdir libgbm1-amdgpu-pro_%{version}-%{release}_i386
cd libgbm1-amdgpu-pro_%{version}-%{release}_i386
ar x libgbm1-amdgpu-pro_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgbm1-amdgpu-pro package
mkdir libgbm1-amdgpu-pro_%{version}-%{release}_amd64
cd libgbm1-amdgpu-pro_%{version}-%{release}_amd64
ar x libgbm1-amdgpu-pro_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgl1-amdgpu-pro-dev package
mkdir libgl1-amdgpu-pro-dev_%{version}-%{release}_amd64
cd libgl1-amdgpu-pro-dev_%{version}-%{release}_amd64
ar x libgl1-amdgpu-pro-dev_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgl1-amdgpu-pro-dev package
mkdir libgl1-amdgpu-pro-dev_%{version}-%{release}_i386
cd libgl1-amdgpu-pro-dev_%{version}-%{release}_i386
ar x libgl1-amdgpu-pro-dev_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgl1-amdgpu-pro-dri package
mkdir libgl1-amdgpu-pro-dri_%{version}-%{release}_amd64
cd libgl1-amdgpu-pro-dri_%{version}-%{release}_amd64
ar x libgl1-amdgpu-pro-dri_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgl1-amdgpu-pro-dri package
mkdir libgl1-amdgpu-pro-dri_%{version}-%{release}_i386
cd libgl1-amdgpu-pro-dri_%{version}-%{release}_i386
ar x libgl1-amdgpu-pro-dri_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgl1-amdgpu-pro-glx package
mkdir libgl1-amdgpu-pro-glx_%{version}-%{release}_i386
cd libgl1-amdgpu-pro-glx_%{version}-%{release}_i386
ar x libgl1-amdgpu-pro-glx_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgl1-amdgpu-pro-glx package
mkdir libgl1-amdgpu-pro-glx_%{version}-%{release}_amd64
cd libgl1-amdgpu-pro-glx_%{version}-%{release}_amd64
ar x libgl1-amdgpu-pro-glx_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgles2-amdgpu-pro package
mkdir libgles2-amdgpu-pro_%{version}-%{release}_amd64
cd libgles2-amdgpu-pro_%{version}-%{release}_amd64
ar x libgles2-amdgpu-pro_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgles2-amdgpu-pro package
mkdir libgles2-amdgpu-pro_%{version}-%{release}_i386
cd libgles2-amdgpu-pro_%{version}-%{release}_i386
ar x libgles2-amdgpu-pro_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libgles2-amdgpu-pro-dev package
mkdir libgles2-amdgpu-pro-dev_%{version}-%{release}_amd64
cd libgles2-amdgpu-pro-dev_%{version}-%{release}_amd64
ar x libgles2-amdgpu-pro-dev_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libgles2-amdgpu-pro-dev package
mkdir libgles2-amdgpu-pro-dev_%{version}-%{release}_i386
cd libgles2-amdgpu-pro-dev_%{version}-%{release}_i386
ar x libgles2-amdgpu-pro-dev_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#libvdpau-amdgpu-pro package
mkdir libvdpau-amdgpu-pro_%{version}-%{release}_amd64
cd libvdpau-amdgpu-pro_%{version}-%{release}_amd64
ar x libvdpau-amdgpu-pro_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#lib32-libvdpau-amdgpu-pro package
mkdir libvdpau-amdgpu-pro_%{version}-%{release}_i386
cd libvdpau-amdgpu-pro_%{version}-%{release}_i386
ar x libvdpau-amdgpu-pro_%{version}-%{release}_i386.deb
tar -C %{buildroot} -xf data.tar.xz
cd ..

#xserver-xorg-video-amdgpu-pro package
mkdir xserver-xorg-video-amdgpu-pro_%{version}-%{release}_amd64
cd xserver-xorg-video-amdgpu-pro_%{version}-%{release}_amd64
ar x xserver-xorg-video-amdgpu-pro_%{version}-%{release}_amd64.deb
tar -C %{buildroot} -xf data.tar.xz
ln -sfn 1.18 ${pkgdir}%{_prefix}/lib/x86_64-linux-gnu/amdgpu-pro/xorg

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%files
%{_prefix}/*
%config(noreplace) %{_sysconfdir}/*

%changelog
