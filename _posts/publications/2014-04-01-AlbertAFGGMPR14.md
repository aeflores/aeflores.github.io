---
layout: post
title: "SACO: Static Analyzer for Concurrent Objects"
category: publication
---
#### Elvira Albert, Puri Arenas, Antonio Flores-Montoya, Samir Genaim, Miguel Gómez-Zamalloa, Enrique Martin-Martin, Germán Puebla, Guillermo Román-Díez
*In Proceedings of Tools and Algorithms for the Construction and Analysis of
Systems - 20th International Conference, TACAS 2014*  [link](http://costa.ls.fi.upm.es/papers/costa/AlbertAFGGMPR14.pdf)

We present the main concepts, usage and implementation of SACO, a static analyzer for concurrent objects. Interestingly, SACO is able to infer both liveness (namely termination and resource boundedness) and safety properties (namely deadlock freedom) of programs based on concurrent objects. The system integrates auxiliary analyses such as points-to and may-happen-in-parallel, which are essential for increasing the accuracy of the aforementioned more complex properties. SACO provides accurate information about the dependencies which may introduce deadlocks, loops whose termination is not guaranteed, and upper bounds on the resource consumption of methods.