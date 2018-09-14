from __future__ import absolute_import, division, print_function

import numpy as np

__all__ = ['scale_mag_as_flux', 'flux_to_mag', 'mag_to_flux',]

def scale_mag_as_flux(mag, flux_scale=1.0):
    """
    Identical to flux_to_mag(mag_to_flux(mag)*flux_scale)
    """
    return mag - 2.5*np.log10(flux_scale)

def flux_to_mag(flux, zeropoint_mag=0.0, from_unit=None, to_unit=None):
    if from_unit=='nMgy':
        zeropoint_mag=22.5
    return zeropoint_mag-2.5*np.log10(flux)

def mag_to_flux(mag, zeropoint_mag=0.0, from_unit=None, to_unit=None):
    if to_unit=='nMgy':
        zeropoint_mag=22.5
    return np.power(10.0, -0.4*(mag - zeropoint_mag))