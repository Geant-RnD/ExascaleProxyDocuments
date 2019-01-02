# Proposal for Determining Subset of Particles and Processes

## TiMemory

I have created a library that includes "auto-timers" that start recording on construction and stop recording at destruction.
It needs some extensions to work in this mode (as object timers instead of function timers) that will remove some duplicates,
collapse + display the data better, and factor in processes but here is a selection of the current output from a Geant4 example
(1000 events with `examples/extended/parallel/ThreadsafeScorers`). The timers were attached to each `G4Track` object.

```
> [exe] total execution time  : 10.589 wall,  6.203 user +  0.440 system =  6.643 CPU [sec] ( 62.7%)  (x1 laps)

### this is the start of a "primary particle" tree ###

> [cxx] neutron               :  1.151 wall,  1.146 user +  0.010 system =  1.156 CPU [sec] (100.4%)  (x200 laps)
> [cxx] |_proton              :  0.315 wall,  0.315 user +  0.000 system =  0.315 CPU [sec] ( 99.7%)  (x30 laps)
> [cxx] |_B10                 :  0.121 wall,  0.121 user +  0.000 system =  0.121 CPU [sec] ( 99.6%)  (x24 laps)
> [cxx]   |_proton            :  0.328 wall,  0.327 user +  0.000 system =  0.327 CPU [sec] ( 99.8%)  (x32 laps)
> [cxx]     |_proton          :  0.259 wall,  0.258 user +  0.000 system =  0.258 CPU [sec] ( 99.7%)  (x23 laps)
> [cxx]       |_deuteron      :  0.007 wall,  0.007 user +  0.000 system =  0.007 CPU [sec] ( 99.6%)  (x9 laps)
> [cxx]       |_proton        :  0.039 wall,  0.039 user +  0.000 system =  0.039 CPU [sec] ( 99.7%)  (x5 laps)
> [cxx]     |_deuteron        :  0.004 wall,  0.004 user +  0.000 system =  0.004 CPU [sec] ( 99.9%)  (x6 laps)
> [cxx] |_B11                 :  0.409 wall,  0.407 user +  0.010 system =  0.417 CPU [sec] (102.0%)  (x53 laps)
> [cxx]   |_B11               :  0.108 wall,  0.108 user +  0.000 system =  0.108 CPU [sec] ( 99.7%)  (x27 laps)
> [cxx]     |_B11             :  0.031 wall,  0.031 user +  0.000 system =  0.031 CPU [sec] ( 99.7%)  (x8 laps)
> [cxx]       |_alpha         :  0.019 wall,  0.019 user +  0.000 system =  0.019 CPU [sec] ( 99.9%)  (x16 laps)
> [cxx]       |_B10           :  0.002 wall,  0.002 user +  0.000 system =  0.002 CPU [sec] ( 99.6%)  (x1 laps)
> [cxx]     |_B10             :  0.022 wall,  0.022 user +  0.000 system =  0.022 CPU [sec] (100.0%)  (x4 laps)
> [cxx]   |_alpha             :  0.023 wall,  0.023 user +  0.000 system =  0.023 CPU [sec] ( 99.9%)  (x27 laps)
> [cxx]     |_gamma           :  0.012 wall,  0.012 user +  0.000 system =  0.012 CPU [sec] ( 99.8%)  (x30 laps)
> [cxx]       |_Li7           :  0.002 wall,  0.002 user +  0.000 system =  0.002 CPU [sec] ( 99.1%)  (x25 laps)
> [cxx]   |_B10               :  0.045 wall,  0.045 user +  0.000 system =  0.045 CPU [sec] ( 99.8%)  (x11 laps)
> [cxx]     |_alpha           :  0.021 wall,  0.021 user +  0.000 system =  0.021 CPU [sec] ( 99.9%)  (x25 laps)
> [cxx]   |_deuteron          :  0.002 wall,  0.002 user +  0.000 system =  0.002 CPU [sec] (100.0%)  (x6 laps)
> [cxx] |_alpha               :  0.070 wall,  0.070 user +  0.000 system =  0.070 CPU [sec] ( 99.6%)  (x80 laps)
> [cxx]   |_gamma             :  0.038 wall,  0.038 user +  0.000 system =  0.038 CPU [sec] ( 99.5%)  (x81 laps)
> [cxx]     |_Li7             :  0.008 wall,  0.008 user +  0.000 system =  0.008 CPU [sec] ( 98.6%)  (x78 laps)
> [cxx]   |_e-                :  0.059 wall,  0.059 user +  0.000 system =  0.059 CPU [sec] ( 99.8%)  (x81 laps)
> [cxx]     |_e-              :  0.067 wall,  0.067 user +  0.000 system =  0.067 CPU [sec] ( 99.9%)  (x99 laps)
> [cxx]   |_Li7               :  0.001 wall,  0.001 user +  0.000 system =  0.001 CPU [sec] (100.0%)  (x6 laps)
> [cxx] |_O16                 :  0.063 wall,  0.063 user +  0.000 system =  0.063 CPU [sec] ( 99.7%)  (x3 laps)
> [cxx]   |_O16               :  0.031 wall,  0.031 user +  0.000 system =  0.031 CPU [sec] ( 99.6%)  (x2 laps)
> [cxx] |_deuteron            :  0.005 wall,  0.005 user +  0.000 system =  0.005 CPU [sec] (100.1%)  (x7 laps)

### this is the start of a "primary particle" tree ###

> [cxx] proton                :  0.027 wall,  0.026 user +  0.000 system =  0.026 CPU [sec] ( 98.6%)  (x200 laps)

### this is the start of a "primary particle" tree ###

> [cxx] e-                    :  0.037 wall,  0.037 user +  0.000 system =  0.037 CPU [sec] ( 99.4%)  (x200 laps)
> [cxx] |_gamma               :  0.002 wall,  0.002 user +  0.000 system =  0.002 CPU [sec] ( 99.9%)  (x5 laps)
> [cxx] |_e-                  :  0.002 wall,  0.002 user +  0.000 system =  0.002 CPU [sec] (100.1%)  (x5 laps)

### this is the start of a "primary particle" tree ###

> [cxx] pi-                   :  0.046 wall,  0.046 user +  0.000 system =  0.046 CPU [sec] ( 99.7%)  (x200 laps)
> [cxx] |_anti_nu_mu          :  0.756 wall,  0.754 user +  0.010 system =  0.764 CPU [sec] (101.0%)  (x200 laps)
> [cxx]   |_mu-               :  0.040 wall,  0.040 user +  0.000 system =  0.040 CPU [sec] ( 99.8%)  (x200 laps)
> [cxx]   |_nu_mu             :  0.710 wall,  0.708 user +  0.010 system =  0.718 CPU [sec] (101.1%)  (x200 laps)
> [cxx]     |_anti_nu_e       :  0.700 wall,  0.698 user +  0.010 system =  0.708 CPU [sec] (101.1%)  (x200 laps)
> [cxx]       |_e-            :  1.673 wall,  1.668 user +  0.020 system =  1.688 CPU [sec] (100.9%)  (x2276 laps)
> [cxx]       |_gamma         :  1.041 wall,  1.037 user +  0.020 system =  1.057 CPU [sec] (101.5%)  (x381 laps)

### this is the start of a "primary particle" tree ###

> [cxx] pi+                   :  0.049 wall,  0.049 user +  0.000 system =  0.049 CPU [sec] ( 99.8%)  (x200 laps)
> [cxx] |_nu_mu               :  0.992 wall,  0.988 user +  0.030 system =  1.018 CPU [sec] (102.7%)  (x200 laps)
> [cxx]   |_mu+               :  0.044 wall,  0.044 user +  0.000 system =  0.044 CPU [sec] ( 99.6%)  (x200 laps)
> [cxx]   |_anti_nu_mu        :  0.942 wall,  0.939 user +  0.030 system =  0.969 CPU [sec] (102.8%)  (x200 laps)
> [cxx]     |_nu_e            :  0.932 wall,  0.929 user +  0.030 system =  0.959 CPU [sec] (102.8%)  (x200 laps)
> [cxx]       |_e+            :  0.202 wall,  0.201 user +  0.000 system =  0.201 CPU [sec] ( 99.6%)  (x200 laps)
```

For brevity, I restricted the tree depth to 5. After some modifications, I will be able to collapse the call-tree
results to provide the total time spent for each particle along with associated processes.

### Summary

- `pi+` and `pi-` particle required very little processesing time
  - Resulted in many electrons, photons, and neutrinos requiring a lot of processing time
- `neutron` took a long time to process and produced many particles
  - None of the secondary particles required a lot of processesing time outside of `protons`
- `e-` and `proton` in isolation required little processing time
  - This is in contrast to `e-` and `proton` produced in `pi-` and `neutron` trees, respectively.
    - Further investigation is needed, it may be that in general, primary `e-` and `proton` were too high energy and exiting world too quickly

### Primary Particle Production

```c++
TSPrimaryGeneratorAction::TSPrimaryGeneratorAction()
{
    fGun = new G4ParticleGun(1);

    G4ParticleTable* table = G4ParticleTable::GetParticleTable();
    G4ParticleDefinition* particle
    = table->FindParticle("neutron");

    fGun->SetParticleDefinition(particle);
    fGun->SetParticleEnergy(1.0 * MeV);

    gun_settings.push_back(
        new GunSetting(table->FindParticle("neutron"), 0.1 * keV, 1.0 * MeV));
    gun_settings.push_back(
        new GunSetting(table->FindParticle("proton"), 100.0 * keV, 10.0 * MeV));
    gun_settings.push_back(
        new GunSetting(table->FindParticle("e-"), 100.0 * keV, 1.0 * MeV));
    gun_settings.push_back(
        new GunSetting(table->FindParticle("pi-"), 100.0 * keV, 10.0 * MeV));
    gun_settings.push_back(
        new GunSetting(table->FindParticle("pi+"), 100.0 * keV, 10.0 * MeV));
}

void TSPrimaryGeneratorAction::GeneratePrimaries(G4Event* anEvent)
{
    static TSDetectorConstruction* detector
            = TSDetectorConstruction::Instance();

    G4ThreeVector dir = G4RandomDirection();

    G4ThreeVector pos(
        0.5 * detector->GetWorldDimensions().x() * (G4UniformRand() - 0.5),
        0.5 * detector->GetWorldDimensions().y() * (G4UniformRand() - 0.5),
        -0.25 * detector->GetWorldDimensions().z());

    auto idx = anEvent->GetEventID() % gun_settings.size();
    GunSetting* gun_setting = gun_settings.at(idx);

    fGun->SetParticlePosition(pos);
    fGun->SetParticleMomentumDirection(dir / dir.mag());
    fGun->SetParticleEnergy(gun_setting->GetRandomEnergy());
    fGun->SetParticleDefinition(gun_setting->GetParticle());

    fGun->GeneratePrimaryVertex(anEvent);
}
```

## Usage

With information about the total number of particles produced (i.e. "laps") and the wall time and CPU time, we
gain insight into which particles and processes dominate the transport. From this information, we can make
decisions about which processes and particles to implement in the proxy application. This will result in a
proxy application that best resembles the runtime of a real application -- the phyiscs will be incorrect,
but the runtime should be representative.

### TODO

- Add in "timers" for physics processes
- Process data for statistics

## Full output

```
> [exe] total execution time                                                                  : 10.367 wall,  6.162 user +  0.470 system =  6.632 CPU [sec] ( 64.0%)  (x1 laps)
> [cxx] neutron                                                                               :  0.921 wall,  0.917 user +  0.010 system =  0.927 CPU [sec] (100.7%)  (x200 laps)
> [cxx] |_proton                                                                              :  0.395 wall,  0.394 user +  0.000 system =  0.394 CPU [sec] ( 99.8%)  (x41 laps)
> [cxx]   |_alpha                                                                             :  0.037 wall,  0.037 user +  0.000 system =  0.037 CPU [sec] ( 99.9%)  (x30 laps)
> [cxx]     |_gamma                                                                           :  0.024 wall,  0.024 user +  0.000 system =  0.024 CPU [sec] ( 99.8%)  (x31 laps)
> [cxx]       |_Li7                                                                           :  0.010 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 99.8%)  (x30 laps)
> [cxx]     |_e-                                                                              :  0.069 wall,  0.069 user +  0.010 system =  0.079 CPU [sec] (114.2%)  (x92 laps)
> [cxx]   |_deuteron                                                                          :  0.005 wall,  0.005 user +  0.000 system =  0.005 CPU [sec] (100.0%)  (x6 laps)
> [cxx] |_B11                                                                                 :  0.209 wall,  0.208 user +  0.010 system =  0.218 CPU [sec] (104.6%)  (x44 laps)
> [cxx]   |_B11                                                                               :  0.089 wall,  0.088 user +  0.000 system =  0.088 CPU [sec] ( 99.8%)  (x25 laps)
> [cxx]     |_proton                                                                          :  0.186 wall,  0.186 user +  0.010 system =  0.196 CPU [sec] (105.1%)  (x20 laps)
> [cxx]       |_alpha                                                                         :  0.011 wall,  0.011 user +  0.000 system =  0.011 CPU [sec] ( 99.0%)  (x13 laps)
> [cxx]       |_proton                                                                        :  0.050 wall,  0.050 user +  0.000 system =  0.050 CPU [sec] ( 99.8%)  (x5 laps)
> [cxx]         |_alpha                                                                       :  0.003 wall,  0.003 user +  0.000 system =  0.003 CPU [sec] (100.0%)  (x3 laps)
> [cxx]         |_deuteron                                                                    :  0.001 wall,  0.001 user +  0.000 system =  0.001 CPU [sec] ( 99.3%)  (x1 laps)
> [cxx]       |_deuteron                                                                      :  0.006 wall,  0.006 user +  0.000 system =  0.006 CPU [sec] ( 99.7%)  (x6 laps)
> [cxx]     |_B11                                                                             :  0.016 wall,  0.016 user +  0.000 system =  0.016 CPU [sec] ( 99.6%)  (x7 laps)
> [cxx]       |_B11                                                                           :  0.004 wall,  0.004 user +  0.000 system =  0.004 CPU [sec] ( 99.9%)  (x1 laps)
> [cxx]         |_B10                                                                         :  0.004 wall,  0.004 user +  0.000 system =  0.004 CPU [sec] ( 99.9%)  (x1 laps)
> [cxx]           |_deuteron                                                                  :  0.002 wall,  0.002 user +  0.000 system =  0.002 CPU [sec] ( 99.8%)  (x1 laps)
> [cxx]   |_proton                                                                            :  0.385 wall,  0.384 user +  0.010 system =  0.394 CPU [sec] (102.4%)  (x43 laps)
> [cxx]     |_deuteron                                                                        :  0.005 wall,  0.005 user +  0.000 system =  0.005 CPU [sec] ( 99.0%)  (x4 laps)
> [cxx]   |_B10                                                                               :  0.015 wall,  0.015 user +  0.000 system =  0.015 CPU [sec] ( 99.9%)  (x7 laps)
> [cxx]     |_alpha                                                                           :  0.024 wall,  0.024 user +  0.000 system =  0.024 CPU [sec] ( 99.8%)  (x33 laps)
> [cxx]     |_B10                                                                             :  0.004 wall,  0.004 user +  0.000 system =  0.004 CPU [sec] (100.0%)  (x2 laps)
> [cxx] |_B10                                                                                 :  0.171 wall,  0.171 user +  0.000 system =  0.171 CPU [sec] ( 99.8%)  (x28 laps)
> [cxx] |_alpha                                                                               :  0.065 wall,  0.065 user +  0.010 system =  0.075 CPU [sec] (114.9%)  (x78 laps)
> [cxx]   |_gamma                                                                             :  0.034 wall,  0.034 user +  0.000 system =  0.034 CPU [sec] ( 99.6%)  (x76 laps)
> [cxx]     |_Li7                                                                             :  0.008 wall,  0.008 user +  0.000 system =  0.008 CPU [sec] ( 99.0%)  (x78 laps)
> [cxx]   |_e-                                                                                :  0.050 wall,  0.050 user +  0.010 system =  0.060 CPU [sec] (119.4%)  (x68 laps)
> [cxx]   |_Li7                                                                               :  0.001 wall,  0.001 user +  0.000 system =  0.001 CPU [sec] (100.0%)  (x5 laps)
> [cxx] |_O16                                                                                 :  0.014 wall,  0.014 user +  0.000 system =  0.014 CPU [sec] ( 99.7%)  (x2 laps)
> [cxx] |_deuteron                                                                            :  0.001 wall,  0.001 user +  0.000 system =  0.001 CPU [sec] ( 96.5%)  (x3 laps)
> [cxx] proton                                                                                :  0.025 wall,  0.025 user +  0.000 system =  0.025 CPU [sec] ( 99.8%)  (x200 laps)
> [cxx] e-                                                                                    :  0.034 wall,  0.034 user +  0.000 system =  0.034 CPU [sec] ( 99.7%)  (x200 laps)
> [cxx] |_gamma                                                                               :  0.001 wall,  0.001 user +  0.000 system =  0.001 CPU [sec] ( 99.7%)  (x3 laps)
> [cxx] |_e-                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (100.3%)  (x3 laps)
> [cxx] pi-                                                                                   :  0.046 wall,  0.045 user +  0.000 system =  0.045 CPU [sec] ( 99.5%)  (x200 laps)
> [cxx] |_anti_nu_mu                                                                          :  0.789 wall,  0.787 user +  0.010 system =  0.797 CPU [sec] (100.9%)  (x200 laps)
> [cxx]   |_mu-                                                                               :  0.041 wall,  0.041 user +  0.000 system =  0.041 CPU [sec] ( 99.8%)  (x200 laps)
> [cxx]   |_nu_mu                                                                             :  0.743 wall,  0.740 user +  0.010 system =  0.750 CPU [sec] (101.0%)  (x200 laps)
> [cxx]     |_anti_nu_e                                                                       :  0.733 wall,  0.730 user +  0.010 system =  0.740 CPU [sec] (101.0%)  (x200 laps)
> [cxx]       |_e-                                                                            :  1.019 wall,  1.016 user +  0.040 system =  1.056 CPU [sec] (103.6%)  (x729 laps)
> [cxx]         |_e+                                                                          :  0.001 wall,  0.001 user +  0.000 system =  0.001 CPU [sec] ( 99.8%)  (x4 laps)
> [cxx]       |_gamma                                                                         :  1.022 wall,  1.018 user +  0.020 system =  1.038 CPU [sec] (101.6%)  (x315 laps)
> [cxx]         |_gamma                                                                       :  0.910 wall,  0.906 user +  0.030 system =  0.936 CPU [sec] (102.9%)  (x308 laps)
> [cxx]           |_gamma                                                                     :  0.799 wall,  0.795 user +  0.030 system =  0.825 CPU [sec] (103.4%)  (x294 laps)
> [cxx]             |_e-                                                                      :  0.735 wall,  0.732 user +  0.030 system =  0.762 CPU [sec] (103.7%)  (x934 laps)
> [cxx]               |_e-                                                                    :  0.762 wall,  0.759 user +  0.040 system =  0.799 CPU [sec] (104.9%)  (x960 laps)
> [cxx]                 |_e-                                                                  :  0.653 wall,  0.650 user +  0.030 system =  0.680 CPU [sec] (104.3%)  (x968 laps)
> [cxx]                   |_e-                                                                :  0.596 wall,  0.594 user +  0.020 system =  0.614 CPU [sec] (103.0%)  (x974 laps)
> [cxx]                     |_e-                                                              :  0.547 wall,  0.545 user +  0.020 system =  0.565 CPU [sec] (103.2%)  (x936 laps)
> [cxx]                       |_e-                                                            :  0.501 wall,  0.499 user +  0.030 system =  0.529 CPU [sec] (105.6%)  (x895 laps)
> [cxx]                         |_e-                                                          :  0.442 wall,  0.441 user +  0.030 system =  0.471 CPU [sec] (106.4%)  (x820 laps)
> [cxx]                           |_e-                                                        :  0.399 wall,  0.397 user +  0.030 system =  0.427 CPU [sec] (107.1%)  (x751 laps)
> [cxx]                             |_e-                                                      :  0.339 wall,  0.337 user +  0.030 system =  0.367 CPU [sec] (108.4%)  (x684 laps)
> [cxx]                               |_e-                                                    :  0.292 wall,  0.291 user +  0.020 system =  0.311 CPU [sec] (106.4%)  (x616 laps)
> [cxx]                                 |_e-                                                  :  0.249 wall,  0.248 user +  0.020 system =  0.268 CPU [sec] (107.5%)  (x546 laps)
> [cxx]                                   |_e-                                                :  0.212 wall,  0.211 user +  0.020 system =  0.231 CPU [sec] (108.9%)  (x487 laps)
> [cxx]                                     |_e-                                              :  0.179 wall,  0.178 user +  0.020 system =  0.198 CPU [sec] (110.7%)  (x427 laps)
> [cxx]                                       |_e-                                            :  0.150 wall,  0.149 user +  0.020 system =  0.169 CPU [sec] (113.0%)  (x379 laps)
> [cxx]                                         |_e-                                          :  0.124 wall,  0.123 user +  0.010 system =  0.133 CPU [sec] (107.8%)  (x334 laps)
> [cxx]                                           |_e-                                        :  0.101 wall,  0.101 user +  0.010 system =  0.111 CPU [sec] (109.7%)  (x294 laps)
> [cxx]                                             |_e-                                      :  0.082 wall,  0.082 user +  0.010 system =  0.092 CPU [sec] (112.0%)  (x250 laps)
> [cxx]                                               |_e-                                    :  0.066 wall,  0.065 user +  0.010 system =  0.075 CPU [sec] (115.0%)  (x212 laps)
> [cxx]                                                 |_e-                                  :  0.052 wall,  0.052 user +  0.000 system =  0.052 CPU [sec] ( 99.8%)  (x178 laps)
> [cxx]                                                   |_e-                                :  0.040 wall,  0.040 user +  0.000 system =  0.040 CPU [sec] ( 99.7%)  (x149 laps)
> [cxx]                                                     |_e-                              :  0.030 wall,  0.030 user +  0.000 system =  0.030 CPU [sec] ( 99.7%)  (x125 laps)
> [cxx]                                                       |_e-                            :  0.022 wall,  0.022 user +  0.000 system =  0.022 CPU [sec] ( 99.9%)  (x99 laps)
> [cxx]                                                         |_e-                          :  0.016 wall,  0.016 user +  0.000 system =  0.016 CPU [sec] ( 99.9%)  (x78 laps)
> [cxx]                                                           |_e-                        :  0.011 wall,  0.011 user +  0.000 system =  0.011 CPU [sec] ( 99.9%)  (x57 laps)
> [cxx]                                                             |_e-                      :  0.007 wall,  0.007 user +  0.000 system =  0.007 CPU [sec] (100.0%)  (x45 laps)
> [cxx]                                                               |_e-                    :  0.005 wall,  0.005 user +  0.000 system =  0.005 CPU [sec] (100.0%)  (x30 laps)
> [cxx]                                                                 |_e-                  :  0.003 wall,  0.003 user +  0.000 system =  0.003 CPU [sec] (100.1%)  (x19 laps)
> [cxx]                                                                   |_e-                :  0.002 wall,  0.002 user +  0.000 system =  0.002 CPU [sec] (100.1%)  (x11 laps)
> [cxx]                                                                     |_e-              :  0.001 wall,  0.001 user +  0.000 system =  0.001 CPU [sec] (100.0%)  (x6 laps)
> [cxx]                                                                       |_e-            :  0.001 wall,  0.001 user +  0.000 system =  0.001 CPU [sec] ( 99.8%)  (x5 laps)
> [cxx]                                                                         |_e-          :  0.001 wall,  0.001 user +  0.000 system =  0.001 CPU [sec] (100.2%)  (x3 laps)
> [cxx]                                                                           |_e-        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] ( 99.8%)  (x2 laps)
> [cxx]                                                                             |_e-      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (100.3%)  (x2 laps)
> [cxx]                                                                               |_e-    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (100.0%)  (x1 laps)
> [cxx]                                                                                 |_e-  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (100.8%)  (x1 laps)
> [cxx]                                                         |_gamma                       :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (100.0%)  (x1 laps)
> [cxx]                                   |_gamma                                             :  0.003 wall,  0.003 user +  0.000 system =  0.003 CPU [sec] ( 99.7%)  (x3 laps)
> [cxx]                                     |_gamma                                           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] ( 99.8%)  (x1 laps)
> [cxx]                           |_gamma                                                     :  0.028 wall,  0.028 user +  0.000 system =  0.028 CPU [sec] ( 99.8%)  (x42 laps)
> [cxx]                             |_gamma                                                   :  0.018 wall,  0.018 user +  0.000 system =  0.018 CPU [sec] ( 99.9%)  (x26 laps)
> [cxx]                               |_gamma                                                 :  0.006 wall,  0.006 user +  0.000 system =  0.006 CPU [sec] ( 99.9%)  (x6 laps)
> [cxx]                                 |_gamma                                               :  0.003 wall,  0.003 user +  0.000 system =  0.003 CPU [sec] ( 99.6%)  (x2 laps)
> [cxx]                       |_e+                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (100.0%)  (x1 laps)
> [cxx]                   |_e+                                                                :  0.001 wall,  0.001 user +  0.000 system =  0.001 CPU [sec] (100.0%)  (x1 laps)
> [cxx]                 |_e+                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (100.0%)  (x1 laps)
> [cxx]               |_gamma                                                                 :  0.432 wall,  0.430 user +  0.010 system =  0.440 CPU [sec] (102.0%)  (x222 laps)
> [cxx]                 |_gamma                                                               :  0.384 wall,  0.383 user +  0.030 system =  0.413 CPU [sec] (107.4%)  (x214 laps)
> [cxx]                   |_gamma                                                             :  0.267 wall,  0.265 user +  0.020 system =  0.285 CPU [sec] (107.0%)  (x170 laps)
> [cxx]                     |_gamma                                                           :  0.178 wall,  0.177 user +  0.010 system =  0.187 CPU [sec] (105.3%)  (x135 laps)
> [cxx]                       |_gamma                                                         :  0.117 wall,  0.117 user +  0.010 system =  0.127 CPU [sec] (108.2%)  (x108 laps)
> [cxx]                         |_gamma                                                       :  0.067 wall,  0.067 user +  0.000 system =  0.067 CPU [sec] ( 99.8%)  (x66 laps)
> [cxx]               |_e+                                                                    :  0.001 wall,  0.001 user +  0.000 system =  0.001 CPU [sec] ( 99.9%)  (x3 laps)
> [cxx]             |_gamma                                                                   :  0.633 wall,  0.630 user +  0.020 system =  0.650 CPU [sec] (102.8%)  (x268 laps)
> [cxx]             |_Li7                                                                     :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (100.8%)  (x3 laps)
> [cxx]           |_e-                                                                        :  0.739 wall,  0.737 user +  0.020 system =  0.757 CPU [sec] (102.4%)  (x835 laps)
> [cxx]             |_e+                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (100.0%)  (x1 laps)
> [cxx]           |_Li7                                                                       :  0.001 wall,  0.001 user +  0.000 system =  0.001 CPU [sec] ( 97.3%)  (x13 laps)
> [cxx]         |_e-                                                                          :  0.800 wall,  0.798 user +  0.030 system =  0.828 CPU [sec] (103.4%)  (x705 laps)
> [cxx]           |_e+                                                                        :  0.003 wall,  0.003 user +  0.000 system =  0.003 CPU [sec] ( 98.8%)  (x4 laps)
> [cxx]         |_Li7                                                                         :  0.003 wall,  0.003 user +  0.000 system =  0.003 CPU [sec] ( 99.9%)  (x28 laps)
> [cxx] pi+                                                                                   :  0.049 wall,  0.049 user +  0.000 system =  0.049 CPU [sec] ( 99.5%)  (x200 laps)
> [cxx] |_nu_mu                                                                               :  1.068 wall,  1.064 user +  0.040 system =  1.104 CPU [sec] (103.4%)  (x200 laps)
> [cxx]   |_mu+                                                                               :  0.042 wall,  0.042 user +  0.000 system =  0.042 CPU [sec] ( 99.7%)  (x200 laps)
> [cxx]   |_anti_nu_mu                                                                        :  1.021 wall,  1.017 user +  0.040 system =  1.057 CPU [sec] (103.6%)  (x200 laps)
> [cxx]     |_nu_e                                                                            :  1.011 wall,  1.007 user +  0.040 system =  1.047 CPU [sec] (103.6%)  (x200 laps)
> [cxx]       |_e+                                                                            :  0.213 wall,  0.213 user +  0.000 system =  0.213 CPU [sec] ( 99.7%)  (x200 laps)
```
