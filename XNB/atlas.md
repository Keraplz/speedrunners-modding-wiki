# Atlas XNB files

Sample .json file

```json
{
	"frames": [
	{
		"filename": "321GO0001.png",
		"frame": {"x":1348,"y":1300,"w":68,"h":140},
		"rotated": false,
		"trimmed": true,
		"spriteSourceSize": {"x":115,"y":38,"w":68,"h":140},
		"sourceSize": {"w":270,"h":180}
	},
	{
		"filename": "Double-Jump0001.png",
		"frame": {"x":1962,"y":1202,"w":84,"h":126},
		"rotated": false,
		"trimmed": true,
		"spriteSourceSize": {"x":107,"y":25,"w":84,"h":126},
		"sourceSize": {"w":270,"h":180}
	}]
}

```

.json Documentation

* ``frames``: A list containing all the animation frames
  * ``filename``: The name of the animation plus the file extension (normally a .png)
  * ``frame``: Data related to this frame within the sheet
    * ``x``: The horizontal position of this frame within the sheet, from left to right
    * ``y``: The vertical position of this frame within the sheet, from top to bottom
    * ``w``: The width of this frame within the sheet
    * ``h``: The width of this frame within the sheet
  * ``rotated``: *true* if this frame has been rotated when packing, *false* if not (270-degree clockwise rotation by default)
  * ``trimmed``: *true* if this frame has been trimmed when packing, *false* if not (removed fully empty columns/rows of pixels)
  * ``spriteSourceSize``: Data for non-empty columns/rows of pixels
    * ``x``: The horizontal position of this frame within the sprite, from left to right
    * ``y``: The vertical position of this frame within the sprite, from top to bottom
    * ``w``: The width of this frame within the sprite
    * ``h``: The width of this frame within the sprite
  * ``sourceSize``: Data related to sprite size
    * ``w``: The width of this sprite
    * ``h``: The height of this sprite
    
Structure

```csharp
    /// <summary>
    /// Array of frame data
    /// </summary>
    public Sprite[] frames;

    /// <summary>
    /// Holds all necessary data about sprite Position and Size
    /// </summary>
    public struct Sprite
    {
        /// <summary>
        /// Sprite name with extension
        /// </summary>
        public string filename;

        /// <summary>
        /// Position of the sprite graphic inside the spritesheet
        /// and Size of the sprite graphic
        /// </summary>
        public Frame frame;

        /// <summary>
        /// True if spritesheet was compiled with rotated sprites
        /// </summary>
        public bool rotated;

        /// <summary>
        /// True if spritesheet was compiled with trimmed sprites
        /// </summary>
        public bool trimmed;

        /// <summary>
        /// Position and Size of sprite graphic
        /// </summary>
        public SpriteSourceSize spriteSourceSize;

        /// <summary>
        /// Size of sprite image
        /// </summary>
        public SourceSize sourceSize;

        /// <summary>
        /// 
        /// </summary>
        /// <param name="filename">Sprite name with extension</param>
        /// <param name="frame">Position and Size of the sprite inside the spritesheet</param>
        /// <param name="rotated">True if spritesheet was compiled with rotated sprites</param>
        /// <param name="trimmed">True if spritesheet was compiled with trimmed sprites</param>
        /// <param name="spriteSourceSize">Position and Size of sprite graphic</param>
        /// <param name="sourceSize">Size of sprite image</param>
        public Sprite(string filename, Frame frame, bool rotated, bool trimmed, SpriteSourceSize spriteSourceSize, SourceSize sourceSize)
        {
            this.filename = filename;
            this.frame = frame;
            this.rotated = rotated;
            this.trimmed = trimmed;
            this.spriteSourceSize = spriteSourceSize;
            this.sourceSize = sourceSize;
        }

    }

    /// <summary>
    /// The position of the sprite inside the spritesheet
    /// </summary>
    public struct Frame
    {
        /// <summary>
        /// Horizontal position of the sprite graphic inside the spritesheet
        /// </summary>
        public int x;

        /// <summary>
        /// Vertical position of the sprite graphic inside the spritesheet
        /// </summary>
        public int y;

        /// <summary>
        /// Width of the sprite graphic
        /// </summary>
        public int w;

        /// <summary>
        /// Height of the sprite graphic
        /// </summary>
        public int h;

        /// <summary>
        /// 
        /// </summary>
        /// <param name="x">Horizontal position of the sprite graphic inside the spritesheet</param>
        /// <param name="y">Vertical position of the sprite graphic inside the spritesheet</param>
        /// <param name="w">Width of the sprite graphic</param>
        /// <param name="h">Height of the sprite graphic</param>
        public Frame(int x, int y, int w, int h)
        {
            this.x = x;
            this.y = y;
            this.w = w;
            this.h = h;
        }
    }

    /// <summary>
    /// The size of the sprite inside the spritesheet
    /// </summary>
    public struct SpriteSourceSize
    {
        /// <summary>
        /// Horizontal position of the sprite graphic
        /// </summary>
        public int x;

        /// <summary>
        /// Vertical position of the sprite graphic
        /// </summary>
        public int y;

        /// <summary>
        /// Width of the sprite graphic
        /// </summary>
        public int w;

        /// <summary>
        /// Height of the sprite graphic
        /// </summary>
        public int h;

        /// <summary>
        /// Holds data of the sprite graphic inside the image
        /// </summary>
        /// <param name="x">Horizontal Position</param>
        /// <param name="y">Vertical Position</param>
        /// <param name="w">Width</param>
        /// <param name="h">Height</param>
        public SpriteSourceSize(int x, int y, int w, int h)
        {
            this.x = x;
            this.y = y;
            this.w = w;
            this.h = h;
        }
    }

    /// <summary>
    /// Size of the sprite
    /// </summary>
    public struct SourceSize
    {
        /// <summary>
        /// Width of the sprite
        /// </summary>
        public int w;

        /// <summary>
        /// Height of the sprite
        /// </summary>
        public int h;

        /// <summary>
        /// Size for sprite image
        /// </summary>
        /// <param name="w">Width</param>
        /// <param name="h">Height</param>
        public SourceSize(int w, int h)
        {
            this.w = w;
            this.h = h;
        }
    }
```
