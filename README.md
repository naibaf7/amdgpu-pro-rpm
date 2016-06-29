# amdgpu-pro-rpm
Spec file for building RPM's for amdgpu pro (WIP)

Instructions:
1)Make srpm:
```rpmbuild -bs amdgpu-pro.spec```
2)Build using mock:
```mock rebuild ~/rpmbuild/SPRMS/amdgpu-pro-VERSION.src.rpm```
