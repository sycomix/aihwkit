# -*- coding: utf-8 -*-

# (C) Copyright 2020, 2021 IBM. All Rights Reserved.
#
# This code is licensed under the Apache License, Version 2.0. You may
# obtain a copy of this license in the LICENSE.txt file in the root directory
# of this source tree or at http://www.apache.org/licenses/LICENSE-2.0.
#
# Any modifications or derivative works of this code must retain this
# copyright notice, and modified files need to carry a notice indicating
# that they have been altered from the originals.

"""Configurations presets for resistive processing units."""

from .configs import (
    # Single device configs.
    ReRamESPreset, ReRamSBPreset, CapacitorPreset, EcRamPreset, IdealizedPreset,
    GokmenVlasovPreset,
    # 2-device configs.
    ReRamES2Preset, ReRamSB2Preset, Capacitor2Preset, EcRam2Preset, Idealized2Preset,
    # 4-device configs.
    ReRamES4Preset, ReRamSB4Preset, Capacitor4Preset, EcRam4Preset, Idealized4Preset,
    # Tiki-taka configs.
    TikiTakaReRamESPreset, TikiTakaReRamSBPreset, TikiTakaCapacitorPreset,
    TikiTakaEcRamPreset, TikiTakaIdealizedPreset
)
