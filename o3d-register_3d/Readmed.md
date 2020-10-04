# Register 3d - Point Cloud registration

O3D modifications to python Teaser++
```
https://github.com/MIT-SPARK/TEASER-plusplus/tree/feature/python-fpfh-example
```

## Setup - WSL
* install bindings for Teaser++
* start Xserver Xming on Windows 10,  export DISPLAY=:0 on client

### Usage
```
r = Registration()
r.estimate(pc1, pc2)
```

## Example code
```
cd o3d-registration_3d
python3d registration.py
``` 


