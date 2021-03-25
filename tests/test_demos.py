import pytest

from pyvista import demos
from pyvista.plotting import system_supports_plotting

skip_no_plotting = pytest.mark.skipif(not system_supports_plotting(),
                                      reason="Test requires system to support plotting")


def test_glyphs():
    demos.glyphs(2)


def test_atomized():
    grid = demos.logo_atomized(density=0.2, scale=0.6)
    assert grid.n_cells


def test_logo_basic():
    pd = demos.logo_basic()
    assert pd.n_faces


def test_logo_voxel():
    grid = demos.logo_voxel()
    assert grid.n_cells


@skip_no_plotting
def test_plot_logo():
    # simply should not fail
    demos.plot_logo()
