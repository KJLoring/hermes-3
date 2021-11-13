#pragma once
#ifndef ELECTRON_FORCE_BALANCE
#define ELECTRON_FORCE_BALANCE

#include "component.hxx"

/// Balance the parallel electron pressure gradient against
/// the electric field. Use this electric field to calculate
/// a force on the other species
///
///   E = (-∇p_e + F) / n_e
///
/// where F is the momentum source for the electrons.
///
/// Then uses this electric field to calculate a force on all
/// ion species.
///
/// Note: This needs to be put after collisions and other
///       components which impose forces on electrons
///
struct ElectronForceBalance : public Component {
  ElectronForceBalance(std::string, Options&, Solver*) {}

  /// Required inputs
  /// - species
  ///   - e
  ///     - pressure
  ///     - density
  ///     - momentum_source [optional]
  ///     Asserts that charge = -1
  ///
  /// Sets in the input
  /// - species
  ///   - <all except e>   if both density and charge are set
  ///     - momentum_source
  /// 
  void transform(Options &state) override;
};

namespace {
RegisterComponent<ElectronForceBalance> registercomponentelectronforcebalance("electron_force_balance");
}

#endif // ELECTRON_FORCE_BALANCE
