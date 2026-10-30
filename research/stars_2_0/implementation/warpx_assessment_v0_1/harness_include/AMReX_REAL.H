// Assessment-only CPU/double type shim. This is NOT the AMReX implementation.
#pragma once
#define AMREX_GPU_HOST_DEVICE
#define AMREX_INLINE inline
namespace amrex {
using Real = double;
using ParticleReal = double;
namespace literals {
constexpr double operator""_prt(long double x) {return static_cast<double>(x);}
constexpr double operator""_prt(unsigned long long x) {return static_cast<double>(x);}
}}
