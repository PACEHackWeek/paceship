import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from shapely.geometry import box
import geopandas as gpd


def simple_bbox(bbox, projection='PlateCarree'):
    """
    Plot a bounding box on a global map using Cartopy.

    This function displays a world map with coastlines and borders, and overlays
    a red bounding box. Optionally, it can render the Earth as a globe using
    Orthographic projection centered on the bounding box.

    Parameters
    ----------
    bbox : list or tuple of float
        Bounding box in [min_lon, min_lat, max_lon, max_lat] format.

    projection : str, optional
        Map projection to use. Options include:
            - 'PlateCarree' (default)
            - 'Robinson'
            - 'Mollweide'
            - 'Mercator'
            - 'EqualEarth'
            - 'InterruptedGoodeHomolosine'
            - 'globe' (for Orthographic projection centered on the bbox)

    Returns
    -------
    None
        Displays the plot using matplotlib.

    Example
    -------
    >>> plot_global_bbox([-25, 10, -10, 30], projection='globe')
    """
    if not (isinstance(bbox, (list, tuple)) and len(bbox) == 4):
        raise ValueError("bbox must be a list or tuple of four floats: [min_lon, min_lat, max_lon, max_lat]")

    min_lon, min_lat, max_lon, max_lat = bbox

    # Projection handling
    projection_dict = {
        'PlateCarree': ccrs.PlateCarree(),
        'Robinson': ccrs.Robinson(),
        'Mollweide': ccrs.Mollweide(),
        'Mercator': ccrs.Mercator(),
        'EqualEarth': ccrs.EqualEarth(),
        'InterruptedGoodeHomolosine': ccrs.InterruptedGoodeHomolosine(),
    }

    if projection == 'globe':
        center_lon = (min_lon + max_lon) / 2
        center_lat = (min_lat + max_lat) / 2
        proj = ccrs.Orthographic(central_longitude=center_lon, central_latitude=center_lat)
    elif projection in projection_dict:
        proj = projection_dict[projection]
    else:
        raise ValueError(f"Unsupported projection '{projection}'. Choose from {list(projection_dict.keys()) + ['globe']}.")

    # Plot setup
    fig, ax = plt.subplots(figsize=(12, 6), subplot_kw={"projection": proj})
    if projection == 'globe':
        ax.set_global()
    else:
        ax.set_global()

    ax.coastlines()
    ax.add_feature(cfeature.LAND, facecolor="lightgray")
    ax.add_feature(cfeature.BORDERS, linestyle=":")
    if projection != 'globe':
        ax.gridlines(draw_labels=True, crs=ccrs.PlateCarree())

    # Bounding box
    gdf = gpd.GeoDataFrame(
        geometry=[box(min_lon, min_lat, max_lon, max_lat)],
        crs="EPSG:4326"
    )
    gdf.boundary.plot(ax=ax, edgecolor="red", linewidth=2, transform=ccrs.PlateCarree())

    title = "Study Area"
    ax.set_title(title, fontsize=14)
    plt.show()
