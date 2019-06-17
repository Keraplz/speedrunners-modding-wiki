
# Trail files

## Overview

Trail files are used by the game to render trails.

## File format

Trail files (.srt) are standard zip files. To access the contents of the trail, simply rename `file.srt` to `file.zip`, then use windows explorer, [7-Zip](https://www.7-zip.org/download.html) or [Winrar](https://www.rarlab.com/download.htm) to extract the archive.

A normal trail file will have the following files:

#### settings.trail

This contains the properties and their values for each layer. The file structure is defined like this: 

```c
typedef struct Image {
    byte name_length;
    char name[name_length];
    byte image_lengthl
    char image[image_length];
}

typedef struct Layer {
    byte type_length;
    char type[type_length];
    byte properties_length;
    Property properties[property_length];
}

typedef struct Property {
    byte name_length;
    char name[name_length];
    byte value_length;
    char value[value_length];
}

int version;
byte name_length;
char name[name_length];
byte description_length;
char description[description_length];
long long last_updated;
byte icon_length;
char icon[icon_length];
byte image_count;
Image img[image_count];
byte layer_count;
```

#### icon

The trail icon as a png file (but without the file extension `.png`). The default trail icon size is 64x64.

#### .png

The screenshot preview of the trail as an unnamed png file. The default screenshot size is 370x370

#### file.png

Any images used by the trail as png images

## Layers

There are 3 types of layers:

#### Stripe

Horizontal stripes. They can be a single image (animations not supported) and they have 3 unique `Sinewave` properties that allow for sinusoidal movevent of the stripe

#### Particle

Particles that are emitted with a given velocity at a given rate. They can be a static image or a spritesheet of multiple animation frames.

#### Animation

A static image or animated sprite.

## Properties

The game uses properties that define the behavior and appearance of trails. The recognised properties and their default values are listed below.

### Stripe layer

<table width=100%><tr><th>Property name</th><th>Default value</th></tr><tr><td>Enabled</td><td>NEVER</td></tr><tr><td>Order</td><td>2</td></tr><tr><td>Layer</td><td>TrailBehindLocalPlayersLayer</td></tr><tr><td>Image</td><td></td></tr><tr><td>Visible</td><td>TRUE</td></tr><tr><td>LifeTime</td><td>2</td></tr><tr><td>Color</td><td>1,1,1</td></tr><tr><td>Taper</td><td>FALSE</td></tr><tr><td>FadeOut</td><td>FALSE</td></tr><tr><td>FadeOut Speed</td><td>1</td></tr><tr><td>Opacity</td><td>1</td></tr><tr><td>Size</td><td>40</td></tr><tr><td>Offset</td><td>0</td></tr><tr><td>X-Offset</td><td>0</td></tr><tr><td>OffsetVector</td><td>0,0</td></tr><tr><td>Invert Offset</td><td>TRUE</td></tr><tr><td>Flip Horizontally</td><td>FALSE</td></tr><tr><td>Flip Vertically</td><td>FALSE</td></tr><tr><td>Force right side Up</td><td>FALSE</td></tr><tr><td>Noise</td><td>0</td></tr><tr><td>Sinewave Amplitude</td><td>0</td></tr><tr><td>Sinewave Frequency</td><td>0</td></tr><tr><td>Sine Phase Offset</td><td>0</td></tr></table>

### Particle layer

<table width=100%><tr><th>Property name</th><th>Default value</th></tr><tr><td>Enabled</td><td>NEVER</td></tr><tr><td>Order</td><td>1</td></tr><tr><td>Layer</td><td>TrailBehindLocalPlayersLayer</td></tr><tr><td>Image</td><td>N/A</td></tr><tr><td>Visible</td><td>TRUE</td></tr><tr><td>isAnimated</td><td>FALSE</td></tr><tr><td>spriteMode</td><td>DEFAULT</td></tr><tr><td>SpriteSize</td><td>100,100</td></tr><tr><td>SpriteCount</td><td>1,1</td></tr><tr><td>FPS</td><td>30</td></tr><tr><td>Spawn Rate</td><td>0.25</td></tr><tr><td>Amount</td><td>1</td></tr><tr><td>LifeTime</td><td>1</td></tr><tr><td>FadeOut</td><td>TRUE</td></tr><tr><td>Scale</td><td>1</td></tr><tr><td>ScaleSpeed</td><td>-1</td></tr><tr><td>Scale Variance</td><td>0.5</td></tr><tr><td>Rotation</td><td>0</td></tr><tr><td>Rotation Variance</td><td>0</td></tr><tr><td>Rotation Speed</td><td>0</td></tr><tr><td>Rotation Speed Variance</td><td>0</td></tr><tr><td>Rotate with Player</td><td>FALSE</td></tr><tr><td>Color</td><td>1,1,1</td></tr><tr><td>Opacity</td><td>1</td></tr><tr><td>Offset</td><td>0,0</td></tr><tr><td>OffsetVariance</td><td>0,0</td></tr><tr><td>Force</td><td>0</td></tr><tr><td>Force Variance</td><td>0</td></tr><tr><td>Direction</td><td>1,0</td></tr><tr><td>Direction Variance</td><td>0,0</td></tr><tr><td>Use World Axis</td><td>FALSE</td></tr><tr><td>Same Side Up</td><td>FALSE</td></tr><tr><td>hasGravity</td><td>FALSE</td></tr><tr><td>gravity</td><td>0,0</td></tr></table>

### Animation layer

<table width=100%><tr><th>Property name</th><th>Default value</th></tr><tr><td>Enabled</td><td>NEVER</td></tr><tr><td>Order</td><td>0</td></tr><tr><td>Layer</td><td>TrailBehindLocalPlayersLayer</td></tr><tr><td>Image</td><td>N/A</td></tr><tr><td>Visible</td><td>TRUE</td></tr><tr><td>SpriteCount</td><td>1,1</td></tr><tr><td>FPS</td><td>30</td></tr><tr><td>Color</td><td>1,1,1</td></tr><tr><td>Opacity</td><td>1</td></tr><tr><td>Offset</td><td>0,0</td></tr><tr><td>Scale</td><td>1</td></tr><tr><td>FadeIn</td><td>0</td></tr><tr><td>FadeOut</td><td>0</td></tr><tr><td>ScaleOut</td><td>0</td></tr><tr><td>Force right side Up</td><td>FALSE</td></tr><tr><td>Rotate with Player</td><td>TRUE</td></tr><tr><td>Move when inactive</td><td>TRUE</td></tr></table>

### Misc

<table width=100%><tr><th>Property name</th><th>Default value</th></tr><tr><td>Is Beta Trail</td><td>FALSE</td></tr></table>

## Tools / Resources

- [srtail - a python library for modifying trails by pop4959](https://github.com/pop4959/srtrail)
