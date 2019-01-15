# Proposal for Determining Subset of Particles and Processes

## TiMemory

I have created a library that includes "auto-timers" that start recording on construction and stop recording at destruction.
It needs some extensions to work in this mode (as object timers instead of function timers) that will remove some duplicates,
collapse + display the data better, and factor in processes but here is a selection of the current output from a Geant4 example
(1000 events with `examples/extended/parallel/ThreadsafeScorers`). The timers were attached to each `G4Track` object.

```
> [exe] total execution time               : 22.586 wall, 19.130 user +  2.850 system = 21.980 CPU [sec] ( 97.3%)  (x1 laps)

### this is the start of a "primary particle" tree ###

> [cxx] |_neutron                          :  1.388 wall,  1.210 user +  0.100 system =  1.310 CPU [sec] ( 94.4%)  (x200 laps)
> [cxx]   |_[StepLimiter_neutron]          :  0.007 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3846 laps)
> [cxx]   |_[hadElastic_neutron]           :  0.054 wall,  0.050 user +  0.010 system =  0.060 CPU [sec] (110.9%)  (x4207 laps)
> [cxx]   |_[nFission_neutron]             :  0.006 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2779 laps)
> [cxx]   |_[nCapture_neutron]             :  0.015 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 67.8%)  (x2784 laps)
> [cxx]   |_[neutronInelastic_neutron]     :  0.019 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2835 laps)
> [cxx]   |_[Decay_neutron]                :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2779 laps)
> [cxx]   |_[Transportation_neutron]       :  0.024 wall,  0.030 user +  0.000 system =  0.030 CPU [sec] (123.6%)  (x11116 laps)
> [cxx]     |_proton                       :  0.450 wall,  0.380 user +  0.070 system =  0.450 CPU [sec] (100.1%)  (x41 laps)
> [cxx]     |_[StepLimiter_neutron]        :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2220 laps)
> [cxx]     |_[hadElastic_neutron]         :  0.050 wall,  0.050 user +  0.010 system =  0.060 CPU [sec] (120.3%)  (x3200 laps)
> [cxx]     |_[nFission_neutron]           :  0.004 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] (554.5%)  (x1868 laps)
> [cxx]     |_[nCapture_neutron]           :  0.014 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] (143.9%)  (x1882 laps)
> [cxx]     |_[neutronInelastic_neutron]   :  0.014 wall,  0.010 user +  0.010 system =  0.020 CPU [sec] (145.8%)  (x1892 laps)
> [cxx]     |_[Decay_neutron]              :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1868 laps)
> [cxx]     |_[Transportation_neutron]     :  0.016 wall,  0.040 user +  0.000 system =  0.040 CPU [sec] (253.6%)  (x7472 laps)
> [cxx]   |_[StepLimiter_Li7]              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x46 laps)
> [cxx]   |_[ionInelastic_Li7]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x46 laps)
> [cxx]   |_[ionElastic_Li7]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x46 laps)
> [cxx]   |_[RadioactiveDecay_Li7]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x94 laps)
> [cxx]   |_[ionIoni_Li7]                  :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x138 laps)
> [cxx]   |_[Transportation_Li7]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x184 laps)
> [cxx]   |_[nuclearStopping_Li7]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x92 laps)
> [cxx]   |_[msc_Li7]                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x92 laps)
> [cxx]   |_[Rayl_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x87 laps)
> [cxx]   |_[conv_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x87 laps)
> [cxx]   |_[compt_gamma]                  :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x113 laps)
> [cxx]   |_[phot_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x87 laps)
> [cxx]   |_[Transportation_gamma]         :  0.001 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (1338.7%)  (x348 laps)
> [cxx]   |_[StepLimiter_alpha]            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x24 laps)
> [cxx]   |_[alphaInelastic_alpha]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x24 laps)
> [cxx]   |_[hadElastic_alpha]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x24 laps)
> [cxx]   |_[ionIoni_alpha]                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x72 laps)
> [cxx]   |_[Transportation_alpha]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x96 laps)
> [cxx]   |_[nuclearStopping_alpha]        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x48 laps)
> [cxx]   |_[msc_alpha]                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x48 laps)
> [cxx]   |_[StepLimiter_proton]           :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1322 laps)
> [cxx]   |_[hadElastic_proton]            :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1322 laps)
> [cxx]   |_[protonInelastic_proton]       :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1322 laps)
> [cxx]   |_[CoulombScat_proton]           :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1322 laps)
> [cxx]   |_[hPairProd_proton]             :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1322 laps)
> [cxx]   |_[hBrems_proton]                :  0.003 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (391.1%)  (x1322 laps)
> [cxx]   |_[hIoni_proton]                 :  0.009 wall,  0.010 user +  0.010 system =  0.020 CPU [sec] (210.7%)  (x3966 laps)
> [cxx]   |_[Transportation_proton]        :  0.012 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x5288 laps)
> [cxx]   |_[msc_proton]                   :  0.008 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (132.9%)  (x2644 laps)

### this is the start of a "primary particle" tree ###

> [cxx] |_proton                           :  0.201 wall,  0.200 user +  0.010 system =  0.210 CPU [sec] (104.3%)  (x200 laps)

### this is the start of a "primary particle" tree ###

> [cxx] |_e-                               :  0.316 wall,  0.360 user +  0.030 system =  0.390 CPU [sec] (123.6%)  (x200 laps)
> [cxx]   |_[StepLimiter_e-]               :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2264 laps)
> [cxx]   |_[CoulombScat_e-]               :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2264 laps)
> [cxx]   |_[ePairProd_e-]                 :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2264 laps)
> [cxx]   |_[eBrem_e-]                     :  0.005 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (215.6%)  (x2266 laps)
> [cxx]   |_[eIoni_e-]                     :  0.015 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 65.7%)  (x6792 laps)
> [cxx]   |_[Transportation_e-]            :  0.018 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x9056 laps)
> [cxx]   |_[msc_e-]                       :  0.014 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4528 laps)

### this is the start of a "primary particle" tree ###

> [cxx] |_pi-                              :  0.443 wall,  0.410 user +  0.060 system =  0.470 CPU [sec] (106.1%)  (x200 laps)
> [cxx]   |_[StepLimiter_pi-]              :  0.005 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (204.0%)  (x2557 laps)
> [cxx]   |_[hadElastic_pi-]               :  0.005 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (184.2%)  (x2557 laps)
> [cxx]   |_[pi-Inelastic_pi-]             :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2557 laps)
> [cxx]   |_[Decay_pi-]                    :  0.008 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (126.8%)  (x2957 laps)
> [cxx]   |_[CoulombScat_pi-]              :  0.005 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] (397.7%)  (x2557 laps)
> [cxx]   |_[hPairProd_pi-]                :  0.005 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (201.8%)  (x2557 laps)
> [cxx]   |_[hBrems_pi-]                   :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2557 laps)
> [cxx]   |_[hIoni_pi-]                    :  0.017 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] ( 57.8%)  (x7671 laps)
> [cxx]   |_[Transportation_pi-]           :  0.021 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x10228 laps)
> [cxx]   |_[msc_pi-]                      :  0.013 wall,  0.010 user +  0.010 system =  0.020 CPU [sec] (154.4%)  (x5114 laps)
> [cxx]     |_anti_nu_mu                   :  7.197 wall,  6.230 user +  0.930 system =  7.160 CPU [sec] ( 99.5%)  (x200 laps)
> [cxx]   |_[StepLimiter_mu-]              :  0.004 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (223.3%)  (x2489 laps)
> [cxx]   |_[Decay_mu-]                    :  0.007 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (133.9%)  (x2889 laps)
> [cxx]   |_[CoulombScat_mu-]              :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2489 laps)
> [cxx]   |_[muPairProd_mu-]               :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2489 laps)
> [cxx]   |_[muBrems_mu-]                  :  0.005 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (213.5%)  (x2489 laps)
> [cxx]   |_[muIoni_mu-]                   :  0.017 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x7467 laps)
> [cxx]   |_[Transportation_mu-]           :  0.019 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 51.6%)  (x9956 laps)
> [cxx]   |_[msc_mu-]                      :  0.012 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 81.9%)  (x4978 laps)
> [cxx]     |_nu_mu                        :  6.776 wall,  5.850 user +  0.870 system =  6.720 CPU [sec] ( 99.2%)  (x200 laps)
> [cxx]     |_[StepLimiter_e-]             :  0.136 wall,  0.090 user +  0.020 system =  0.110 CPU [sec] ( 80.7%)  (x76348 laps)
> [cxx]     |_[CoulombScat_e-]             :  0.134 wall,  0.100 user +  0.060 system =  0.160 CPU [sec] (119.5%)  (x75902 laps)
> [cxx]     |_[ePairProd_e-]               :  0.140 wall,  0.100 user +  0.050 system =  0.150 CPU [sec] (106.9%)  (x75902 laps)
> [cxx]     |_[eBrem_e-]                   :  0.154 wall,  0.090 user +  0.060 system =  0.150 CPU [sec] ( 97.3%)  (x76970 laps)
> [cxx]     |_[eIoni_e-]                   :  0.478 wall,  0.370 user +  0.100 system =  0.470 CPU [sec] ( 98.3%)  (x228293 laps)
> [cxx]     |_[Transportation_e-]          :  0.582 wall,  0.440 user +  0.180 system =  0.620 CPU [sec] (106.5%)  (x303608 laps)
> [cxx]     |_[msc_e-]                     :  0.407 wall,  0.370 user +  0.190 system =  0.560 CPU [sec] (137.4%)  (x151804 laps)
> [cxx]     |_[Rayl_gamma]                 :  0.041 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] ( 49.1%)  (x20665 laps)
> [cxx]     |_[conv_gamma]                 :  0.038 wall,  0.010 user +  0.030 system =  0.040 CPU [sec] (106.1%)  (x19971 laps)
> [cxx]     |_[compt_gamma]                :  0.118 wall,  0.160 user +  0.040 system =  0.200 CPU [sec] (168.8%)  (x30334 laps)
> [cxx]     |_[phot_gamma]                 :  0.050 wall,  0.040 user +  0.030 system =  0.070 CPU [sec] (140.3%)  (x21294 laps)
> [cxx]     |_[Transportation_gamma]       :  0.166 wall,  0.150 user +  0.020 system =  0.170 CPU [sec] (102.3%)  (x79804 laps)
> [cxx]     |_[Transportation_anti_nu_e]   :  0.009 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3640 laps)
> [cxx]     |_[Transportation_nu_mu]       :  0.008 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3784 laps)
> [cxx]   |_[Transportation_anti_nu_mu]    :  0.008 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3588 laps)

### this is the start of a "primary particle" tree ###

> [cxx] |_pi+                              :  0.443 wall,  0.340 user +  0.070 system =  0.410 CPU [sec] ( 92.5%)  (x200 laps)
> [cxx]   |_[StepLimiter_pi+]              :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2540 laps)
> [cxx]   |_[hadElastic_pi+]               :  0.006 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2540 laps)
> [cxx]   |_[pi+Inelastic_pi+]             :  0.006 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2540 laps)
> [cxx]   |_[Decay_pi+]                    :  0.008 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (126.8%)  (x2940 laps)
> [cxx]   |_[CoulombScat_pi+]              :  0.005 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (200.8%)  (x2540 laps)
> [cxx]   |_[hPairProd_pi+]                :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2540 laps)
> [cxx]   |_[hBrems_pi+]                   :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2540 laps)
> [cxx]   |_[hIoni_pi+]                    :  0.018 wall,  0.030 user +  0.010 system =  0.040 CPU [sec] (225.4%)  (x7620 laps)
> [cxx]   |_[Transportation_pi+]           :  0.020 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 48.9%)  (x10160 laps)
> [cxx]   |_[msc_pi+]                      :  0.013 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] (150.2%)  (x5080 laps)
> [cxx]     |_nu_mu                        :  8.263 wall,  7.260 user +  1.070 system =  8.330 CPU [sec] (100.8%)  (x200 laps)
> [cxx]   |_[StepLimiter_mu+]              :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2570 laps)
> [cxx]   |_[Decay_mu+]                    :  0.008 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (133.0%)  (x2970 laps)
> [cxx]   |_[CoulombScat_mu+]              :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2570 laps)
> [cxx]   |_[muPairProd_mu+]               :  0.005 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (202.0%)  (x2570 laps)
> [cxx]   |_[muBrems_mu+]                  :  0.005 wall,  0.000 user +  0.020 system =  0.020 CPU [sec] (419.4%)  (x2570 laps)
> [cxx]   |_[muIoni_mu+]                   :  0.017 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 58.7%)  (x7710 laps)
> [cxx]   |_[Transportation_mu+]           :  0.020 wall,  0.010 user +  0.010 system =  0.020 CPU [sec] (101.4%)  (x10280 laps)
> [cxx]   |_[msc_mu+]                      :  0.013 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] (159.7%)  (x5140 laps)
> [cxx]     |_anti_nu_mu                   :  7.837 wall,  6.830 user +  0.980 system =  7.810 CPU [sec] ( 99.7%)  (x200 laps)
> [cxx]     |_[StepLimiter_e+]             :  0.027 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 36.8%)  (x15285 laps)
> [cxx]     |_[CoulombScat_e+]             :  0.027 wall,  0.030 user +  0.020 system =  0.050 CPU [sec] (188.2%)  (x14870 laps)
> [cxx]     |_[annihil_e+]                 :  0.028 wall,  0.020 user +  0.010 system =  0.030 CPU [sec] (106.5%)  (x15250 laps)
> [cxx]     |_[ePairProd_e+]               :  0.028 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 36.3%)  (x14870 laps)
> [cxx]     |_[eBrem_e+]                   :  0.032 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 31.0%)  (x15634 laps)
> [cxx]     |_[eIoni_e+]                   :  0.097 wall,  0.050 user +  0.010 system =  0.060 CPU [sec] ( 61.7%)  (x45015 laps)
> [cxx]     |_[Transportation_e+]          :  0.115 wall,  0.050 user +  0.070 system =  0.120 CPU [sec] (104.1%)  (x59480 laps)
> [cxx]     |_[msc_e+]                     :  0.083 wall,  0.090 user +  0.040 system =  0.130 CPU [sec] (157.4%)  (x29740 laps)
> [cxx]     |_[Transportation_nu_e]        :  0.008 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (122.2%)  (x3508 laps)
> [cxx]     |_[Transportation_anti_nu_mu]  :  0.008 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (118.4%)  (x3592 laps)
> [cxx]   |_[Transportation_nu_mu]         :  0.008 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3704 laps)
> [cxx]     |_e-                           :  0.127 wall,  0.090 user +  0.040 system =  0.130 CPU [sec] (102.4%)  (x26 laps)
> [cxx]     |_[Rayl_gamma]                 :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x285 laps)
> [cxx]     |_[conv_gamma]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x279 laps)
> [cxx]     |_[compt_gamma]                :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x424 laps)
> [cxx]     |_[phot_gamma]                 :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x285 laps)
> [cxx]     |_[Transportation_gamma]       :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1116 laps)
> [cxx]     |_[StepLimiter_e-]             :  0.001 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (793.0%)  (x749 laps)
> [cxx]     |_[CoulombScat_e-]             :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x749 laps)
> [cxx]     |_[ePairProd_e-]               :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x749 laps)
> [cxx]     |_[eBrem_e-]                   :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x749 laps)
> [cxx]     |_[eIoni_e-]                   :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2247 laps)
> [cxx]     |_[Transportation_e-]          :  0.006 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (175.2%)  (x2996 laps)
> [cxx]     |_[msc_e-]                     :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1498 laps)
> [cxx]   |_[StepLimiter_deuteron]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x14 laps)
> [cxx]   |_[dInelastic_deuteron]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x14 laps)
> [cxx]   |_[hadElastic_deuteron]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x14 laps)
> [cxx]   |_[hIoni_deuteron]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x42 laps)
> [cxx]   |_[Transportation_deuteron]      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x56 laps)
> [cxx]   |_[nuclearStopping_deuteron]     :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x28 laps)
> [cxx]   |_[msc_deuteron]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x28 laps)
> [cxx]     |_B10                          :  0.353 wall,  0.320 user +  0.020 system =  0.340 CPU [sec] ( 96.3%)  (x27 laps)
> [cxx]     |_[StepLimiter_neutron]        :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2225 laps)
> [cxx]     |_[hadElastic_neutron]         :  0.041 wall,  0.070 user +  0.000 system =  0.070 CPU [sec] (172.4%)  (x2904 laps)
> [cxx]     |_[nFission_neutron]           :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1754 laps)
> [cxx]     |_[nCapture_neutron]           :  0.011 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1758 laps)
> [cxx]     |_[neutronInelastic_neutron]   :  0.011 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] (177.9%)  (x1771 laps)
> [cxx]     |_[Decay_neutron]              :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1754 laps)
> [cxx]     |_[Transportation_neutron]     :  0.015 wall,  0.010 user +  0.010 system =  0.020 CPU [sec] (134.2%)  (x7016 laps)
> [cxx]   |_[StepLimiter_Li7]              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x31 laps)
> [cxx]   |_[ionInelastic_Li7]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x31 laps)
> [cxx]   |_[ionElastic_Li7]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x31 laps)
> [cxx]   |_[RadioactiveDecay_Li7]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x65 laps)
> [cxx]   |_[ionIoni_Li7]                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x93 laps)
> [cxx]   |_[Transportation_Li7]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x124 laps)
> [cxx]   |_[nuclearStopping_Li7]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x62 laps)
> [cxx]   |_[msc_Li7]                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x62 laps)
> [cxx]   |_[Rayl_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x46 laps)
> [cxx]   |_[conv_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x46 laps)
> [cxx]   |_[compt_gamma]                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x61 laps)
> [cxx]   |_[phot_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x46 laps)
> [cxx]   |_[Transportation_gamma]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x184 laps)
> [cxx]     |_e-                           :  0.075 wall,  0.060 user +  0.000 system =  0.060 CPU [sec] ( 79.7%)  (x15 laps)
> [cxx]     |_[Rayl_gamma]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x203 laps)
> [cxx]     |_[conv_gamma]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x198 laps)
> [cxx]     |_[compt_gamma]                :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x316 laps)
> [cxx]     |_[phot_gamma]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x204 laps)
> [cxx]     |_[Transportation_gamma]       :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x792 laps)
> [cxx]     |_[StepLimiter_e-]             :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x419 laps)
> [cxx]     |_[CoulombScat_e-]             :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x419 laps)
> [cxx]     |_[ePairProd_e-]               :  0.001 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (1261.0%)  (x419 laps)
> [cxx]     |_[eBrem_e-]                   :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x419 laps)
> [cxx]     |_[eIoni_e-]                   :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1257 laps)
> [cxx]     |_[Transportation_e-]          :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1676 laps)
> [cxx]     |_[msc_e-]                     :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x838 laps)
> [cxx]   |_[StepLimiter_alpha]            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x17 laps)
> [cxx]   |_[alphaInelastic_alpha]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x17 laps)
> [cxx]   |_[hadElastic_alpha]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x17 laps)
> [cxx]   |_[ionIoni_alpha]                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x51 laps)
> [cxx]   |_[Transportation_alpha]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x68 laps)
> [cxx]   |_[nuclearStopping_alpha]        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x34 laps)
> [cxx]   |_[msc_alpha]                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x34 laps)
> [cxx]   |_[StepLimiter_B10]              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x33 laps)
> [cxx]   |_[ionInelastic_B10]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x33 laps)
> [cxx]   |_[ionElastic_B10]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x33 laps)
> [cxx]   |_[RadioactiveDecay_B10]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x99 laps)
> [cxx]   |_[ionIoni_B10]                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x99 laps)
> [cxx]   |_[Transportation_B10]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x132 laps)
> [cxx]   |_[nuclearStopping_B10]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x66 laps)
> [cxx]   |_[msc_B10]                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x66 laps)
> [cxx]     |_B11                          :  0.847 wall,  0.740 user +  0.070 system =  0.810 CPU [sec] ( 95.6%)  (x64 laps)
> [cxx]     |_[StepLimiter_neutron]        :  0.007 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4086 laps)
> [cxx]     |_[hadElastic_neutron]         :  0.066 wall,  0.070 user +  0.000 system =  0.070 CPU [sec] (105.7%)  (x4938 laps)
> [cxx]     |_[nFission_neutron]           :  0.006 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3110 laps)
> [cxx]     |_[nCapture_neutron]           :  0.018 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3123 laps)
> [cxx]     |_[neutronInelastic_neutron]   :  0.021 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] ( 93.1%)  (x3160 laps)
> [cxx]     |_[Decay_neutron]              :  0.005 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (185.4%)  (x3110 laps)
> [cxx]     |_[Transportation_neutron]     :  0.026 wall,  0.030 user +  0.010 system =  0.040 CPU [sec] (153.6%)  (x12440 laps)
> [cxx]   |_[StepLimiter_Li7]              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x91 laps)
> [cxx]   |_[ionInelastic_Li7]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x91 laps)
> [cxx]   |_[ionElastic_Li7]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x91 laps)
> [cxx]   |_[RadioactiveDecay_Li7]         :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x191 laps)
> [cxx]   |_[ionIoni_Li7]                  :  0.001 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (895.3%)  (x273 laps)
> [cxx]   |_[Transportation_Li7]           :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x364 laps)
> [cxx]   |_[nuclearStopping_Li7]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x182 laps)
> [cxx]   |_[msc_Li7]                      :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x182 laps)
> [cxx]   |_[Rayl_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x114 laps)
> [cxx]   |_[conv_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x113 laps)
> [cxx]   |_[compt_gamma]                  :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x165 laps)
> [cxx]   |_[phot_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x113 laps)
> [cxx]   |_[Transportation_gamma]         :  0.001 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (939.0%)  (x452 laps)
> [cxx]     |_e-                           :  0.329 wall,  0.260 user +  0.030 system =  0.290 CPU [sec] ( 88.1%)  (x52 laps)
> [cxx]     |_[Rayl_gamma]                 :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x811 laps)
> [cxx]     |_[conv_gamma]                 :  0.001 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (668.0%)  (x788 laps)
> [cxx]     |_[compt_gamma]                :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1236 laps)
> [cxx]     |_[phot_gamma]                 :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x813 laps)
> [cxx]     |_[Transportation_gamma]       :  0.007 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3152 laps)
> [cxx]     |_[StepLimiter_e-]             :  0.003 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (307.1%)  (x1810 laps)
> [cxx]     |_[CoulombScat_e-]             :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1810 laps)
> [cxx]     |_[ePairProd_e-]               :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1810 laps)
> [cxx]     |_[eBrem_e-]                   :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1810 laps)
> [cxx]     |_[eIoni_e-]                   :  0.012 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x5430 laps)
> [cxx]     |_[Transportation_e-]          :  0.014 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] (140.0%)  (x7240 laps)
> [cxx]     |_[msc_e-]                     :  0.010 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 97.8%)  (x3620 laps)
> [cxx]   |_[StepLimiter_alpha]            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x50 laps)
> [cxx]   |_[alphaInelastic_alpha]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x50 laps)
> [cxx]   |_[hadElastic_alpha]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x50 laps)
> [cxx]   |_[ionIoni_alpha]                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x150 laps)
> [cxx]   |_[Transportation_alpha]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x200 laps)
> [cxx]   |_[nuclearStopping_alpha]        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x100 laps)
> [cxx]   |_[msc_alpha]                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x100 laps)
> [cxx]   |_[StepLimiter_proton]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x67 laps)
> [cxx]   |_[hadElastic_proton]            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x67 laps)
> [cxx]   |_[protonInelastic_proton]       :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x67 laps)
> [cxx]   |_[CoulombScat_proton]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x67 laps)
> [cxx]   |_[hPairProd_proton]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x67 laps)
> [cxx]   |_[hBrems_proton]                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x67 laps)
> [cxx]   |_[hIoni_proton]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x201 laps)
> [cxx]   |_[Transportation_proton]        :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x268 laps)
> [cxx]   |_[msc_proton]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x134 laps)
> [cxx]   |_[StepLimiter_B10]              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x14 laps)
> [cxx]   |_[ionInelastic_B10]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x14 laps)
> [cxx]   |_[ionElastic_B10]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x14 laps)
> [cxx]   |_[RadioactiveDecay_B10]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x42 laps)
> [cxx]   |_[ionIoni_B10]                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x42 laps)
> [cxx]   |_[Transportation_B10]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x56 laps)
> [cxx]   |_[nuclearStopping_B10]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x28 laps)
> [cxx]   |_[msc_B10]                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x28 laps)
> [cxx]   |_[StepLimiter_B11]              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x95 laps)
> [cxx]   |_[ionInelastic_B11]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x95 laps)
> [cxx]   |_[ionElastic_B11]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x95 laps)
> [cxx]   |_[RadioactiveDecay_B11]         :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x285 laps)
> [cxx]   |_[ionIoni_B11]                  :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x285 laps)
> [cxx]   |_[Transportation_B11]           :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x380 laps)
> [cxx]   |_[nuclearStopping_B11]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x190 laps)
> [cxx]   |_[msc_B11]                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x190 laps)
> [cxx]   |_[StepLimiter_deuteron]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x13 laps)
> [cxx]   |_[dInelastic_deuteron]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x13 laps)
> [cxx]   |_[hadElastic_deuteron]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x13 laps)
> [cxx]   |_[hIoni_deuteron]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x39 laps)
> [cxx]   |_[Transportation_deuteron]      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x52 laps)
> [cxx]   |_[nuclearStopping_deuteron]     :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x26 laps)
> [cxx]   |_[msc_deuteron]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x26 laps)
> [cxx]     |_alpha                        :  0.309 wall,  0.240 user +  0.030 system =  0.270 CPU [sec] ( 87.5%)  (x56 laps)
> [cxx]   |_[StepLimiter_Li7]              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x105 laps)
> [cxx]   |_[ionInelastic_Li7]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x105 laps)
> [cxx]   |_[ionElastic_Li7]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x105 laps)
> [cxx]   |_[RadioactiveDecay_Li7]         :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x217 laps)
> [cxx]   |_[ionIoni_Li7]                  :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x315 laps)
> [cxx]   |_[Transportation_Li7]           :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x420 laps)
> [cxx]   |_[nuclearStopping_Li7]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x210 laps)
> [cxx]   |_[msc_Li7]                      :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x210 laps)
> [cxx]   |_[Rayl_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x98 laps)
> [cxx]   |_[conv_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x98 laps)
> [cxx]   |_[compt_gamma]                  :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x146 laps)
> [cxx]   |_[phot_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x99 laps)
> [cxx]   |_[Transportation_gamma]         :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x392 laps)
> [cxx]     |_e-                           :  0.269 wall,  0.180 user +  0.030 system =  0.210 CPU [sec] ( 78.0%)  (x48 laps)
> [cxx]     |_[Rayl_gamma]                 :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x735 laps)
> [cxx]     |_[conv_gamma]                 :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x711 laps)
> [cxx]     |_[compt_gamma]                :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1104 laps)
> [cxx]     |_[phot_gamma]                 :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x737 laps)
> [cxx]     |_[Transportation_gamma]       :  0.006 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2844 laps)
> [cxx]     |_[StepLimiter_e-]             :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1483 laps)
> [cxx]     |_[CoulombScat_e-]             :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1483 laps)
> [cxx]     |_[ePairProd_e-]               :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1483 laps)
> [cxx]     |_[eBrem_e-]                   :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1485 laps)
> [cxx]     |_[eIoni_e-]                   :  0.009 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (109.8%)  (x4449 laps)
> [cxx]     |_[Transportation_e-]          :  0.011 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] (181.2%)  (x5932 laps)
> [cxx]     |_[msc_e-]                     :  0.008 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2966 laps)
> [cxx]   |_[StepLimiter_alpha]            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x56 laps)
> [cxx]   |_[alphaInelastic_alpha]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x56 laps)
> [cxx]   |_[hadElastic_alpha]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x56 laps)
> [cxx]   |_[ionIoni_alpha]                :  0.000 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (2475.2%)  (x168 laps)
> [cxx]   |_[Transportation_alpha]         :  0.000 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (2222.2%)  (x224 laps)
> [cxx]   |_[nuclearStopping_alpha]        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x112 laps)
> [cxx]   |_[msc_alpha]                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x112 laps)
> [cxx]     |_O16                          :  0.043 wall,  0.040 user +  0.000 system =  0.040 CPU [sec] ( 92.4%)  (x4 laps)
> [cxx]     |_[StepLimiter_neutron]        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x152 laps)
> [cxx]     |_[hadElastic_neutron]         :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x152 laps)
> [cxx]     |_[nFission_neutron]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x107 laps)
> [cxx]     |_[nCapture_neutron]           :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x107 laps)
> [cxx]     |_[neutronInelastic_neutron]   :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x111 laps)
> [cxx]     |_[Decay_neutron]              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x107 laps)
> [cxx]     |_[Transportation_neutron]     :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x428 laps)
> [cxx]   |_[StepLimiter_Li7]              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]   |_[ionInelastic_Li7]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]   |_[ionElastic_Li7]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]   |_[RadioactiveDecay_Li7]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x16 laps)
> [cxx]   |_[ionIoni_Li7]                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x24 laps)
> [cxx]   |_[Transportation_Li7]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x32 laps)
> [cxx]   |_[nuclearStopping_Li7]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x16 laps)
> [cxx]   |_[msc_Li7]                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x16 laps)
> [cxx]   |_[Rayl_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x7 laps)
> [cxx]   |_[conv_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x7 laps)
> [cxx]   |_[compt_gamma]                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x11 laps)
> [cxx]   |_[phot_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x7 laps)
> [cxx]   |_[Transportation_gamma]         :  0.000 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (19607.8%)  (x28 laps)
> [cxx]     |_e-                           :  0.021 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] ( 93.6%)  (x4 laps)
> [cxx]     |_[Rayl_gamma]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x53 laps)
> [cxx]     |_[conv_gamma]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x53 laps)
> [cxx]     |_[compt_gamma]                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x75 laps)
> [cxx]     |_[phot_gamma]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x55 laps)
> [cxx]     |_[Transportation_gamma]       :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x212 laps)
> [cxx]     |_[StepLimiter_e-]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x119 laps)
> [cxx]     |_[CoulombScat_e-]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x119 laps)
> [cxx]     |_[ePairProd_e-]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x119 laps)
> [cxx]     |_[eBrem_e-]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x119 laps)
> [cxx]     |_[eIoni_e-]                   :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x357 laps)
> [cxx]     |_[Transportation_e-]          :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x476 laps)
> [cxx]     |_[msc_e-]                     :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x238 laps)
> [cxx]   |_[StepLimiter_alpha]            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]   |_[alphaInelastic_alpha]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]   |_[hadElastic_alpha]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]   |_[ionIoni_alpha]                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x12 laps)
> [cxx]   |_[Transportation_alpha]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x16 laps)
> [cxx]   |_[nuclearStopping_alpha]        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]   |_[msc_alpha]                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]   |_[StepLimiter_proton]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x13 laps)
> [cxx]   |_[hadElastic_proton]            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x13 laps)
> [cxx]   |_[protonInelastic_proton]       :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x13 laps)
> [cxx]   |_[CoulombScat_proton]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x13 laps)
> [cxx]   |_[hPairProd_proton]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x13 laps)
> [cxx]   |_[hBrems_proton]                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x13 laps)
> [cxx]   |_[hIoni_proton]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x39 laps)
> [cxx]   |_[Transportation_proton]        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x52 laps)
> [cxx]   |_[msc_proton]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x26 laps)
> [cxx]   |_[StepLimiter_O16]              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x7 laps)
> [cxx]   |_[ionInelastic_O16]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x7 laps)
> [cxx]   |_[ionElastic_O16]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x7 laps)
> [cxx]   |_[RadioactiveDecay_O16]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x15 laps)
> [cxx]   |_[ionIoni_O16]                  :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x21 laps)
> [cxx]   |_[Transportation_O16]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x28 laps)
> [cxx]   |_[nuclearStopping_O16]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x14 laps)
> [cxx]   |_[msc_O16]                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x14 laps)
> [cxx]   |_[StepLimiter_proton]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x27 laps)
> [cxx]   |_[hadElastic_proton]            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x27 laps)
> [cxx]   |_[protonInelastic_proton]       :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x27 laps)
> [cxx]   |_[CoulombScat_proton]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x27 laps)
> [cxx]   |_[hPairProd_proton]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x27 laps)
> [cxx]   |_[hBrems_proton]                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x27 laps)
> [cxx]   |_[hIoni_proton]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x81 laps)
> [cxx]   |_[Transportation_proton]        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x108 laps)
> [cxx]   |_[msc_proton]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x54 laps)
> [cxx]   |_[StepLimiter_O16]              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]   |_[ionInelastic_O16]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]   |_[ionElastic_O16]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]   |_[RadioactiveDecay_O16]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]   |_[ionIoni_O16]                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]   |_[Transportation_O16]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]   |_[nuclearStopping_O16]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]   |_[msc_O16]                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]     |_deuteron                     :  0.041 wall,  0.030 user +  0.000 system =  0.030 CPU [sec] ( 73.8%)  (x5 laps)
> [cxx]   |_[Rayl_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x9 laps)
> [cxx]   |_[conv_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x9 laps)
> [cxx]   |_[compt_gamma]                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x13 laps)
> [cxx]   |_[phot_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x9 laps)
> [cxx]   |_[Transportation_gamma]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x36 laps)
> [cxx]     |_e-                           :  0.038 wall,  0.030 user +  0.000 system =  0.030 CPU [sec] ( 78.2%)  (x4 laps)
> [cxx]     |_[Rayl_gamma]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x58 laps)
> [cxx]     |_[conv_gamma]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x57 laps)
> [cxx]     |_[compt_gamma]                :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x89 laps)
> [cxx]     |_[phot_gamma]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x58 laps)
> [cxx]     |_[Transportation_gamma]       :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x228 laps)
> [cxx]     |_[StepLimiter_e-]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x216 laps)
> [cxx]     |_[CoulombScat_e-]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x216 laps)
> [cxx]     |_[ePairProd_e-]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x216 laps)
> [cxx]     |_[eBrem_e-]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x216 laps)
> [cxx]     |_[eIoni_e-]                   :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x648 laps)
> [cxx]     |_[Transportation_e-]          :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x864 laps)
> [cxx]     |_[msc_e-]                     :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x432 laps)
> [cxx]   |_[StepLimiter_deuteron]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x5 laps)
> [cxx]   |_[dInelastic_deuteron]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x5 laps)
> [cxx]   |_[hadElastic_deuteron]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x5 laps)
> [cxx]   |_[hIoni_deuteron]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x15 laps)
> [cxx]   |_[Transportation_deuteron]      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x20 laps)
> [cxx]   |_[nuclearStopping_deuteron]     :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x10 laps)
> [cxx]   |_[msc_deuteron]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x10 laps)
> [cxx]     |_gamma                        :  0.005 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (197.5%)  (x2 laps)
> [cxx]     |_[StepLimiter_e-]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x24 laps)
> [cxx]     |_[CoulombScat_e-]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x24 laps)
> [cxx]     |_[ePairProd_e-]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x24 laps)
> [cxx]     |_[eBrem_e-]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x24 laps)
> [cxx]     |_[eIoni_e-]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x72 laps)
> [cxx]     |_[Transportation_e-]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x96 laps)
> [cxx]     |_[msc_e-]                     :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x48 laps)
> [cxx]   |_[Rayl_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]   |_[conv_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]   |_[compt_gamma]                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]   |_[phot_gamma]                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]   |_[Transportation_gamma]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x12 laps)
> [cxx]     |_e-                           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1 laps)
> [cxx]   |_[StepLimiter_B11]              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x10 laps)
> [cxx]   |_[ionInelastic_B11]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x10 laps)
> [cxx]   |_[ionElastic_B11]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x10 laps)
> [cxx]   |_[RadioactiveDecay_B11]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x30 laps)
> [cxx]   |_[ionIoni_B11]                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x30 laps)
> [cxx]   |_[Transportation_B11]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x40 laps)
> [cxx]   |_[nuclearStopping_B11]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x20 laps)
> [cxx]   |_[msc_B11]                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x20 laps)
> [cxx]     |_e-                           :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1 laps)
> [cxx]   |_[StepLimiter_deuteron]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]   |_[dInelastic_deuteron]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]   |_[hadElastic_deuteron]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]   |_[hIoni_deuteron]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x12 laps)
> [cxx]   |_[Transportation_deuteron]      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x16 laps)
> [cxx]   |_[nuclearStopping_deuteron]     :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]   |_[msc_deuteron]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]     |_e-                           :  0.004 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (257.4%)  (x1 laps)
> [cxx]     |_[Rayl_gamma]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x10 laps)
> [cxx]     |_[conv_gamma]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x9 laps)
> [cxx]     |_[compt_gamma]                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x14 laps)
> [cxx]     |_[phot_gamma]                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x9 laps)
> [cxx]     |_[Transportation_gamma]       :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x36 laps)
> [cxx]   |_[StepLimiter_B11]              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1 laps)
> [cxx]   |_[ionInelastic_B11]             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1 laps)
> [cxx]   |_[ionElastic_B11]               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1 laps)
> [cxx]   |_[RadioactiveDecay_B11]         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]   |_[ionIoni_B11]                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]   |_[Transportation_B11]           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]   |_[nuclearStopping_B11]          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]   |_[msc_B11]                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
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

## Accumulated Data

- 10000 events

```
e-                             :: wall     =   334.20, sys      =    88.97, user     =   333.68, cpu      =   422.65, perc     =  9819.15, , laps =   159460
gamma                          :: wall     =   193.58, sys      =    52.30, user     =   193.26, cpu      =   245.56, perc     =  3508.09, , laps =    23679
nu_mu                          :: wall     =    71.52, sys      =    19.36, user     =    71.41, cpu      =    90.77, perc     =   353.64, , laps =     3998
anti_nu_mu                     :: wall     =    71.48, sys      =    19.24, user     =    71.37, cpu      =    90.61, perc     =   408.11, , laps =     3998
nu_e                           :: wall     =    38.69, sys      =    10.61, user     =    38.63, cpu      =    49.24, perc     =   282.36, , laps =     2000
anti_nu_e                      :: wall     =    30.39, sys      =     7.99, user     =    30.34, cpu      =    38.33, perc     =   226.14, , laps =     1998
e+                             :: wall     =    10.55, sys      =     2.96, user     =    10.53, cpu      =    13.49, perc     =  1900.41, , laps =     2177
proton                         :: wall     =     8.28, sys      =     1.87, user     =     8.27, cpu      =    10.14, perc     =  1108.65, , laps =     2988
Transportation_e-              :: wall     =     7.45, sys      =     2.26, user     =     7.43, cpu      =     9.69, perc     =  7123.20, , laps =  3223760
neutron                        :: wall     =     7.30, sys      =     1.41, user     =     7.28, cpu      =     8.69, perc     =   737.53, , laps =     2007
eIoni_e-                       :: wall     =     5.95, sys      =     1.43, user     =     5.94, cpu      =     7.37, perc     =  5783.96, , laps =  2423469
B11                            :: wall     =     5.00, sys      =     0.95, user     =     4.99, cpu      =     5.94, perc     =   674.59, , laps =      835
msc_e-                         :: wall     =     4.50, sys      =     1.16, user     =     4.50, cpu      =     5.66, perc     =  5717.43, , laps =  1611880
alpha                          :: wall     =     4.22, sys      =     1.09, user     =     4.22, cpu      =     5.31, perc     =   926.64, , laps =     1522
Transportation_gamma           :: wall     =     2.17, sys      =     0.73, user     =     2.17, cpu      =     2.90, perc     =  6168.92, , laps =   902476
pi+                            :: wall     =     2.15, sys      =     0.55, user     =     2.14, cpu      =     2.69, perc     =   125.46, , laps =     2000
pi-                            :: wall     =     2.06, sys      =     0.53, user     =     2.05, cpu      =     2.58, perc     =   125.41, , laps =     2000
eBrem_e-                       :: wall     =     1.96, sys      =     0.56, user     =     1.96, cpu      =     2.52, perc     =  5814.14, , laps =   815900
B10                            :: wall     =     1.96, sys      =     0.41, user     =     1.95, cpu      =     2.36, perc     =   466.90, , laps =      325
compt_gamma                    :: wall     =     1.89, sys      =     0.25, user     =     1.89, cpu      =     2.14, perc     =  5309.01, , laps =   343505
StepLimiter_e-                 :: wall     =     1.84, sys      =     0.55, user     =     1.83, cpu      =     2.38, perc     =  5596.64, , laps =   810489
hadElastic_neutron             :: wall     =     1.83, sys      =     0.12, user     =     1.83, cpu      =     1.95, perc     =  1040.67, , laps =   145105
mu+                            :: wall     =     1.83, sys      =     0.53, user     =     1.83, cpu      =     2.36, perc     =   229.03, , laps =     2000
ePairProd_e-                   :: wall     =     1.82, sys      =     0.62, user     =     1.82, cpu      =     2.44, perc     =  5787.87, , laps =   805940
CoulombScat_e-                 :: wall     =     1.79, sys      =     0.60, user     =     1.78, cpu      =     2.38, perc     =  5464.43, , laps =   805940
mu-                            :: wall     =     1.77, sys      =     0.44, user     =     1.77, cpu      =     2.21, perc     =   224.80, , laps =     1998
Transportation_e+              :: wall     =     1.36, sys      =     0.27, user     =     1.36, cpu      =     1.63, perc     =  2154.78, , laps =   592936
eIoni_e+                       :: wall     =     1.15, sys      =     0.38, user     =     1.15, cpu      =     1.53, perc     =  2289.74, , laps =   448684
Transportation_neutron         :: wall     =     0.85, sys      =     0.26, user     =     0.84, cpu      =     1.10, perc     =  1136.07, , laps =   361384
msc_e+                         :: wall     =     0.84, sys      =     0.22, user     =     0.85, cpu      =     1.07, perc     =  2247.15, , laps =   296468
phot_gamma                     :: wall     =     0.76, sys      =     0.20, user     =     0.76, cpu      =     0.96, perc     =  5596.31, , laps =   239543
neutronInelastic_neutron       :: wall     =     0.67, sys      =     0.10, user     =     0.67, cpu      =     0.77, perc     =  1073.35, , laps =    91867
deuteron                       :: wall     =     0.66, sys      =     0.17, user     =     0.66, cpu      =     0.83, perc     =   909.30, , laps =      286
nCapture_neutron               :: wall     =     0.57, sys      =     0.04, user     =     0.57, cpu      =     0.61, perc     =  1016.02, , laps =    90632
Rayl_gamma                     :: wall     =     0.57, sys      =     0.24, user     =     0.56, cpu      =     0.80, perc     =  6308.18, , laps =   233437
conv_gamma                     :: wall     =     0.52, sys      =     0.18, user     =     0.51, cpu      =     0.69, perc     =  6221.44, , laps =   225796
eBrem_e+                       :: wall     =     0.40, sys      =     0.11, user     =     0.40, cpu      =     0.51, perc     =  2221.39, , laps =   156362
annihil_e+                     :: wall     =     0.37, sys      =     0.08, user     =     0.37, cpu      =     0.45, perc     =  2122.59, , laps =   151978
StepLimiter_e+                 :: wall     =     0.35, sys      =     0.11, user     =     0.34, cpu      =     0.45, perc     =  2278.84, , laps =   152781
ePairProd_e+                   :: wall     =     0.33, sys      =     0.04, user     =     0.33, cpu      =     0.37, perc     =  2037.36, , laps =   148234
CoulombScat_e+                 :: wall     =     0.33, sys      =     0.08, user     =     0.33, cpu      =     0.41, perc     =  2192.60, , laps =   148234
StepLimiter_neutron            :: wall     =     0.27, sys      =     0.04, user     =     0.27, cpu      =     0.31, perc     =  1165.81, , laps =   117172
Li7                            :: wall     =     0.27, sys      =     0.11, user     =     0.27, cpu      =     0.38, perc     =  1031.48, , laps =     1520
Transportation_pi+             :: wall     =     0.25, sys      =     0.07, user     =     0.25, cpu      =     0.32, perc     =   261.96, , laps =   104444
Transportation_pi-             :: wall     =     0.24, sys      =     0.08, user     =     0.24, cpu      =     0.32, perc     =   229.60, , laps =   100840
Transportation_mu+             :: wall     =     0.24, sys      =     0.09, user     =     0.24, cpu      =     0.33, perc     =   229.33, , laps =   103192
Transportation_mu-             :: wall     =     0.23, sys      =     0.04, user     =     0.23, cpu      =     0.27, perc     =   216.32, , laps =    99116
nFission_neutron               :: wall     =     0.21, sys      =     0.06, user     =     0.21, cpu      =     0.27, perc     =  1140.96, , laps =    90346
Decay_neutron                  :: wall     =     0.20, sys      =     0.02, user     =     0.20, cpu      =     0.22, perc     =  1017.22, , laps =    90346
O16                            :: wall     =     0.20, sys      =     0.05, user     =     0.20, cpu      =     0.25, perc     =   291.24, , laps =       30
hIoni_pi+                      :: wall     =     0.20, sys      =     0.07, user     =     0.20, cpu      =     0.27, perc     =   239.09, , laps =    78333
Transportation_anti_nu_mu      :: wall     =     0.19, sys      =     0.07, user     =     0.19, cpu      =     0.26, perc     =   374.15, , laps =    73224
muIoni_mu+                     :: wall     =     0.19, sys      =     0.03, user     =     0.19, cpu      =     0.22, perc     =   214.57, , laps =    77394
hIoni_pi-                      :: wall     =     0.19, sys      =     0.03, user     =     0.19, cpu      =     0.22, perc     =   204.30, , laps =    75630
muIoni_mu-                     :: wall     =     0.18, sys      =     0.06, user     =     0.19, cpu      =     0.25, perc     =   229.13, , laps =    74337
Transportation_nu_mu           :: wall     =     0.18, sys      =     0.08, user     =     0.18, cpu      =     0.26, perc     =   400.81, , laps =    74000
msc_pi+                        :: wall     =     0.14, sys      =     0.03, user     =     0.14, cpu      =     0.17, perc     =   212.38, , laps =    52222
Transportation_proton          :: wall     =     0.14, sys      =     0.03, user     =     0.14, cpu      =     0.17, perc     =   912.17, , laps =    57152
msc_pi-                        :: wall     =     0.13, sys      =     0.04, user     =     0.13, cpu      =     0.17, perc     =   237.67, , laps =    50420
msc_mu+                        :: wall     =     0.13, sys      =     0.05, user     =     0.13, cpu      =     0.18, perc     =   237.83, , laps =    51596
msc_mu-                        :: wall     =     0.13, sys      =     0.02, user     =     0.13, cpu      =     0.15, perc     =   210.68, , laps =    49558
hIoni_proton                   :: wall     =     0.11, sys      =     0.08, user     =     0.11, cpu      =     0.19, perc     =  1012.16, , laps =    42864
Transportation_anti_nu_e       :: wall     =     0.10, sys      =     0.02, user     =     0.10, cpu      =     0.12, perc     =   219.89, , laps =    36476
Transportation_nu_e            :: wall     =     0.09, sys      =     0.01, user     =     0.09, cpu      =     0.10, perc     =   218.50, , laps =    36712
Decay_mu+                      :: wall     =     0.09, sys      =     0.02, user     =     0.09, cpu      =     0.11, perc     =   223.02, , laps =    29798
Decay_pi+                      :: wall     =     0.09, sys      =     0.02, user     =     0.09, cpu      =     0.11, perc     =   224.67, , laps =    30110
Decay_mu-                      :: wall     =     0.09, sys      =     0.02, user     =     0.09, cpu      =     0.11, perc     =   217.92, , laps =    28775
Decay_pi-                      :: wall     =     0.09, sys      =     0.02, user     =     0.09, cpu      =     0.11, perc     =   226.17, , laps =    29205
msc_proton                     :: wall     =     0.08, sys      =     0.02, user     =     0.08, cpu      =     0.10, perc     =   941.29, , laps =    28576
pi+Inelastic_pi+               :: wall     =     0.07, sys      =     0.03, user     =     0.07, cpu      =     0.10, perc     =   250.14, , laps =    26111
hadElastic_pi+                 :: wall     =     0.06, sys      =     0.01, user     =     0.06, cpu      =     0.07, perc     =   211.23, , laps =    26112
hadElastic_pi-                 :: wall     =     0.06, sys      =     0.01, user     =     0.06, cpu      =     0.07, perc     =   201.94, , laps =    25212
pi-Inelastic_pi-               :: wall     =     0.06, sys      =     0.01, user     =     0.06, cpu      =     0.07, perc     =   200.85, , laps =    25212
CoulombScat_pi+                :: wall     =     0.06, sys      =     0.02, user     =     0.06, cpu      =     0.08, perc     =   232.94, , laps =    26111
StepLimiter_pi+                :: wall     =     0.06, sys      =     0.02, user     =     0.06, cpu      =     0.08, perc     =   214.08, , laps =    26111
hPairProd_pi+                  :: wall     =     0.06, sys      =     0.02, user     =     0.06, cpu      =     0.08, perc     =   241.52, , laps =    26111
hBrems_pi+                     :: wall     =     0.06, sys      =     0.01, user     =     0.06, cpu      =     0.07, perc     =   224.90, , laps =    26111
CoulombScat_pi-                :: wall     =     0.06, sys      =     0.02, user     =     0.06, cpu      =     0.08, perc     =   242.06, , laps =    25210
CoulombScat_mu+                :: wall     =     0.06, sys      =     0.01, user     =     0.06, cpu      =     0.07, perc     =   216.81, , laps =    25798
muPairProd_mu+                 :: wall     =     0.06, sys      =     0.02, user     =     0.06, cpu      =     0.08, perc     =   227.47, , laps =    25798
StepLimiter_mu+                :: wall     =     0.06, sys      =     0.04, user     =     0.06, cpu      =     0.10, perc     =   254.96, , laps =    25798
hPairProd_pi-                  :: wall     =     0.06, sys      =     0.01, user     =     0.06, cpu      =     0.07, perc     =   242.60, , laps =    25210
StepLimiter_pi-                :: wall     =     0.06, sys      =     0.01, user     =     0.06, cpu      =     0.07, perc     =   233.31, , laps =    25210
muBrems_mu+                    :: wall     =     0.06, sys      =     0.02, user     =     0.06, cpu      =     0.08, perc     =   234.11, , laps =    25798
hBrems_pi-                     :: wall     =     0.06, sys      =     0.03, user     =     0.06, cpu      =     0.09, perc     =   252.61, , laps =    25210
muPairProd_mu-                 :: wall     =     0.06, sys      =     0.03, user     =     0.06, cpu      =     0.09, perc     =   249.13, , laps =    24779
StepLimiter_mu-                :: wall     =     0.06, sys      =     0.04, user     =     0.06, cpu      =     0.10, perc     =   282.52, , laps =    24779
CoulombScat_mu-                :: wall     =     0.06, sys      =     0.02, user     =     0.06, cpu      =     0.08, perc     =   248.00, , laps =    24779
muBrems_mu-                    :: wall     =     0.06, sys      =     0.01, user     =     0.05, cpu      =     0.06, perc     =   221.98, , laps =    24779
hadElastic_proton              :: wall     =     0.04, sys      =     0.00, user     =     0.04, cpu      =     0.04, perc     =   933.31, , laps =    14291
protonInelastic_proton         :: wall     =     0.04, sys      =     0.02, user     =     0.04, cpu      =     0.06, perc     =   954.29, , laps =    14288
StepLimiter_proton             :: wall     =     0.04, sys      =     0.03, user     =     0.03, cpu      =     0.06, perc     =   978.58, , laps =    14288
CoulombScat_proton             :: wall     =     0.04, sys      =     0.03, user     =     0.04, cpu      =     0.07, perc     =  1528.68, , laps =    14289
hPairProd_proton               :: wall     =     0.03, sys      =     0.01, user     =     0.03, cpu      =     0.04, perc     =   935.56, , laps =    14288
hBrems_proton                  :: wall     =     0.03, sys      =     0.01, user     =     0.03, cpu      =     0.04, perc     =   902.29, , laps =    14288
ionIoni_Li7                    :: wall     =     0.03, sys      =     0.00, user     =     0.03, cpu      =     0.03, perc     =   794.98, , laps =     8352
Transportation_Li7             :: wall     =     0.03, sys      =     0.01, user     =     0.03, cpu      =     0.04, perc     =   877.74, , laps =    11136
msc_Li7                        :: wall     =     0.02, sys      =     0.00, user     =     0.02, cpu      =     0.02, perc     =   801.68, , laps =     5568
RadioactiveDecay_Li7           :: wall     =     0.02, sys      =     0.02, user     =     0.02, cpu      =     0.04, perc     =  1253.60, , laps =     5824
Transportation_alpha           :: wall     =     0.01, sys      =     0.00, user     =     0.01, cpu      =     0.01, perc     =   803.67, , laps =     6104
nuclearStopping_Li7            :: wall     =     0.01, sys      =     0.01, user     =     0.01, cpu      =     0.02, perc     =  1709.28, , laps =     5568
ionIoni_alpha                  :: wall     =     0.01, sys      =     0.00, user     =     0.01, cpu      =     0.01, perc     =   807.31, , laps =     4578
ionInelastic_Li7               :: wall     =     0.01, sys      =     0.01, user     =     0.01, cpu      =     0.02, perc     =  1360.47, , laps =     2784
msc_alpha                      :: wall     =     0.01, sys      =     0.00, user     =     0.01, cpu      =     0.01, perc     =   776.42, , laps =     3052
Transportation_B11             :: wall     =     0.01, sys      =     0.00, user     =     0.01, cpu      =     0.01, perc     =   589.69, , laps =     3340
ionElastic_Li7                 :: wall     =     0.01, sys      =     0.01, user     =     0.01, cpu      =     0.02, perc     =  1682.09, , laps =     2784
nuclearStopping_alpha          :: wall     =     0.01, sys      =     0.01, user     =     0.01, cpu      =     0.02, perc     =  1518.39, , laps =     3052
StepLimiter_Li7                :: wall     =     0.01, sys      =     0.00, user     =     0.01, cpu      =     0.01, perc     =   820.42, , laps =     2784
ionIoni_B11                    :: wall     =     0.01, sys      =     0.00, user     =     0.01, cpu      =     0.01, perc     =   607.83, , laps =     2505
RadioactiveDecay_B11           :: wall     =     0.01, sys      =     0.00, user     =     0.01, cpu      =     0.01, perc     =   602.21, , laps =     2505
hadElastic_alpha               :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   781.88, , laps =     1526
alphaInelastic_alpha           :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   829.93, , laps =     1526
ionIoni_B10                    :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   397.30, , laps =      978
msc_B11                        :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   590.01, , laps =     1670
StepLimiter_alpha              :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   789.37, , laps =     1526
nuclearStopping_B11            :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   582.59, , laps =     1670
Transportation_B10             :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   400.00, , laps =     1304
Transportation_deuteron        :: wall     =     0.00, sys      =     0.01, user     =     0.00, cpu      =     0.01, perc     =  2234.79, , laps =     1144
RadioactiveDecay_B10           :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   396.45, , laps =      976
ionInelastic_B11               :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   604.18, , laps =      835
hIoni_deuteron                 :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   779.81, , laps =      858
ionIoni_O16                    :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   196.51, , laps =       93
ionElastic_B11                 :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   573.13, , laps =      835
StepLimiter_B11                :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   565.03, , laps =      835
dInelastic_deuteron            :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   794.92, , laps =      286
msc_deuteron                   :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   777.42, , laps =      572
msc_B10                        :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   403.44, , laps =      652
nuclearStopping_B10            :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   408.96, , laps =      652
nuclearStopping_deuteron       :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   783.68, , laps =      572
hadElastic_deuteron            :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   746.33, , laps =      286
ionInelastic_B10               :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   415.51, , laps =      326
triton                         :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   100.00, , laps =        1
ionElastic_B10                 :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   404.01, , laps =      326
StepLimiter_B10                :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   385.55, , laps =      326
StepLimiter_deuteron           :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   699.60, , laps =      286
Transportation_O16             :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   192.17, , laps =      124
RadioactiveDecay_O16           :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   213.04, , laps =       91
msc_O16                        :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   202.26, , laps =       62
O17                            :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   100.00, , laps =        1
nuclearStopping_O16            :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   215.52, , laps =       62
ionInelastic_O16               :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   195.93, , laps =       31
ionElastic_O16                 :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   206.37, , laps =       31
StepLimiter_O16                :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   177.00, , laps =       31
Transportation_triton          :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =    97.62, , laps =       20
hIoni_triton                   :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =    89.19, , laps =       15
msc_triton                     :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =    96.00, , laps =       10
nuclearStopping_triton         :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   109.52, , laps =       10
Decay_triton                   :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   100.00, , laps =        7
tInelastic_triton              :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   108.33, , laps =        5
StepLimiter_triton             :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =    90.91, , laps =        5
hadElastic_triton              :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   100.00, , laps =        5
Transportation_O17             :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =    80.00, , laps =        4
RadioactiveDecay_O17           :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   100.00, , laps =        3
ionIoni_O17                    :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   100.00, , laps =        3
ionInelastic_O17               :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   100.00, , laps =        1
nuclearStopping_O17            :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =    80.00, , laps =        2
msc_O17                        :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   100.00, , laps =        2
StepLimiter_O17                :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   100.00, , laps =        1
ionElastic_O17                 :: wall     =     0.00, sys      =     0.00, user     =     0.00, cpu      =     0.00, perc     =   133.33, , laps =        1
```

## Full output for neutron, proton, e-, and pi-

```
> [exe] total execution time                                                                                          : 21.027 wall, 18.390 user +  2.570 system = 20.960 CPU [sec] ( 99.7%)  (x1 laps)
> [cxx] |_neutron                                                                                                     :  1.217 wall,  0.980 user +  0.140 system =  1.120 CPU [sec] ( 92.0%)  (x200 laps)
> [cxx]   |_[StepLimiter_neutron]                                                                                     :  0.008 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (119.5%)  (x4457 laps)
> [cxx]   |_[hadElastic_neutron]                                                                                      :  0.044 wall,  0.030 user +  0.010 system =  0.040 CPU [sec] ( 91.3%)  (x4772 laps)
> [cxx]   |_[nFission_neutron]                                                                                        :  0.006 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (168.4%)  (x3201 laps)
> [cxx]   |_[nCapture_neutron]                                                                                        :  0.015 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] (134.7%)  (x3207 laps)
> [cxx]   |_[neutronInelastic_neutron]                                                                                :  0.022 wall,  0.030 user +  0.010 system =  0.040 CPU [sec] (182.8%)  (x3273 laps)
> [cxx]   |_[Decay_neutron]                                                                                           :  0.006 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3201 laps)
> [cxx]   |_[Transportation_neutron]                                                                                  :  0.027 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] ( 74.8%)  (x12804 laps)
> [cxx]     |_B11                                                                                                     :  0.552 wall,  0.470 user +  0.060 system =  0.530 CPU [sec] ( 96.0%)  (x54 laps)
> [cxx]     |_[StepLimiter_neutron]                                                                                   :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1069 laps)
> [cxx]     |_[hadElastic_neutron]                                                                                    :  0.008 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1065 laps)
> [cxx]     |_[nFission_neutron]                                                                                      :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x741 laps)
> [cxx]     |_[nCapture_neutron]                                                                                      :  0.003 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (325.4%)  (x742 laps)
> [cxx]     |_[neutronInelastic_neutron]                                                                              :  0.005 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (211.1%)  (x759 laps)
> [cxx]     |_[Decay_neutron]                                                                                         :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x741 laps)
> [cxx]     |_[Transportation_neutron]                                                                                :  0.006 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2964 laps)
> [cxx]       |_B10                                                                                                   :  0.052 wall,  0.050 user +  0.000 system =  0.050 CPU [sec] ( 95.5%)  (x7 laps)
> [cxx]       |_[StepLimiter_neutron]                                                                                 :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x701 laps)
> [cxx]       |_[hadElastic_neutron]                                                                                  :  0.008 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (120.6%)  (x777 laps)
> [cxx]       |_[nFission_neutron]                                                                                    :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x509 laps)
> [cxx]       |_[nCapture_neutron]                                                                                    :  0.003 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (394.0%)  (x510 laps)
> [cxx]       |_[neutronInelastic_neutron]                                                                            :  0.003 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (321.8%)  (x517 laps)
> [cxx]       |_[Decay_neutron]                                                                                       :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x509 laps)
> [cxx]       |_[Transportation_neutron]                                                                              :  0.004 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (241.5%)  (x2036 laps)
> [cxx]         |_B10                                                                                                 :  0.020 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] (101.2%)  (x2 laps)
> [cxx]         |_[StepLimiter_neutron]                                                                               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x69 laps)
> [cxx]         |_[hadElastic_neutron]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x70 laps)
> [cxx]         |_[nFission_neutron]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x50 laps)
> [cxx]         |_[nCapture_neutron]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x50 laps)
> [cxx]         |_[neutronInelastic_neutron]                                                                          :  0.001 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (1869.2%)  (x52 laps)
> [cxx]         |_[Decay_neutron]                                                                                     :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x50 laps)
> [cxx]         |_[Transportation_neutron]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x200 laps)
> [cxx]           |_alpha                                                                                             :  0.013 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 78.8%)  (x2 laps)
> [cxx]             |_gamma                                                                                           :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]               |_Li7                                                                                           :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]             |_[StepLimiter_Li7]                                                                               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]             |_[ionInelastic_Li7]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]             |_[ionElastic_Li7]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]             |_[RadioactiveDecay_Li7]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x7 laps)
> [cxx]             |_[ionIoni_Li7]                                                                                   :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x9 laps)
> [cxx]             |_[Transportation_Li7]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x12 laps)
> [cxx]             |_[nuclearStopping_Li7]                                                                           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]             |_[msc_Li7]                                                                                       :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]           |_[Rayl_gamma]                                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]           |_[conv_gamma]                                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]           |_[compt_gamma]                                                                                     :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]           |_[phot_gamma]                                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]           |_[Transportation_gamma]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x16 laps)
> [cxx]             |_e-                                                                                              :  0.010 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (103.4%)  (x2 laps)
> [cxx]             |_[Rayl_gamma]                                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]             |_[conv_gamma]                                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]             |_[compt_gamma]                                                                                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]             |_[phot_gamma]                                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]             |_[Transportation_gamma]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x16 laps)
> [cxx]               |_e-                                                                                            :  0.007 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (147.7%)  (x2 laps)
> [cxx]               |_[Rayl_gamma]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]               |_[conv_gamma]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]               |_[compt_gamma]                                                                                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x5 laps)
> [cxx]               |_[phot_gamma]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]               |_[Transportation_gamma]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x12 laps)
> [cxx]                 |_e-                                                                                          :  0.005 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (206.8%)  (x2 laps)
> [cxx]                 |_[Rayl_gamma]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]                 |_[conv_gamma]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]                 |_[compt_gamma]                                                                               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x5 laps)
> [cxx]                 |_[phot_gamma]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]                 |_[Transportation_gamma]                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x12 laps)
> [cxx]                   |_e-                                                                                        :  0.004 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (280.9%)  (x2 laps)
> [cxx]                   |_[Rayl_gamma]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]                   |_[conv_gamma]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]                   |_[compt_gamma]                                                                             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]                   |_[phot_gamma]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]                   |_[Transportation_gamma]                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x16 laps)
> [cxx]                     |_e-                                                                                      :  0.002 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (407.2%)  (x2 laps)
> [cxx]                     |_[Rayl_gamma]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]                     |_[conv_gamma]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]                     |_[compt_gamma]                                                                           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3 laps)
> [cxx]                     |_[phot_gamma]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]                     |_[Transportation_gamma]                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]                   |_[StepLimiter_e-]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]                   |_[CoulombScat_e-]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]                   |_[ePairProd_e-]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]                   |_[eBrem_e-]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]                   |_[eIoni_e-]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x12 laps)
> [cxx]                   |_[Transportation_e-]                                                                       :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x16 laps)
> [cxx]                   |_[msc_e-]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]                 |_[StepLimiter_e-]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x5 laps)
> [cxx]                 |_[CoulombScat_e-]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x5 laps)
> [cxx]                 |_[ePairProd_e-]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x5 laps)
> [cxx]                 |_[eBrem_e-]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x5 laps)
> [cxx]                 |_[eIoni_e-]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x15 laps)
> [cxx]                 |_[Transportation_e-]                                                                         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x20 laps)
> [cxx]                 |_[msc_e-]                                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x10 laps)
> [cxx]               |_[StepLimiter_e-]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]               |_[CoulombScat_e-]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]               |_[ePairProd_e-]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]               |_[eBrem_e-]                                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]               |_[eIoni_e-]                                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x18 laps)
> [cxx]               |_[Transportation_e-]                                                                           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x24 laps)
> [cxx]               |_[msc_e-]                                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x12 laps)
> [cxx]             |_[StepLimiter_e-]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x12 laps)
> [cxx]             |_[CoulombScat_e-]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x12 laps)
> [cxx]             |_[ePairProd_e-]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x12 laps)
> [cxx]             |_[eBrem_e-]                                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x12 laps)
> [cxx]             |_[eIoni_e-]                                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x36 laps)
> [cxx]             |_[Transportation_e-]                                                                             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x48 laps)
> [cxx]             |_[msc_e-]                                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x24 laps)
> [cxx]           |_[StepLimiter_e-]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x19 laps)
> [cxx]           |_[CoulombScat_e-]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x19 laps)
> [cxx]           |_[ePairProd_e-]                                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x19 laps)
> [cxx]           |_[eBrem_e-]                                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x19 laps)
> [cxx]           |_[eIoni_e-]                                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x57 laps)
> [cxx]           |_[Transportation_e-]                                                                               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x76 laps)
> [cxx]           |_[msc_e-]                                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x38 laps)
> [cxx]         |_[StepLimiter_alpha]                                                                                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]         |_[alphaInelastic_alpha]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]         |_[hadElastic_alpha]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]         |_[ionIoni_alpha]                                                                                     :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]         |_[Transportation_alpha]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]         |_[nuclearStopping_alpha]                                                                             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]         |_[msc_alpha]                                                                                         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]       |_[StepLimiter_B10]                                                                                     :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]       |_[ionInelastic_B10]                                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]       |_[ionElastic_B10]                                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2 laps)
> [cxx]       |_[RadioactiveDecay_B10]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]       |_[ionIoni_B10]                                                                                         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x6 laps)
> [cxx]       |_[Transportation_B10]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]       |_[nuclearStopping_B10]                                                                                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]       |_[msc_B10]                                                                                             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4 laps)
> [cxx]     |_[StepLimiter_B10]                                                                                       :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x7 laps)
> [cxx]     |_[ionInelastic_B10]                                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x7 laps)
> [cxx]     |_[ionElastic_B10]                                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x7 laps)
> [cxx]     |_[RadioactiveDecay_B10]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x21 laps)
> [cxx]     |_[ionIoni_B10]                                                                                           :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x21 laps)
> [cxx]     |_[Transportation_B10]                                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x28 laps)
> [cxx]     |_[nuclearStopping_B10]                                                                                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x14 laps)
> [cxx]     |_[msc_B10]                                                                                               :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x14 laps)
> [cxx]   |_[StepLimiter_B11]                                                                                         :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x55 laps)
> [cxx]   |_[ionInelastic_B11]                                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x55 laps)
> [cxx]   |_[ionElastic_B11]                                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x55 laps)
> [cxx]   |_[RadioactiveDecay_B11]                                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x165 laps)
> [cxx]   |_[ionIoni_B11]                                                                                             :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x165 laps)
> [cxx]   |_[Transportation_B11]                                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x220 laps)
> [cxx]   |_[nuclearStopping_B11]                                                                                     :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x110 laps)
> [cxx]   |_[msc_B11]                                                                                                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x110 laps)
> [cxx] |_proton                                                                                                      :  0.191 wall,  0.170 user +  0.030 system =  0.200 CPU [sec] (104.4%)  (x200 laps)
> [cxx]   |_[StepLimiter_proton]                                                                                      :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1247 laps)
> [cxx]   |_[hadElastic_proton]                                                                                       :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1248 laps)
> [cxx]   |_[protonInelastic_proton]                                                                                  :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1247 laps)
> [cxx]   |_[CoulombScat_proton]                                                                                      :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1247 laps)
> [cxx]   |_[hPairProd_proton]                                                                                        :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1247 laps)
> [cxx]   |_[hBrems_proton]                                                                                           :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1247 laps)
> [cxx]   |_[hIoni_proton]                                                                                            :  0.008 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3741 laps)
> [cxx]   |_[Transportation_proton]                                                                                   :  0.011 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] ( 93.8%)  (x4988 laps)
> [cxx]   |_[msc_proton]                                                                                              :  0.006 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2494 laps)
> [cxx] |_e-                                                                                                          :  0.291 wall,  0.220 user +  0.020 system =  0.240 CPU [sec] ( 82.4%)  (x200 laps)
> [cxx]   |_[StepLimiter_e-]                                                                                          :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2100 laps)
> [cxx]   |_[CoulombScat_e-]                                                                                          :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2100 laps)
> [cxx]   |_[ePairProd_e-]                                                                                            :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2100 laps)
> [cxx]   |_[eBrem_e-]                                                                                                :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2109 laps)
> [cxx]   |_[eIoni_e-]                                                                                                :  0.013 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] ( 77.9%)  (x6300 laps)
> [cxx]   |_[Transportation_e-]                                                                                       :  0.016 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] ( 62.5%)  (x8400 laps)
> [cxx]   |_[msc_e-]                                                                                                  :  0.011 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 91.0%)  (x4200 laps)
> [cxx] |_pi-                                                                                                         :  0.404 wall,  0.430 user +  0.030 system =  0.460 CPU [sec] (113.9%)  (x200 laps)
> [cxx]   |_[StepLimiter_pi-]                                                                                         :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2451 laps)
> [cxx]   |_[hadElastic_pi-]                                                                                          :  0.005 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (209.2%)  (x2451 laps)
> [cxx]   |_[pi-Inelastic_pi-]                                                                                        :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2451 laps)
> [cxx]   |_[Decay_pi-]                                                                                               :  0.007 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (134.1%)  (x2851 laps)
> [cxx]   |_[CoulombScat_pi-]                                                                                         :  0.005 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (221.2%)  (x2451 laps)
> [cxx]   |_[hPairProd_pi-]                                                                                           :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2451 laps)
> [cxx]   |_[hBrems_pi-]                                                                                              :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2451 laps)
> [cxx]   |_[hIoni_pi-]                                                                                               :  0.015 wall,  0.030 user +  0.000 system =  0.030 CPU [sec] (197.7%)  (x7353 laps)
> [cxx]   |_[Transportation_pi-]                                                                                      :  0.019 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x9804 laps)
> [cxx]   |_[msc_pi-]                                                                                                 :  0.011 wall,  0.010 user +  0.010 system =  0.020 CPU [sec] (181.1%)  (x4902 laps)
> [cxx]     |_anti_nu_mu                                                                                              :  6.802 wall,  5.840 user +  0.920 system =  6.760 CPU [sec] ( 99.4%)  (x200 laps)
> [cxx]       |_mu-                                                                                                   :  0.362 wall,  0.250 user +  0.040 system =  0.290 CPU [sec] ( 80.1%)  (x200 laps)
> [cxx]     |_[StepLimiter_mu-]                                                                                       :  0.004 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (241.2%)  (x2467 laps)
> [cxx]     |_[Decay_mu-]                                                                                             :  0.008 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2867 laps)
> [cxx]     |_[CoulombScat_mu-]                                                                                       :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2467 laps)
> [cxx]     |_[muPairProd_mu-]                                                                                        :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2467 laps)
> [cxx]     |_[muBrems_mu-]                                                                                           :  0.004 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (226.4%)  (x2467 laps)
> [cxx]     |_[muIoni_mu-]                                                                                            :  0.015 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] ( 65.9%)  (x7401 laps)
> [cxx]     |_[Transportation_mu-]                                                                                    :  0.019 wall,  0.010 user +  0.010 system =  0.020 CPU [sec] (108.1%)  (x9868 laps)
> [cxx]     |_[msc_mu-]                                                                                               :  0.011 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4934 laps)
> [cxx]       |_nu_mu                                                                                                 :  6.400 wall,  5.550 user +  0.880 system =  6.430 CPU [sec] (100.5%)  (x200 laps)
> [cxx]         |_anti_nu_e                                                                                           :  6.361 wall,  5.540 user +  0.860 system =  6.400 CPU [sec] (100.6%)  (x200 laps)
> [cxx]           |_e-                                                                                                :  2.183 wall,  1.910 user +  0.290 system =  2.200 CPU [sec] (100.8%)  (x200 laps)
> [cxx]         |_[StepLimiter_e-]                                                                                    :  0.006 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (169.3%)  (x3229 laps)
> [cxx]         |_[CoulombScat_e-]                                                                                    :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3142 laps)
> [cxx]         |_[ePairProd_e-]                                                                                      :  0.006 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (178.6%)  (x3142 laps)
> [cxx]         |_[eBrem_e-]                                                                                          :  0.007 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3279 laps)
> [cxx]         |_[eIoni_e-]                                                                                          :  0.020 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] ( 50.7%)  (x9509 laps)
> [cxx]         |_[Transportation_e-]                                                                                 :  0.023 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] ( 85.7%)  (x12568 laps)
> [cxx]         |_[msc_e-]                                                                                            :  0.016 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] ( 62.9%)  (x6284 laps)
> [cxx]           |_e-                                                                                                :  2.341 wall,  1.990 user +  0.320 system =  2.310 CPU [sec] ( 98.7%)  (x82 laps)
> [cxx]           |_[StepLimiter_e-]                                                                                  :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1572 laps)
> [cxx]           |_[CoulombScat_e-]                                                                                  :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1540 laps)
> [cxx]           |_[ePairProd_e-]                                                                                    :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1540 laps)
> [cxx]           |_[eBrem_e-]                                                                                        :  0.003 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] (597.6%)  (x1601 laps)
> [cxx]           |_[eIoni_e-]                                                                                        :  0.009 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] (216.3%)  (x4646 laps)
> [cxx]           |_[Transportation_e-]                                                                               :  0.011 wall,  0.020 user +  0.000 system =  0.020 CPU [sec] (176.1%)  (x6160 laps)
> [cxx]           |_[msc_e-]                                                                                          :  0.008 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3080 laps)
> [cxx]             |_e-                                                                                              :  0.540 wall,  0.480 user +  0.080 system =  0.560 CPU [sec] (103.6%)  (x25 laps)
> [cxx]             |_[StepLimiter_e-]                                                                                :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x839 laps)
> [cxx]             |_[CoulombScat_e-]                                                                                :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x829 laps)
> [cxx]             |_[ePairProd_e-]                                                                                  :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x829 laps)
> [cxx]             |_[eBrem_e-]                                                                                      :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x842 laps)
> [cxx]             |_[eIoni_e-]                                                                                      :  0.005 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (203.0%)  (x2499 laps)
> [cxx]             |_[Transportation_e-]                                                                             :  0.006 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (164.5%)  (x3316 laps)
> [cxx]             |_[msc_e-]                                                                                        :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1658 laps)
> [cxx]               |_gamma                                                                                         :  0.260 wall,  0.220 user +  0.030 system =  0.250 CPU [sec] ( 96.0%)  (x13 laps)
> [cxx]               |_[StepLimiter_e-]                                                                              :  0.002 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (509.7%)  (x1141 laps)
> [cxx]               |_[CoulombScat_e-]                                                                              :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1129 laps)
> [cxx]               |_[ePairProd_e-]                                                                                :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1129 laps)
> [cxx]               |_[eBrem_e-]                                                                                    :  0.002 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (436.1%)  (x1161 laps)
> [cxx]               |_[eIoni_e-]                                                                                    :  0.007 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3400 laps)
> [cxx]               |_[Transportation_e-]                                                                           :  0.008 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (119.5%)  (x4516 laps)
> [cxx]               |_[msc_e-]                                                                                      :  0.006 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (180.5%)  (x2258 laps)
> [cxx]                 |_gamma                                                                                       :  0.503 wall,  0.470 user +  0.050 system =  0.520 CPU [sec] (103.4%)  (x31 laps)
> [cxx]                 |_[StepLimiter_e-]                                                                            :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1424 laps)
> [cxx]                 |_[CoulombScat_e-]                                                                            :  0.002 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (420.5%)  (x1408 laps)
> [cxx]                 |_[ePairProd_e-]                                                                              :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1408 laps)
> [cxx]                 |_[eBrem_e-]                                                                                  :  0.003 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (346.7%)  (x1443 laps)
> [cxx]                 |_[eIoni_e-]                                                                                  :  0.009 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x4244 laps)
> [cxx]                 |_[Transportation_e-]                                                                         :  0.010 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x5632 laps)
> [cxx]                 |_[msc_e-]                                                                                    :  0.007 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2816 laps)
> [cxx]                   |_e-                                                                                        :  0.358 wall,  0.280 user +  0.030 system =  0.310 CPU [sec] ( 86.6%)  (x20 laps)
> [cxx]                   |_[StepLimiter_e-]                                                                          :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x795 laps)
> [cxx]                   |_[CoulombScat_e-]                                                                          :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x791 laps)
> [cxx]                   |_[ePairProd_e-]                                                                            :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x791 laps)
> [cxx]                   |_[eBrem_e-]                                                                                :  0.002 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (626.6%)  (x807 laps)
> [cxx]                   |_[eIoni_e-]                                                                                :  0.005 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (205.5%)  (x2380 laps)
> [cxx]                   |_[Transportation_e-]                                                                       :  0.006 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (167.2%)  (x3164 laps)
> [cxx]                   |_[msc_e-]                                                                                  :  0.004 wall,  0.010 user +  0.010 system =  0.020 CPU [sec] (507.2%)  (x1582 laps)
> [cxx]               |_[Rayl_gamma]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x204 laps)
> [cxx]               |_[conv_gamma]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x198 laps)
> [cxx]               |_[compt_gamma]                                                                                 :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x292 laps)
> [cxx]               |_[phot_gamma]                                                                                  :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x212 laps)
> [cxx]               |_[Transportation_gamma]                                                                        :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x792 laps)
> [cxx]                 |_e-                                                                                          :  0.394 wall,  0.310 user +  0.080 system =  0.390 CPU [sec] ( 98.9%)  (x97 laps)
> [cxx]                 |_[Rayl_gamma]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x162 laps)
> [cxx]                 |_[conv_gamma]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x156 laps)
> [cxx]                 |_[compt_gamma]                                                                               :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x242 laps)
> [cxx]                 |_[phot_gamma]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x166 laps)
> [cxx]                 |_[Transportation_gamma]                                                                      :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x624 laps)
> [cxx]                   |_e-                                                                                        :  0.337 wall,  0.310 user +  0.070 system =  0.380 CPU [sec] (112.8%)  (x93 laps)
> [cxx]                   |_[Rayl_gamma]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x154 laps)
> [cxx]                   |_[conv_gamma]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x148 laps)
> [cxx]                   |_[compt_gamma]                                                                             :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x228 laps)
> [cxx]                   |_[phot_gamma]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x153 laps)
> [cxx]                   |_[Transportation_gamma]                                                                    :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x592 laps)
> [cxx]                     |_e-                                                                                      :  0.283 wall,  0.250 user +  0.060 system =  0.310 CPU [sec] (109.6%)  (x83 laps)
> [cxx]                     |_[Rayl_gamma]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x139 laps)
> [cxx]                     |_[conv_gamma]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x134 laps)
> [cxx]                     |_[compt_gamma]                                                                           :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x203 laps)
> [cxx]                     |_[phot_gamma]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x140 laps)
> [cxx]                     |_[Transportation_gamma]                                                                  :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x536 laps)
> [cxx]                       |_e-                                                                                    :  0.247 wall,  0.170 user +  0.060 system =  0.230 CPU [sec] ( 93.0%)  (x72 laps)
> [cxx]                       |_[Rayl_gamma]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x109 laps)
> [cxx]                       |_[conv_gamma]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x107 laps)
> [cxx]                       |_[compt_gamma]                                                                         :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x168 laps)
> [cxx]                       |_[phot_gamma]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x110 laps)
> [cxx]                       |_[Transportation_gamma]                                                                :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x428 laps)
> [cxx]                         |_e-                                                                                  :  0.217 wall,  0.140 user +  0.050 system =  0.190 CPU [sec] ( 87.6%)  (x67 laps)
> [cxx]                         |_[Rayl_gamma]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x96 laps)
> [cxx]                         |_[conv_gamma]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x93 laps)
> [cxx]                         |_[compt_gamma]                                                                       :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x151 laps)
> [cxx]                         |_[phot_gamma]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x96 laps)
> [cxx]                         |_[Transportation_gamma]                                                              :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x372 laps)
> [cxx]                           |_e-                                                                                :  0.187 wall,  0.130 user +  0.040 system =  0.170 CPU [sec] ( 91.0%)  (x62 laps)
> [cxx]                             |_e-                                                                              :  0.158 wall,  0.100 user +  0.040 system =  0.140 CPU [sec] ( 88.6%)  (x51 laps)
> [cxx]                             |_[Rayl_gamma]                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x70 laps)
> [cxx]                             |_[conv_gamma]                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x67 laps)
> [cxx]                             |_[compt_gamma]                                                                   :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x107 laps)
> [cxx]                             |_[phot_gamma]                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x71 laps)
> [cxx]                             |_[Transportation_gamma]                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x268 laps)
> [cxx]                               |_e-                                                                            :  0.136 wall,  0.080 user +  0.040 system =  0.120 CPU [sec] ( 88.3%)  (x46 laps)
> [cxx]                               |_[Rayl_gamma]                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x85 laps)
> [cxx]                               |_[conv_gamma]                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x80 laps)
> [cxx]                               |_[compt_gamma]                                                                 :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x120 laps)
> [cxx]                               |_[phot_gamma]                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x84 laps)
> [cxx]                               |_[Transportation_gamma]                                                        :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x320 laps)
> [cxx]                             |_[StepLimiter_e-]                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x107 laps)
> [cxx]                             |_[CoulombScat_e-]                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x107 laps)
> [cxx]                             |_[ePairProd_e-]                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x107 laps)
> [cxx]                             |_[eBrem_e-]                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x107 laps)
> [cxx]                             |_[eIoni_e-]                                                                      :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x321 laps)
> [cxx]                             |_[Transportation_e-]                                                             :  0.001 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (1317.5%)  (x428 laps)
> [cxx]                             |_[msc_e-]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x214 laps)
> [cxx]                           |_[StepLimiter_e-]                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x121 laps)
> [cxx]                           |_[CoulombScat_e-]                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x121 laps)
> [cxx]                           |_[ePairProd_e-]                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x121 laps)
> [cxx]                           |_[eBrem_e-]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x121 laps)
> [cxx]                           |_[eIoni_e-]                                                                        :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x363 laps)
> [cxx]                           |_[Transportation_e-]                                                               :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x484 laps)
> [cxx]                           |_[msc_e-]                                                                          :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x242 laps)
> [cxx]                         |_[StepLimiter_e-]                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x142 laps)
> [cxx]                         |_[CoulombScat_e-]                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x142 laps)
> [cxx]                         |_[ePairProd_e-]                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x142 laps)
> [cxx]                         |_[eBrem_e-]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x142 laps)
> [cxx]                         |_[eIoni_e-]                                                                          :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x426 laps)
> [cxx]                         |_[Transportation_e-]                                                                 :  0.001 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (1007.0%)  (x568 laps)
> [cxx]                         |_[msc_e-]                                                                            :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x284 laps)
> [cxx]                       |_[StepLimiter_e-]                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x158 laps)
> [cxx]                       |_[CoulombScat_e-]                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x158 laps)
> [cxx]                       |_[ePairProd_e-]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x158 laps)
> [cxx]                       |_[eBrem_e-]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x159 laps)
> [cxx]                       |_[eIoni_e-]                                                                            :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x474 laps)
> [cxx]                       |_[Transportation_e-]                                                                   :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x632 laps)
> [cxx]                       |_[msc_e-]                                                                              :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x316 laps)
> [cxx]                     |_[StepLimiter_e-]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x279 laps)
> [cxx]                     |_[CoulombScat_e-]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x277 laps)
> [cxx]                     |_[ePairProd_e-]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x277 laps)
> [cxx]                     |_[eBrem_e-]                                                                              :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x281 laps)
> [cxx]                     |_[eIoni_e-]                                                                              :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x832 laps)
> [cxx]                     |_[Transportation_e-]                                                                     :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1108 laps)
> [cxx]                     |_[msc_e-]                                                                                :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x554 laps)
> [cxx]                   |_[StepLimiter_e-]                                                                          :  0.001 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (830.6%)  (x671 laps)
> [cxx]                   |_[CoulombScat_e-]                                                                          :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x669 laps)
> [cxx]                   |_[ePairProd_e-]                                                                            :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x669 laps)
> [cxx]                   |_[eBrem_e-]                                                                                :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x671 laps)
> [cxx]                   |_[eIoni_e-]                                                                                :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2015 laps)
> [cxx]                   |_[Transportation_e-]                                                                       :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2676 laps)
> [cxx]                   |_[msc_e-]                                                                                  :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1338 laps)
> [cxx]                 |_[StepLimiter_e-]                                                                            :  0.001 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (834.0%)  (x708 laps)
> [cxx]                 |_[CoulombScat_e-]                                                                            :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x708 laps)
> [cxx]                 |_[ePairProd_e-]                                                                              :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x708 laps)
> [cxx]                 |_[eBrem_e-]                                                                                  :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x717 laps)
> [cxx]                 |_[eIoni_e-]                                                                                  :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2135 laps)
> [cxx]                 |_[Transportation_e-]                                                                         :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x2832 laps)
> [cxx]                 |_[msc_e-]                                                                                    :  0.003 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (291.3%)  (x1416 laps)
> [cxx]             |_[Rayl_gamma]                                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x196 laps)
> [cxx]             |_[conv_gamma]                                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x190 laps)
> [cxx]             |_[compt_gamma]                                                                                   :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x287 laps)
> [cxx]             |_[phot_gamma]                                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x201 laps)
> [cxx]             |_[Transportation_gamma]                                                                          :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x760 laps)
> [cxx]               |_e-                                                                                            :  0.403 wall,  0.340 user +  0.080 system =  0.420 CPU [sec] (104.1%)  (x102 laps)
> [cxx]               |_[Rayl_gamma]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x166 laps)
> [cxx]               |_[conv_gamma]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x160 laps)
> [cxx]               |_[compt_gamma]                                                                                 :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x252 laps)
> [cxx]               |_[phot_gamma]                                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x170 laps)
> [cxx]               |_[Transportation_gamma]                                                                        :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x640 laps)
> [cxx]                 |_e-                                                                                          :  0.348 wall,  0.290 user +  0.060 system =  0.350 CPU [sec] (100.5%)  (x95 laps)
> [cxx]                 |_[Rayl_gamma]                                                                                :  0.000 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (3424.7%)  (x161 laps)
> [cxx]                 |_[conv_gamma]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x154 laps)
> [cxx]                 |_[compt_gamma]                                                                               :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x234 laps)
> [cxx]                 |_[phot_gamma]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x163 laps)
> [cxx]                 |_[Transportation_gamma]                                                                      :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x616 laps)
> [cxx]                   |_e-                                                                                        :  0.296 wall,  0.230 user +  0.060 system =  0.290 CPU [sec] ( 98.1%)  (x83 laps)
> [cxx]                   |_[Rayl_gamma]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x124 laps)
> [cxx]                   |_[conv_gamma]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x122 laps)
> [cxx]                   |_[compt_gamma]                                                                             :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x191 laps)
> [cxx]                   |_[phot_gamma]                                                                              :  0.000 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (3436.4%)  (x129 laps)
> [cxx]                   |_[Transportation_gamma]                                                                    :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x488 laps)
> [cxx]                     |_e-                                                                                      :  0.254 wall,  0.190 user +  0.030 system =  0.220 CPU [sec] ( 86.6%)  (x73 laps)
> [cxx]                     |_[Rayl_gamma]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x109 laps)
> [cxx]                     |_[conv_gamma]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x106 laps)
> [cxx]                     |_[compt_gamma]                                                                           :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x171 laps)
> [cxx]                     |_[phot_gamma]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x108 laps)
> [cxx]                     |_[Transportation_gamma]                                                                  :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x424 laps)
> [cxx]                       |_e-                                                                                    :  0.222 wall,  0.170 user +  0.020 system =  0.190 CPU [sec] ( 85.7%)  (x69 laps)
> [cxx]                       |_[Rayl_gamma]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x96 laps)
> [cxx]                       |_[conv_gamma]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x94 laps)
> [cxx]                       |_[compt_gamma]                                                                         :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x155 laps)
> [cxx]                       |_[phot_gamma]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x98 laps)
> [cxx]                       |_[Transportation_gamma]                                                                :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x376 laps)
> [cxx]                         |_e-                                                                                  :  0.192 wall,  0.140 user +  0.010 system =  0.150 CPU [sec] ( 78.0%)  (x64 laps)
> [cxx]                         |_[Rayl_gamma]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x93 laps)
> [cxx]                         |_[conv_gamma]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x89 laps)
> [cxx]                         |_[compt_gamma]                                                                       :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x143 laps)
> [cxx]                         |_[phot_gamma]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x95 laps)
> [cxx]                         |_[Transportation_gamma]                                                              :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x356 laps)
> [cxx]                           |_e-                                                                                :  0.004 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]                             |_e-                                                                              :  0.005 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x8 laps)
> [cxx]                               |_e-                                                                            :  0.003 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (396.8%)  (x6 laps)
> [cxx]                             |_[StepLimiter_e-]                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x99 laps)
> [cxx]                             |_[CoulombScat_e-]                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x99 laps)
> [cxx]                             |_[ePairProd_e-]                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x99 laps)
> [cxx]                             |_[eBrem_e-]                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x99 laps)
> [cxx]                             |_[eIoni_e-]                                                                      :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x297 laps)
> [cxx]                             |_[Transportation_e-]                                                             :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x396 laps)
> [cxx]                             |_[msc_e-]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x198 laps)
> [cxx]                           |_[StepLimiter_e-]                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x117 laps)
> [cxx]                           |_[CoulombScat_e-]                                                                  :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x117 laps)
> [cxx]                           |_[ePairProd_e-]                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x117 laps)
> [cxx]                           |_[eBrem_e-]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x117 laps)
> [cxx]                           |_[eIoni_e-]                                                                        :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x351 laps)
> [cxx]                           |_[Transportation_e-]                                                               :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x468 laps)
> [cxx]                           |_[msc_e-]                                                                          :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x234 laps)
> [cxx]                         |_[StepLimiter_e-]                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x135 laps)
> [cxx]                         |_[CoulombScat_e-]                                                                    :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x135 laps)
> [cxx]                         |_[ePairProd_e-]                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x135 laps)
> [cxx]                         |_[eBrem_e-]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x135 laps)
> [cxx]                         |_[eIoni_e-]                                                                          :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x405 laps)
> [cxx]                         |_[Transportation_e-]                                                                 :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x540 laps)
> [cxx]                         |_[msc_e-]                                                                            :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x270 laps)
> [cxx]                       |_[StepLimiter_e-]                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x145 laps)
> [cxx]                       |_[CoulombScat_e-]                                                                      :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x145 laps)
> [cxx]                       |_[ePairProd_e-]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x145 laps)
> [cxx]                       |_[eBrem_e-]                                                                            :  0.000 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (3921.6%)  (x145 laps)
> [cxx]                       |_[eIoni_e-]                                                                            :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x435 laps)
> [cxx]                       |_[Transportation_e-]                                                                   :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x580 laps)
> [cxx]                       |_[msc_e-]                                                                              :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x290 laps)
> [cxx]                     |_[StepLimiter_e-]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x150 laps)
> [cxx]                     |_[CoulombScat_e-]                                                                        :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x150 laps)
> [cxx]                     |_[ePairProd_e-]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x150 laps)
> [cxx]                     |_[eBrem_e-]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x150 laps)
> [cxx]                     |_[eIoni_e-]                                                                              :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x450 laps)
> [cxx]                     |_[Transportation_e-]                                                                     :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x600 laps)
> [cxx]                     |_[msc_e-]                                                                                :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x300 laps)
> [cxx]                   |_[StepLimiter_e-]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x179 laps)
> [cxx]                   |_[CoulombScat_e-]                                                                          :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x179 laps)
> [cxx]                   |_[ePairProd_e-]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x179 laps)
> [cxx]                   |_[eBrem_e-]                                                                                :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x179 laps)
> [cxx]                   |_[eIoni_e-]                                                                                :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x537 laps)
> [cxx]                   |_[Transportation_e-]                                                                       :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x716 laps)
> [cxx]                   |_[msc_e-]                                                                                  :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x358 laps)
> [cxx]                 |_[StepLimiter_e-]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x251 laps)
> [cxx]                 |_[CoulombScat_e-]                                                                            :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x251 laps)
> [cxx]                 |_[ePairProd_e-]                                                                              :  0.000 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x251 laps)
> [cxx]                 |_[eBrem_e-]                                                                                  :  0.000 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (2109.7%)  (x253 laps)
> [cxx]                 |_[eIoni_e-]                                                                                  :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x753 laps)
> [cxx]                 |_[Transportation_e-]                                                                         :  0.002 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1004 laps)
> [cxx]                 |_[msc_e-]                                                                                    :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x502 laps)
> [cxx]               |_[StepLimiter_e-]                                                                              :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x519 laps)
> [cxx]               |_[CoulombScat_e-]                                                                              :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x515 laps)
> [cxx]               |_[ePairProd_e-]                                                                                :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x515 laps)
> [cxx]               |_[eBrem_e-]                                                                                    :  0.001 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x522 laps)
> [cxx]               |_[eIoni_e-]                                                                                    :  0.003 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x1547 laps)
> [cxx]               |_[Transportation_e-]                                                                           :  0.004 wall,  0.000 user +  0.010 system =  0.010 CPU [sec] (262.4%)  (x2060 laps)
> [cxx]               |_[msc_e-]                                                                                      :  0.002 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (413.6%)  (x1030 laps)
> [cxx]       |_[Transportation_anti_nu_e]                                                                            :  0.008 wall,  0.000 user +  0.000 system =  0.000 CPU [sec] (  0.0%)  (x3604 laps)
> [cxx]     |_[Transportation_nu_mu]                                                                                  :  0.007 wall,  0.010 user +  0.010 system =  0.020 CPU [sec] (271.2%)  (x3588 laps)
> [cxx]   |_[Transportation_anti_nu_mu]                                                                               :  0.008 wall,  0.010 user +  0.000 system =  0.010 CPU [sec] (119.7%)  (x3828 laps)
```