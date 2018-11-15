# Introduction

This document reflects my (Seth's) limited understanding of the issues at hand and what I think should be guiding principles for the proxy app if my understanding is more or less correct.

This is meant as another starting point for discussion and not as a manifesto :) 

# Motivation 

Computational physicists estimate that the next generation of particle physics experiments will require an increase in simulation throughput on the order of 100× by the mid-2020s. This computational burden can only be satisfied with exascale computer architectures and an exascale-ready particle physics application.

The number and complexity of physical processes necessary in these simulations are not straightforwardly amenable to execution on the GPU accelerators that provide most of the computational power of the current and next generation of machines. There is therefore a strong need for an application that can approximately *represent* the challenges of the necessary particle physics but can be rapidly changed to determine how to obtain maximum performance on pre-exascale systems.

This requirement implies three key guiding principles for the proxy app:
 1. Modularity. We need to be able to determine whether changing a physics model, a geometry implementation, or even the overall program flow can substantially improve performance.
 2. Simplicity. The app may be implemented on multiple architectures with multiple programming paradigms. 
 3. Scalability. The application needs to be fast *at scale*, which means the components of the app should be parameterized so that both small and large problems can be run on both small and large machines.

# Next steps

We need to identify the following before we can actually write a requirements document. We should also be careful to separate a requirement ("geometric representation of an array of tubes") from an implementation of that requirement ("GDML input of a tube array").

## Capabilities 

What is the *smallest* set of capabilities that can reasonably represent a real-life simulation? What are the ultimate anticipated set of capabilities needed for an exascale-level simulation?

## Data usage and access patterns

What are the data requirements for these capabilities? This includes:
 - Fixed memory requirements of the problem geometry 
 - Fixed memory requirements of the physics kernels
 - Amount of data input per event
 - Amount of data *output* per event

## Parameters

What are the key areas of *scalable* complexity? These might include:
 - Number of events, and amount of data that needs to be collected per event
 - Number of physics modules, and amount of cross section data in each of the modules
 - Number of geometrical regions, and the depth of their CSG representation

What ranges do these values take, from most simple test case to most complex
anticipated simulation?

