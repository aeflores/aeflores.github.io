---
layout: page
title: Software
---

### [CoFloCo](http://aeflores.github.io/CoFloCo/) ([github](https://github.com/aeflores/CoFloCo))

I developed CoFloCo, a static analysis tool to infer automatically symbolic complexity upper and lower bounds of imperative and recursive programs. CoFloCo’s analysis is not binded to any specific programming language, instead it takes an abstract representation of programs as an input. The abstract representation is a set of cost equations that can be generated from source code, bytecode or other intermediate representations.

#### Related publications:
* [Cost Analysis of Programs Based on the Refinement of Cost Relations](https://aeflores.github.io/publication/2017/09/01/Flores17/)
* [Upper and Lower Amortized Cost Bounds of Programs Expressed as Cost Relations](https://aeflores.github.io/publication/2016/11/01/FM16/)
* [Resource Analysis of Complex Programs with Cost Equations](https://aeflores.github.io/publication/2014/11/01/FMH14/)


### [SACO](http://costa.ls.fi.upm.es/web/saco.php)

I participated in the development of SACO,  a static analyzer for concurrent objects. It analyzes programs written in [ABS](http://abs-models.org/)
and performs the following static analyses:

* [Termination and Resource analysis](https://aeflores.github.io/publication/2017/06/01/AlbertFGM17/)
* [Deadlock analysis](https://aeflores.github.io/publication/2013/06/01/FloresAG13/)

In addition, SACO performs auxiliary static analyses: 
 
* Points-to analysis
* May-happen-in-parallel:
  + [May-Happen-in-Parallel Analysis for Asynchronous Programs with Inter-Procedural Synchronization](http://costa.ls.fi.upm.es/papers/costa/AlbertGG15.pdf)

  + [May-Happen-in-Parallel Analysis for Actor-based Concurrency](https://aeflores.github.io/publication/2016/03/01/AlbertFGM15/)

  
  

