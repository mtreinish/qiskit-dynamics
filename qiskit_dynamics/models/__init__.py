# -*- coding: utf-8 -*-

# This code is part of Qiskit.
#
# (C) Copyright IBM 2020.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""
==========================================
RHS Models (:mod:`qiskit_dynamics.models`)
==========================================

.. currentmodule:: qiskit_dynamics.models

Tools for constructing differential equation models to pass to solving routines.

Quantum Models
==============

Models for quantum systems.

.. autosummary::
   :toctree: ../stubs/

   HamiltonianModel
   LindbladModel

Generator Models
================

Tools for constructing generators for LMDEs.

.. autosummary::
   :toctree: ../stubs/

   BaseFrame
   Frame
   GeneratorModel
"""

from .frame import BaseFrame, Frame
from .generator_models import GeneratorModel
from .hamiltonian_models import HamiltonianModel
from .lindblad_models import LindbladModel
