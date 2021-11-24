---
title: 'Building Keras from source: A follow along guide'
date: 2021-11-19
permalink: /blogs/building_keras_from_source/
tags:
  - keras
  - software engineering
  - machine learning
---
A step-by-step guide to building Keras.

Building Keras from source
======

This article originally appeared on [Towards Data Science](https://towardsdatascience.com/building-keras-from-source-a-follow-along-guide-2bcc4cea3aec).

Prelude:
--------
Keras has recently taken a big step towards improving developer inference by hosting the codebase in a separate repository. As mentioned in the [RFC](https://github.com/tensorflow/community/blob/master/rfcs/20200205-standalone-keras-repository.md), one of the main objectives is to eliminate the lengthy feedback loop caused due to long build times of the core TensorFlow library. Due to this change, it is now possible to run tests in an extremely feasible amount of time. 
 
This blog post aims to serve as a beacon for budding developers who wish to contribute to Keras but are not familiar with the building and testing procedure. Let’s dive in!


Building from source:
--------------------
To all the new ones here, I’d like to take a  moment to explain what “building from source” exactly means. This can mean many things (best explained [here](https://stackoverflow.com/questions/1622506/programming-definitions-what-exactly-is-building)), but in our case it means the following: 

> “Compile the source code into an installable package and link all modules to their respective endpoints” [1].

Note that even after this migration, Keras is still accessed by calling `from tensorflow import keras`. This is enabled by something known as golden APIs. These are endpoints exposed by the Keras library for TensorFlow library to pick up. Therefore, even though Keras is developed separately, for the user it still resides at `tf.keras`. You can learn more on this in this [post](https://stackoverflow.com/questions/1622506/programming-definitions-what-exactly-is-building). The code that enables this is available [here](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/api_template.__init__.py). 

I assume you are doing this on a Linux machine. Bonus point, this works flawlessly with TPU-enabled Cloud VMs.


All of the following commands were taken directly or inspired by the official Keras contributing [guide](https://github.com/keras-team/keras/blob/master/CONTRIBUTING.md). Please go through the same before opening a PR.

I’ve also created a [Colab notebook](https://colab.research.google.com/github/AdityaKane2001/keras_build_test/blob/main/Keras_build_test_notebook.ipynb), which you can use to build and test the code easily!

Part 1: Set up the environment
--------
Just like TensorFlow, Keras uses Bazel [2], a graph-based build management system. This means you can build Keras once and the successive builds will reuse the parts which have not changed since the previous one. Due to this, the time required to rebuild decreases dramatically. Here’s what we do to set up the environment:
```
#Install the latest version of Bazel. At the time of writing, the latest version was 4.2.1.
wget https://github.com/bazelbuild/bazel/releases/download/4.2.1/bazel-4.2.1-installer-linux-x86_64.sh
chmod +x bazel-4.2.1-installer-linux-x86_64.sh
./bazel-4.2.1-installer-linux-x86_64.sh
export PATH="$PATH:$HOME/bin"
bazel
```
Next we set up a virtual python environment. This is recommended if you’re working on a development machine. In Colab, it’s fine to reinstall Keras in the base environment. 
```
mkdir keras_installation
cd keras_installation
mkdir keras_env
python3 -m venv keras_env
source keras_env/bin/activate
```
Next we clone our development fork. We also install the nightly versions of TensorFlow, which ensures we’re in sync with the main TensorFlow repo.
```
# Replace BRANCH and USERNAME with your branch name and GitHub username respectively 
git clone -b BRANCH https://github.com/USERNAME/keras.git
cd keras
pip install -r requirements.txt
pip uninstall -y keras-nightly
pip install --upgrade tf-nightly
```

Part 2: Update golden APIs if any
--------
This part applies only if you’ve added some new files. You need to add their names in the following files. This ensures that your module will be built and accessible to the users later on.
```
.
└── keras/
    ├── api/
    │   ├── BUILD
    │   └── api_init_files.bzl
    ├── ...
    └── <submodule name>/
        └── BUILD
```

Part 3: Build and install
--------
Now is the crux of the process. Here we build and install our version of Keras. Use the following commands to do so: 
```
# Make sure you run the following command from the root of your Keras fork
bazel build //keras/tools/pip_package:build_pip_package
~/keras_installation/keras/bazel-bin/keras/tools/pip_package/build_pip_package ~/keras_installation/keras_pkg
pip3 install --force-reinstall --user ~/keras_installation/keras_pkg/keras-2.8.0-py2.py3-none-any.whl

# Note: The version 2.8.0 can change with changes in Keras versions. 
```
After executing the above commands, Keras will be installed anew with your change.
If you want to only conduct tests, then you can use `bazel test` instead of `bazel build`. In this case, you can make changes to the code and run `bazel test` again. You need not manually install the package as we do with `bazel build`.
Example:
```
bazel test keras/layers/convolutional_test
```
Here you can run as many tests as you like. You can run all tests using the following command:



```
!bazel test --test_timeout 300,450,1200,3600 --test_output=errors --keep_going --define=use_fast_cpp_protos=false --build_tests_only --build_tag_filters=-no_oss --test_tag_filters=-no_oss keras/...
```

Common errors:
--------

```
ERROR: /home/jupyter/.cache/bazel/_bazel_jupyter/ebc81b3ee71ff9bb69270887ebdc0d7b/external/bazel_skylib/lib/unittest.bzl:203:27: name 'analysis_test_transition' is not defined
ERROR: error loading package '': Extension 'lib/unittest.bzl' has errors
ERROR: error loading package '': Extension 'lib/unittest.bzl' has errors
INFO: Elapsed time: 3.557s
INFO: 0 processes.
FAILED: Build did NOT complete successfully (0 packages loaded)
```
Restart the VM. This happens just after installation, because path is not updated across the system. 

```
ImportError: cannot import name 'saved_metadata_pb2' from 'keras.protobuf' (unknown location)`  while importing 
```
Change directory and try again. This happens due to mixture of local and global environments


Acknowledgements
--------
I thank TPU Research Cloud (TRC) [3] for supporting this project. TRC provided TPU access for the duration of this project. Google supported this work by providing Google Cloud credit. Thanks to Qianli Scott Zhu from the Keras team for guiding me through the process.

Parting Thoughts
--------

Keras is a versatile and flexible library for deep learning. It is used by thousands of developers and is a big open source project. If you find a bug or  want a feature implemented in Keras, do it yourself! There’s no better joy than watching your code being used by countless people. And with being able to build Keras with ease, it has become within everyone’s reach to provide improvements to the codebase and make Keras a better product for everybody.


References
---------
[1] [Greg Mattes' answer on StackOverflow ](https://stackoverflow.com/questions/1622506/programming-definitions-what-exactly-is-building)

[2] ["Bazel - a fast, scalable, multi-language and extensible build system"](https://bazel.build/)

[3] [TPU Research Cloud](https://sites.research.google/trc/about/)