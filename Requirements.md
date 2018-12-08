# Geant4 Exacale Proxy Requirements

## Description of the functionality necessary for the Geant Exascale Proxy

The proxy should be a standalone application with a mean to explore various
detector layouts, for example the CMS detector and a Liquid Argon TPC.
It should provide interfaces for configuration and options for transport, event input, and output
and either indirectly or directly include performance measurement tools.

### Configuration interfaces

1. physics lists
2. detector descriptions (eg. GDML)
3. input event types

### Transport Options

- charged particles in uniform electromagnetic field
- realistic electromagnetic field description used in typical HEP experiments
- standard set of electromagnetic physics processes and models required for most of HEP detector simulation, including:
  - Charged particles
    - Ionization
      - Bremsstrahlung
      - Multiple scattering models (electron and positron)
  - Photons
    - Photoelectric Effect
    - Compton Scattering
    - Pair-production
  - Hadronic physics models for:
    - Proton
    - Neutron
    - Pion
    - Kaons
  - Parameterized particle shower simulations

### Event Input

- Particle gun win customizations:
  - number of particles
  - particle types
  - random distributions in energy, eta, phi in given ranges
  - Ability to use HEPevents (for an example, BSM events from PYTHIA) would be a plus

### Output

The proxy should be capable of producing output data representative of a typical HEP experiment, for example
digitized hits (scoring) in sensitive detectors.

### Performance Measurements

The proxy should include (directly or indirectly) the ability to measure:

1. scalabily
2. event throughput
3. memory usage under various configuration settings, including multi-threaded execution

### Additional Notes

An estimate of the date size for input events for a real physics process (for
example Higgs -> ZZ , Z to all decays, O(1000) primary tracks) is in the order
of 10's of kilobytes (for example 32K/event at the LHC energy).   A typical
output rate is in the order of 1.5 MB per event (for simulated data, compared
to about 1MB for the equivalent real data.)
