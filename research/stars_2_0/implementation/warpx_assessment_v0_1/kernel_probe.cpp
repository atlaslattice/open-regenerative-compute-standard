// Calls the unchanged pinned WarpX cross-section header in a scalar CPU harness.
// This is NOT a build or execution of the full WarpX PIC application.
#include <iostream>
#include <iomanip>
#include <cmath>
#include "Particles/Collision/BinaryCollision/NuclearFusion/ProtonBoronFusionCrossSection.H"
int main() {
  double E_keV;
  std::cout << std::setprecision(17);
  while(std::cin >> E_keV) {
    if(!std::isfinite(E_keV) || E_keV<0) return 2;
    std::cout << E_keV << " " << ProtonBoronFusionCrossSection(E_keV*1000*PhysConst::q_e) << "\n";
  }
}
