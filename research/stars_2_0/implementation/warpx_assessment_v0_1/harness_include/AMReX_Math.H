// Assessment-only integer-power shim; no GPU, PIC, particle or mesh implementation.
#pragma once
namespace amrex::Math {
template<int N,typename T> constexpr T powi(T x) {
  if constexpr (N == 0) return T(1);
  else return x*powi<N-1>(x);
}}
