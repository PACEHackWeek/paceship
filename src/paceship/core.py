import numpy as np
from PIL import Image, ImageEnhance

def l3enhance(
    rgb,
    scale=0.01,
    vmin=0,
    vmax=1.1,
    gamma=1,
    contrast=1.1,
    brightness=1,
    sharpness=1.1,
    saturation=1,
):
    """Enhance a RGB data array for visualization.

    Parameters
    ----------
    rgb
        the input data array with shape (M, N, 3)
    scale
        scaling factor in rgb normalization
    vmin
        minimum value to which normalized rgb is clipped
    vmax
        maximum value to which normalized rgb is clipped
    gamma
        scaling factor applied to normalized rgb
    contrast
        see PIL.ImageEnhance.Contrast
    brightness
        see PIL.ImageEnhance.Brightness
    sharpness
        see PIL.ImageEnhance.Sharpness
    saturation
        see PIL.ImageEnhance.Color

    Returns
    -------
        the input data array with modified data
    """
    
    da = rgb.where(rgb > 0)
    da = np.log(da / scale) / np.log(1 / scale)
    da = da.clip(vmin, vmax)
    da = (da - da.min()) / (da.max() - da.min())
    da = da * gamma
    da = da * 255
    da = da.where(da.notnull(), 0).astype("uint8")
    img = Image.fromarray(da.data)
    enhancer = ImageEnhance.Contrast(img)
    img = enhancer.enhance(contrast)
    enhancer = ImageEnhance.Brightness(img)
    img = enhancer.enhance(brightness)
    enhancer = ImageEnhance.Sharpness(img)
    img = enhancer.enhance(sharpness)
    enhancer = ImageEnhance.Color(img)
    img = enhancer.enhance(saturation)
    rgb[:] = np.array(img) / 255
    
    return rgb