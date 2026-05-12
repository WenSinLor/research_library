---
citation_key: Boyd1985fading
title: "Fading Memory and the Problem of Approximating Nonlinear Operators with Volterra Series"
authors: "Boyd and Chua"
year: 1985
created: 2026-05-12
paper_type: "theory"
read_status: "skimmed"
tags:
  - methodologies-and-techniques
  - dynamical-systems
---

# Boyd1985fading — Fading Memory and the Problem of Approximating Nonlinear Operators with Volterra Series

## 1. Core contribution

The paper shows that fading memory is a sufficient structural property for approximating broad classes of nonlinear operators with Volterra-series models. In particular, time-invariant continuous nonlinear operators with fading memory can be uniformly approximated by finite Volterra representations over suitable signal sets. The work also connects these approximants to finite-dimensional linear dynamical systems followed by nonlinear readouts. This makes fading memory a central organizing condition for nonlinear system approximation.

## 2. Method / mechanism / evidence

Boyd and Chua formalize fading memory through weighted input norms that discount distant history, then prove approximation results for continuous operators under that topology. They derive both continuous-time Volterra approximants and discrete-time nonlinear moving-average counterparts. The argument improves on earlier finite-horizon or compact-domain results by handling behavior over all time on broader signal classes. The paper is theoretical, with the main evidence carried by constructive approximation theorems.

## 3. Key takeaway and limitation

The paper's enduring point is that finite-history-like nonlinear models are principled when the target system gradually forgets old inputs. That idea later becomes relevant to reservoir computing and other recurrent approximators that rely on stable fading-memory behavior. The main limitation is that the approximation theorems do not by themselves tell a practitioner how large an expansion is needed or how to identify it efficiently from data. Systems without fading memory fall outside the guarantee.

## 4. Open question

What practical identification procedures can exploit the fading-memory approximation result while controlling model order and sample complexity?
