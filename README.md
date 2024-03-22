This is a simple django restful API that receive a POST .glb/.gltf file and receive a converted .usdz file.

Apple [USDZ Tools v0.66](https://developer.apple.com/augmented-reality/tools/files/USDPython-pkg.zip) is required for this API. This tool only works on Apple silicon machines.

Before start, make sure that python 3.7.9 or later version is installed on your mac. In order to run USDZ tools locally without running USD.command, add the following line in `~/.zprofile`:

```sh
# Replace {TOOLS PATH} with `usdzpython` path
export PATH=$PATH:{TOOLS PATH}/USD:$PATH:{TOOLS PATH}/usdzconvert;
export PYTHONPATH=$PYTHONPATH:{TOOLS PATH}/USD/lib/python

# Set the PYTHONPATH to FBX Bindings
export PYTHONPATH=$PYTHONPATH:"/Applications/Autodesk/FBX Python SDK/2020.2.1/lib/Python37_x64"
```

To run server:
```
cd mac_usdz_converter
python manage.py runserver
```
