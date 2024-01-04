# blend-to-gradient
New renderer for converting Blender scenes to GD (based on [@IliasHDZ](https://github.com/iliasHDZ)'s renderer, ported to G.js)

# Features
- Support for animation (though extremely wonky and only works correctly 0.5% of the time)
- Support for materials
- Support for both tris and quads
- Correct layering for gradients

# TODO
- Fix animations so they do not stretch (move vertices to correct positions)
- Optimize as much as possible
- Add better lighting (possible support for lights inside scenes?)
- Add smooth shading (might not be possible, but it is a goal)
