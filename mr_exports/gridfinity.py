"""Gridfinity sample models published as MakerRepo artifacts."""

from __future__ import annotations

from mr import artifact

from gridfinity_build123d.base import BaseEqual
from gridfinity_build123d.baseplate import BasePlateBlockFrame, BasePlateEqual
from gridfinity_build123d.bin import Bin, StackingLip
from gridfinity_build123d.compartments import Compartment, CompartmentsEqual
from gridfinity_build123d.feature_locations import BottomCorners
from gridfinity_build123d.features import Label, MagnetHole, ScrewHole


@artifact
def artifact_baseplate_2x2() -> BasePlateEqual:
    """Publish a simple 2x2 frame baseplate artifact."""
    return BasePlateEqual(size_x=2, size_y=2, baseplate_block=BasePlateBlockFrame())


@artifact
def artifact_base_2x2() -> BaseEqual:
    """Publish a plain 2x2 base artifact."""
    return BaseEqual(grid_x=2, grid_y=2)


@artifact
def artifact_bin_2x2() -> Bin:
    """Publish a basic 2x2 bin with magnets, screws, and label compartments."""
    return Bin(
        base=BaseEqual(
            grid_x=2,
            grid_y=2,
            features=[
                MagnetHole(BottomCorners()),
                ScrewHole(BottomCorners()),
            ],
        ),
        height_in_units=5,
        compartments=CompartmentsEqual(
            div_x=2,
            div_y=2,
            compartment_list=Compartment(features=Label()),
        ),
        lip=StackingLip(),
    )
