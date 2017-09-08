---
layout: post
title: "MayPar: a may-happen-in-parallel analyzer for concurrent objects"
category: publication
---
#### Elvira Albert, Antonio Flores-Montoya, Samir Genaim
*In 20th ACM SIGSOFT Symposium on the Foundations of Software
Engineering (FSE-20), SIGSOFT/FSE'12*  [link](http://dl.acm.org/citation.cfm?id=2393611)

We present the concepts, usage and prototypical implementation of MayPar, a may-happen-in-parallel (MHP) static analyzer for a distributed asynchronous language based on concurrent objects. Our tool allows analyzing an application and finding out the pairs of statements that can execute in parallel. The information can be displayed by means of a graphical representation of the MHP analysis graph or, in a textual way, as a set of pairs which identify the program points that may run in parallel. The information yield by MayPar can be relevant (1) to spot bugs in the program related to fragments of code which should not run in parallel and also (2) to improve the precision of other analyses which infer more complex properties (e.g., termination and cost).